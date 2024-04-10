import { NextResponse } from 'next/server';
import db from '@/lib/db';

export async function GET(req) {
  try {
    const { rows } = await db.query('SELECT * FROM products');
    return NextResponse.json(rows)
  }
  catch (err) {
    return NextResponse.error(err);
  }
}

