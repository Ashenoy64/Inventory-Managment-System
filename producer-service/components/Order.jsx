export function Order({ order }) {
    return (
      <div className="flex flex-row justify-evenly w-full">
        <div>{order.id}</div>
        <div>{order.order_date}</div>
        <div>{order.status}</div>
      </div>
    );
  }
  