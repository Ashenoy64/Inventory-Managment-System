"use client";
import { useEffect,useState } from "react";
import {Node} from "@/components/Node";

export default function Health() {
    const [nodeData,setNodeData] = useState([])

    useEffect(() => {
        fetch('http://localhost:3000/api/health')
            .then(response => response.json())
            .then(data => { console.log(data);setNodeData(data)})
            .catch(err=>console.log(err))
    },[])
  return (
    <main className="w-screen">
      <div className="p-20 w-full flex flex-col ">
        <h1>Node Health</h1>
        <div className="w-full flex flex-col gap-12 justify-center items-center">
            {nodeData && nodeData.map((node,index) =><Node key={index} node={node} />)}
        </div>
      </div>
    </main>
  )
}
