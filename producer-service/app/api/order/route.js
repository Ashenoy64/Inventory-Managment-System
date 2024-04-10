import { NextResponse } from 'next/server';

export async function POST(req) {
    const { body } = req;
    try {
        console.log(body)
        return NextResponse.json({ message: 'Order has been placed' });
    }
    catch (err) {
        return NextResponse.error(err);
    }
}

