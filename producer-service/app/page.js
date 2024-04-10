"use client";
import { useEffect,useState } from "react";
import { Products } from "@/components/Products";

export default function Home() {
  const [products,setProducts] = useState([])
  useEffect(() => {
    fetch('http://localhost:3000/api/products')
      .then(response => response.json())
      .then(data => { setProducts(data)})
  }, [])
  return (
    <main className="w-screen">
      <div className="p-20 w-full flex flex-col gap-2 ">
        <h1 className="text-lg font-bold p-4">Products Available</h1>
        <div className="w-full grid lg:grid-col-4 md:grid-cols-2 grid-cols-1 gap-12 justify-center items-center">
          {products && products.map((product,index) => <Products key={index} product={product} /> ) }
        </div>
      </div>
    </main>
  )
}
