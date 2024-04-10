import Link from "next/link";

export default function Navbar() {
  return (
    <div className="flex flex-row w-full p-4 justify-between">
      <div className="p-2"><Link href="/">Inventory Management</Link></div>
      <div className="flex flex-row gap-4 p-2">
        <Link href='/health'><div>Health Status</div></Link>
        <Link href='/order_status'><div>Order Status</div></Link>
      </div>
    </div>
  );
}
