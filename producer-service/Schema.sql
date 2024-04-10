-- Create the Products table
CREATE TABLE Products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL
);

-- Create the Node Details table
CREATE TABLE NodeDetails (
    id SERIAL PRIMARY KEY,
    node_name VARCHAR(255) NOT NULL,
    checkpoint timestamp
);

-- Create the Order table
CREATE TABLE OrderDetails (
    id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    order_date DATE NOT NULL,
    status VARCHAR(255) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products (id)
);

INSERT INTO Products (name, price, quantity) VALUES ('Product A', 10.99, 100), ('Product B', 15.99, 50), ('Product C', 5.99, 200);