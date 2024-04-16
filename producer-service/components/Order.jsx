export function Order({ order }) {
  const color =
    order.status === "Success"
      ? "bg-success"
      : order.status == "Pending"
      ? "bg-info"
      : "bg-error";
  return (
    <div className="grid grid-cols-4 w-full text-center border-b-2 p-2 rounded ">
      <div>{order.id}</div>
      <div>{order.order_date}</div>
      <div>{order.total}</div>
      <div className={`${color} w-24 p-1 rounded mx-auto font-bold `}>
        {order.status}
      </div>
    </div>
  );
}
