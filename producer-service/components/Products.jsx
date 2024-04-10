export function Products({ product }) {
  return (
    <div className="card w-96 bg-base-100 shadow-xl">
      <div className="card-body">
        <h2 className="card-title">{product.name}</h2>
        <p>{product.price}</p>
        <div className="card-actions justify-end">
          <button className="btn btn-primary">-</button>
          <button className="btn btn-primary">+</button>
        </div>
      </div>
    </div>
  );
}
