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
    order_date DATE NOT NULL,
    status VARCHAR(255) NOT NULL,
);

-- Order Items Table
CREATE TABLE OrderItems(
    id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES OrderDetails (id),
    FOREIGN KEY (product_id) REFERENCES Products (id)
);


-- Node will already be having the details in built 
-- Update or insert Node Details
INSERT INTO NodeDetails (id,node_name, checkpoint) VALUES ('Node1', '2021-01-01 00:00:00');