"use client";
import { useEffect,useState } from "react";
import {Order} from "@/components/Order";
export default function OrderStatus() {
  const [orderData,setOrderData] = useState([])
  useEffect(() => {
    fetch('http://localhost:3000/api/status')
        .then(response => response.json())
        .then(data => { console.log(data);setOrderData(data)})
        .catch(err=>console.log(err))
  },[])
  return (
    <main className="w-screen">
      <div className="p-20 w-full flex flex-col ">
        <h1>Order status</h1>
        <div className="w-full grid lg:grid-col-4 md:grid-cols-2 grid-cols-1 gap-12 justify-center items-center">
            {orderData && orderData.map((order,index) =><Order key={index} order={order} />)}
        </div>
      </div>
    </main>
  )
}
