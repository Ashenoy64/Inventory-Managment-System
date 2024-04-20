import streamlit as st  
import backend
import os 
import dotenv
import rabbitmq_connector
import threading

dotenv.load_dotenv()


def dashboard():
    st.header("Dashboard",divider="blue")
    report = backend.get_report()
    revenue = float(report['report'][1])
    investment = float(report['report'][0])

    with st.container():
        col1, col2= st.columns(2)
        with col1:
            st.metric("Total Orders", report['orders'])
        with col2:
            st.metric("Total Products",report['products'] )

    with st.container():
        col1, col2,col3 = st.columns(3)
        with col1:
            st.metric("Total Revenue", revenue)
        with col2:
            st.metric("Total Investment", investment)  
        with col3:
            st.metric("Profit",value=f"{revenue-investment} ₹",delta_color="inverse")
        pass

    with st.container():
        choice = st.selectbox("Select Product",["Order Trend",'Popular Product'])
        if choice == "Order Trend":
            order_trend = backend.get_order_count()
            with st.container():
                data_dict = {str(date): count for date, count in order_trend}
                st.line_chart(data_dict)
                pass
            pass
        elif choice == "Popular Product":
            product_trend = backend.get_product_count()
            with st.container():
                sorted_data = sorted(product_trend, key=lambda x: x[1], reverse=True)
                top_items = sorted_data[:10]
                data_dict = {name: count for name, count in top_items}
                st.bar_chart(data_dict)
            pass
        

def orders():
    st.header("Orders",divider="blue")
    failed_orders = backend.get_failed_orders()
    success_orders = backend.get_success_stock()

    with st.container():
        col1,col2,col3,col4= st.columns(4)
        with col1:
            st.metric("Failed Orders",value=len(failed_orders))
        with col2:
            st.metric("Success Orders",value=len(success_orders))
        with col3:
            st.metric("Total Orders",value=len(failed_orders)+len(success_orders))
        with col4:
            st.metric("Success Rate",value=f"{(len(success_orders)/(len(failed_orders)+len(success_orders)))*100} %",delta_color="inverse")

    with st.container():
        if(len(failed_orders)!=0):
            with st.container():
                st.subheader("Failed Orders")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write("Order ID")
                with col2:
                    st.write("Order Date")
                with col3:
                    st.write("Total")
                for order in failed_orders:
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.write(order[0])
                    with col2:
                        st.write(order[1])
                    with col3:
                        st.write(order[2])
        with st.container():
            st.subheader("Success Orders")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Order ID")
            with col2:
                st.write("Order Date")
            with col3:
                st.write("Total")
            for order in success_orders:
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(order[0])
                with col2:
                    st.write(order[1])
                with col3:
                    st.write(order[2])

    pass


def products():
    #Get All Products
    #Get stocks which are empty
    #Restock
    #Add New Product
    # empty_stocks = backend.get_empty_stock()
    # products = backend.get_product()

    st.header("Products",divider="blue")

    option = st.selectbox(
    'What you wanna do?',
    ('Get All Products', 'Get Empty Products', 'Add new Product','Restock Product'))

    if option == 'Get All Products':
        products = backend.get_product()
        with st.container():
            st.subheader("All Products")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write("Product ID")
            with col2:
                st.write("Product Name")
            with col3:
                st.write("Price")
            with col4:
                st.write("Quantity")
            for product in products:
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.write(product[0])
                with col2:
                    st.write(product[1])
                with col3:
                    st.write(product[2])
                with col4:
                    st.write(product[3])
        pass

    elif option == 'Get Empty Products':
        empty_stocks = backend.get_empty_stock()
        with st.container():
            st.subheader("Empty Stocks")
            col1, col2,col3 = st.columns(3)
            with col1:
                st.write("Product ID")
            with col2:
                st.write("Product Name")
            with col3:
                st.write("Price")
            for product in empty_stocks:
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(product[0])
                with col2:
                    st.write(product[1])
                with col3:
                    st.write(product[2])
        pass

    elif option == 'Add new Product':
        name = st.text_input("Product Name")
        price = st.number_input("Price")
        quantity = st.number_input("Quantity",step=1)
        if st.button("Add Product"):
            backend.add_new_product(name,quantity,price,st.session_state.producer)
        pass

    elif option == 'Restock Product':
        products = backend.get_product()

        product_name = st.selectbox("Select Product",[product[1] for product in products])

        if (product_name):
            product_id = [product[0] for product in products if product[1]==product_name][0]
            
            price = st.number_input("Price")
            quantity = st.number_input("Quantity",step=1,min_value=1)
            if st.button("Restock"):
                backend.restock_product(product_id,quantity,price,st.session_state.producer)
        # quantity = st.number_input("Quantity")
        # if st.button("Restock"):
        #     backend.restock_product(product_id,quantity,st.session_state.producer)

            



    pass


       

if __name__ == "__main__":
   

    if 'producer' not in st.session_state:
        st.session_state.producer = rabbitmq_connector.Connector(port=os.getenv("RABBITMQ_PORT"),queue=os.getenv("RABBITMQ_QUEUE_PRODUCT"),host=os.getenv("RABBITMQ_HOST"))
    
    if 'health' not in st.session_state:
        st.session_state.health = threading.Thread(target=backend.heartbeat)
        st.session_state.health.start()
        
    st.title("Product Management Service",anchor="top")
    page = st.sidebar.radio("Navigation", ("Dashboard", "Orders","Products"))
    
    if page =="Dashboard":
        dashboard()
    elif page =="Orders":
        orders()
    elif page =="Products":
        products()
    else :
        pass
