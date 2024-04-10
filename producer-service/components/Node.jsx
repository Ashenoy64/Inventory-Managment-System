export function Node({ node }) {
    const time = (new Date()- node.checkpoint).toString();
    return (
      <div className="grid grid-cols-3 w-full text-center border-b-2 p-2 rounded ">
        <div className="p-1">{node.id}</div>
        <div className="p-1">{node.node_name}</div>
        <div className={`p-1 ${time>"10000"?"text-error":"text-success"} `}>{time}</div>
      </div>
    );
  }
  