// pages/api/order.js
import { NextResponse } from 'next/server';
var amqp = require('amqplib');



export async function POST(req) {
    const body = await req.json();
    let connection, channel;
    try {
        connection = await amqp.connect("amqp://" + process.env.RABBITMQ_HOST + ":" + process.env.RABBITMQ_PORT);
        channel = await connection.createChannel()
        await channel.assertQueue(process.env.RABBITMQ_QUEUE_VALIDATION, { durable: false });
    }
    catch (err) {
        console.error('Error connecting to RabbitMQ:', err);
        return NextResponse.error({ message: 'An error occurred while connecting to RabbitMQ.' });
    }
    try {

        await channel.sendToQueue(process.env.RABBITMQ_QUEUE_VALIDATION, Buffer.from(JSON.stringify(body)));
        await channel.close();
        await connection.close();
        return NextResponse.json({ message: 'JSON data received successfully.' });
    } catch (err) {
        console.error('Error processing JSON data:', err); // Log the error for debugging
        return NextResponse.error({ message: 'An error occurred while processing the JSON data.' });
    }
}
