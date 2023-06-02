import pika

user = 'admin'
password = 'password_123'

credentials = pika.PlainCredentials(user, password)
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='vascobank.logs', durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue='vascobank.logs', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
