# Inventory Management System

The Inventory Management System is a comprehensive solution designed to streamline inventory operations, order processing, and administrative tasks. Leveraging various technologies, including RabbitMQ for communication, Next.js for the user frontend, Streamlit for the admin console, and PostgreSQL for data storage, the system offers a robust platform for managing inventory efficiently.

## Features

- **Communication System**: Utilizes RabbitMQ for seamless communication between different components of the system.
- **User Frontend**: Built with Next.js, providing users with an intuitive interface to place orders and track order status ( also displays node status :) ).
- **Admin Console**: Powered by Streamlit, offering administrators access to metrics visualization, sales tracking, restocking functionalities, item management, and comprehensive order status monitoring.
- **Data Storage**: Uses PostgreSQL to securely store inventory data, order information, and other relevant data.
- **Docker Deployment**: All services are containerized using Docker, making deployment simple and scalable with Docker Compose.

## Deployment

To deploy the Inventory Management System, follow these steps:

1. Make sure you have Docker and Docker Compose installed on your machine.

2. Run the following command to start RabbitMQ:
    ```
    docker run -d -p 5672:5672 rabbitmq
    ```

3. Run the following command to start the PostgreSQL database:
    ```
    docker run -d -p 5433:5432 database
    ```

4. Wait for a few seconds for RabbitMQ and the database to start up.

5. Navigate to the directory containing your Docker Compose file and run the following command to start all services:
    ```
    docker-compose up --build
    ```

6. Access the user frontend at `http://localhost:3000` and the admin console at `http://localhost:8501`.


## License

This project is licensed under the [MIT License](LICENSE), allowing for free use, modification, and distribution according to the terms specified.

