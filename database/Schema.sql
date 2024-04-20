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
CREATE TABLE PendingItems(
    id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES OrderDetails (id),
    FOREIGN KEY (product_id) REFERENCES Products (id),
    UNIQUE(id,order_id,product_id)
);


CREATE TABLE DATA_REPORT(
    invested DECIMAL(10, 2) DEFAULT 1000.00,
    revenue DECIMAL(10, 2) DEFAULT 0.00
);   


-- Starting products
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
INSERT INTO Products (name, price, quantity) VALUES ('Quince', 90, 0);
INSERT INTO Products (name, price, quantity) VALUES ('Raspberry', 95, 0);

-- Starting Orders
INSERT INTO OrderDetails (id,order_date, total, status) VALUES (1,'2021-01-01', 1475.00, 'Success');
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (1, 1, 10);
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (1, 2, 20);
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (1, 3, 5);

INSERT INTO OrderDetails (id,order_date, total, status) VALUES (2,'2021-01-01', 1250.00, 'Success');
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (2, 4, 50);
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (2, 5, 30);

INSERT INTO OrderDetails (id,order_date, total, status) VALUES (3,'2021-01-01', 1800.00, 'Success');
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (3, 6, 40);
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (3, 7, 60);

INSERT INTO OrderDetails (id,order_date, total, status) VALUES (4,'2021-01-02', 280.00, 'Success');
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (4, 8, 15);


INSERT INTO OrderDetails (id,order_date, total, status) VALUES (5,'2021-01-03', 405.00, 'Success');
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (5, 9, 25);

INSERT INTO OrderDetails (id,order_date, total, status) VALUES (6,'2021-01-03', 550.00, 'Success');
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (6, 10, 35);

INSERT INTO OrderDetails (id,order_date, total, status) VALUES (7,'2021-01-03', 484.00, 'Failed');
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (7, 11, 45);

INSERT INTO OrderDetails (id,order_date, total, status) VALUES (8,'2021-01-04', 780.00, 'Success');
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (8, 12, 55);

INSERT INTO OrderDetails (id,order_date, total, status) VALUES (9,'2021-01-05', 910.00, 'Success');
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (9, 13, 65);

INSERT INTO OrderDetails (id,order_date, total, status) VALUES (10,'2021-01-06', 420.00, 'Failed');
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (10, 14, 75);

INSERT INTO OrderDetails (id,order_date, total, status) VALUES (11,'2021-01-06', 450.00, 'Success');
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (11, 15, 85);

INSERT INTO OrderDetails (id,order_date, total, status) VALUES (12,'2021-01-07', 1280.00, 'Success');
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (12, 16, 95);

INSERT INTO OrderDetails (id,order_date, total, status) VALUES (13,'2021-01-09', 1615.00, 'Failed');
INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (13, 17, 105);


INSERT INTO DATA_REPORT (invested, revenue) VALUES (79791.67, 9180.00);






















