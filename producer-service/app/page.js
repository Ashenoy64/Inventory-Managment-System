"use client";
import { useEffect, useState } from "react";
import { Products } from "@/components/Products";
import { CartOrder } from "@/components/CartOrder";
export default function Home() {
  const [products, setProducts] = useState([])
  const [cart, setCart] = useState([])
  const [grandTotal, setGrandTotal] = useState(0)
  useEffect(() => {
    fetch('http://localhost:3000/api/products')
      .then(response => response.json())
      .then(data => { setProducts(data) })
  }, [])

  const HandleButton = (ops, product) => {
    if (ops === "add") {
      let cartProduct = cart.find((item) => item.id === product.id);
      if (cartProduct) {
        if (product.quantity > cartProduct.quantity) {
          cartProduct.quantity += 1;
          cartProduct.total = cartProduct.price * cartProduct.quantity;
          setGrandTotal((prev) => prev +parseFloat(cartProduct.price));
        }
      } else {
        if (product.quantity > 0) {
          cartProduct = {
            id: product.id,
            name: product.name,
            price: product.price,
            quantity: 1,
            total: product.price,
          };
          setCart([...cart, cartProduct]);
          setGrandTotal((prev) => prev +  parseInt(cartProduct.price));
        }
      }
    } else if (ops === "remove") {
      let cartProduct = cart.find((item) => item.id === product.id);
      if (cartProduct) {
        if (cartProduct.quantity > 1) {
          cartProduct.quantity -= 1;
          cartProduct.total = cartProduct.price * cartProduct.quantity;
          setGrandTotal((prev) => prev - cartProduct.price);
        } else {
          let newCart = cart.filter((item) => item.id !== cartProduct.id);
          setCart(newCart);
          setGrandTotal((prev) => prev - cartProduct.price);
        }
      }
    }
  };

  const HandleOrder = async () => {
    try {
        // Send a POST request to the backend API with the cart data
        let response = await fetch('http://localhost:3000/api/order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({cart}) // Stringify the cart object
        });
        
        // Parse the response from the server
        let data = await response.json();
        
        // Log the response for debugging
        console.log(data);
        
        // Reset the cart and grand total
        setCart([]);
        setGrandTotal(0);
    } catch (err) {
        // Handle any errors that occur during the request
        console.log(err);
    }
};

  return (
    <main className="w-screen">
      <div className="p-20 w-full flex flex-col gap-2 ">
        <h1 className="text-lg font-bold p-4">Products Available</h1>
        <div className="w-full grid lg:grid-col-3 md:grid-cols-1 grid-cols-1 gap-12 justify-center items-center">
          {products && products.map((product, index) => <Products key={index} product={product} button={HandleButton} />)}
        </div>
      </div>
      {cart.length > 0 &&
        <div className="w-full flex flex-col p-20 ">
          <h1 className="text-lg font-bold p-4">Cart</h1>
          <div className="w-full flex flex-col gap-12 justify-center items-center p-4">
            <div className="grid grid-cols-4 text-center w-full text-base-content font-bold">
              <div>Name</div>
              <div>Price</div>
              <div>Quantity</div>
              <div>Total Price</div>
            </div>
            {cart.map((product, index) => <CartOrder key={index} product={product} />)}
          </div>
          <div className="w-full flex flex-row justify-between p-4">
            <h1 className="text-lg font-bold">Grand Total</h1>
            <h1 className="text-lg font-bold">{grandTotal}</h1>
          </div>
          <div className="flex flex-row-reverse">
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={() => HandleOrder()}>Place Order</button>
          </div>
        </div>}
    </main>
  )
}
