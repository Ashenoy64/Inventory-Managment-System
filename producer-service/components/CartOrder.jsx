export function CartOrder({ product }) {
  return (
    <div className="grid grid-cols-4 w-full text-center border-b-2 p-2 rounded ">
      <div>{product.name}</div>
      <div>{product.price}</div>
      <div>{product.quantity}</div>
      <div>{product.total}</div>
    </div>
  );
}
