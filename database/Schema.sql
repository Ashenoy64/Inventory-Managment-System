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


-- Node will already be having the details in built 
-- Update or insert Node Details