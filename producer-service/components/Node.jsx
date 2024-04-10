export function Node({ node }) {
    return (
      <div className="flex flex-row justify-evenly w-full">
        <div>{node.id}</div>
        <div>{node.node_name}</div>
        <div>{node.checkpoint}</div>
      </div>
    );
  }
  