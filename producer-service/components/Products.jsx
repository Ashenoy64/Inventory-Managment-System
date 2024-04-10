export function Products({ product, button }) {
  return (
    <div className="card w-96 outline outline-1 mx-auto ">
      <div className="card-body">
        <h2 className="card-title">{product.name}</h2>
        <p>₹{product.price}</p>
        <div className="card-actions justify-end">
          <button
            className="btn w-12 font-bold text-xl "
            onClick={() => button("remove", product)}
          >
            -
          </button>
          <button
            className="btn w-12 font-bold text-xl "
            onClick={() => button("add", product)}
          >
            +
          </button>
        </div>
      </div>
    </div>
  );
}
