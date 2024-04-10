"use client";
import { useEffect, useState } from "react";
import { Node } from "@/components/Node";

export default function Health() {
  const [nodeData, setNodeData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:3000/api/health")
      .then((response) => response.json())
      .then((data) => {
        for (let i = 0; i < data.length; i++) {
          data[i].checkpoint = new Date(data[i].checkpoint);
        }
        data.sort((a, b) => b.checkpoint - a.checkpoint);
        setNodeData(data);
      })
      .catch((err) => console.log(err));
  }, []);
  return (
    <main className="w-screen">
      <div className="p-20 w-full flex flex-col ">
        <h1 className="text-lg font-bold p-4">Node Health</h1>
        <div className="w-full flex flex-col gap-12 justify-center items-center">
          <div className="grid grid-cols-3 text-center w-full text-base-content font-bold">
            <div>Node ID</div>
            <div>Node Name</div>
            <div>Last HeartBeat (Sec)</div>
          </div>
          {nodeData &&
            nodeData.map((node, index) => <Node key={index} node={node} />)}
        </div>
      </div>
    </main>
  );
}
