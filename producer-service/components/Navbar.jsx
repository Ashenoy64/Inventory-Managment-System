export default function Navbar() {
  return (
    <div className="flex flex-row w-full p-4 justify-between">
      <div className="p-2">Inventory Management</div>
      <div className="flex flex-row gap-4 p-2">
        <div>Health Status</div>
        <div>Order Status</div>
      </div>
    </div>
  );
}
