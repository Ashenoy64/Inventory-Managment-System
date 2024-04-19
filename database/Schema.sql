-- Create the Products table
CREATE TABLE Products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
);

-- Create the Node Details table
CREATE TABLE NodeDetails (
    id SERIAL PRIMARY KEY,
    node_name VARCHAR(255) NOT NULL,
    checkpoint timestamp,
    UNIQUE(id,node_name)
);

-- Create the Order table
CREATE TABLE OrderDetails (
    id SERIAL PRIMARY KEY,
    order_date DATE NOT NULL,
    total DECIMAL(10, 2) DEFAULT 0.00,
    status VARCHAR(255) NOT NULL,

);

-- Order Items Table
CREATE TABLE OrderItems(
    id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES OrderDetails (id),
    FOREIGN KEY (product_id) REFERENCES Products (id),
    UNIQUE(id,order_id,product_id)
);

-- Report Table
CREATE TABLE PendingItems(){
    id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES OrderDetails (id),
    FOREIGN KEY (product_id) REFERENCES Products (id),
    UNIQUE(id,order_id,product_id)
};


CREATE TABLE DATA_REPORT{
    invested DECIMAL(10, 2) DEFAULT 1000.00,
    revenue DECIMAL(10, 2) DEFAULT 0.00
}   


-- Staring products
INSERT INTO Products (name, price, quantity) VALUES ('Apple', 50, 100);
INSERT INTO Products (name, price, quantity) VALUES ('Banana', 30, 200);
INSERT INTO Products (name, price, quantity) VALUES ('Cherry', 75, 50);
INSERT INTO Products (name, price, quantity) VALUES ('Date', 10, 500);
INSERT INTO Products (name, price, quantity) VALUES ('Elderberry', 25, 300);
INSERT INTO Products (name, price, quantity) VALUES ('Fig', 15, 400);
INSERT INTO Products (name, price, quantity) VALUES ('Grape', 20, 600);
INSERT INTO Products (name, price, quantity) VALUES ('Honeydew', 35, 150);
INSERT INTO Products (name, price, quantity) VALUES ('Jackfruit', 45, 75);
INSERT INTO Products (name, price, quantity) VALUES ('Kiwi', 55, 125);
INSERT INTO Products (name, price, quantity) VALUES ('Lemon', 40, 250);
INSERT INTO Products (name, price, quantity) VALUES ('Mango', 65, 100);
INSERT INTO Products (name, price, quantity) VALUES ('Nectarine', 70, 50);
INSERT INTO Products (name, price, quantity) VALUES ('Orange', 30, 300);
INSERT INTO Products (name, price, quantity) VALUES ('Papaya', 80, 75);
INSERT INTO Products (name, price, quantity) VALUES ('Quince', 90, 25);
INSERT INTO Products (name, price, quantity) VALUES ('Raspberry', 95, 150);