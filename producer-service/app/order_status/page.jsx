"use client";
import { useEffect, useState } from "react";
import { Order } from "@/components/Order";
export default function OrderStatus() {
  const [orderData, setOrderData] = useState([]);
  useEffect(() => {
    fetch("http://localhost:3000/api/status")
      .then((response) => response.json())
      .then((data) => {
        for (let i = 0; i < data.length; i++) {
          const orderDate = new Date(data[i].order_date);

          // Convert to a readable format
          const readableDate = orderDate.toLocaleString("en-US", {
            year: "numeric",
            month: "long",
            day: "numeric",
            hour: "2-digit",
            minute: "2-digit",
            hour12: true, // Add AM/PM
          });

          // Update the order_date property with the readable format
          data[i].order_date = readableDate;
        }

        setOrderData(data);
      })
      .catch((err) => console.log(err));
  }, []);
  return (
    <main className="w-screen">
      <div className="p-20 w-full flex flex-col ">
        <h1 className="text-lg font-bold p-4">Order status</h1>
        <div className="w-full flex flex-col gap-12 justify-center items-center">
          <div className="grid grid-cols-4 text-center w-full text-base-content font-bold">
            <div>Order ID</div>
            <div>Order Date</div>
            <div>Price ₹</div>
            <div>Status</div>
          </div>
          {orderData &&
            orderData.map((order, index) => (
              <Order key={index} order={order} />
            ))}
        </div>
      </div>
    </main>
  );
}
