import './globals.css'
import Navbar from "@/components/Navbar";

export const metadata = {
  title: 'Inventory Management System',
  description: 'Inventory Management System for the Producer Service',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en" className='no-scrollbar h-screen bg-black'>
      <body className="w-full h-full"><Navbar />{children}</body>
    </html>
  )
}
