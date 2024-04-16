import { NextResponse } from 'next/server';
import db from '@/lib/db';

export async function GET(req) {
  try {
    const { rows } = await db.query('SELECT DISTINCT id,total,order_date,status FROM orderdetails');
    return NextResponse.json(rows)
  }
  catch (err) {
    return NextResponse.error(err);
  }
}

