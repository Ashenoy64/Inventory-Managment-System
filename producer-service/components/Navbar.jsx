import Link from "next/link";

export default function Navbar() {
  return (
    <div className="flex flex-row w-full p-4 justify-between border-b-2">
      <div className="p-2 text-xl font-bold">
        <Link href="/">Inventory Management</Link>
      </div>
      <div className="flex flex-row gap-4 items-center">
        <Link href="/health">
          <div className="text-lg font-semibold hover:border-b-2 p-1">
            Health Status
          </div>
        </Link>
        <Link href="/order_status">
          <div className="text-lg font-semibold hover:border-b-2 p-1">
            Order Status
          </div>
        </Link>
      </div>
    </div>
  );
}
