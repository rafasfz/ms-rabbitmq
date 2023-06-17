import pika
import json

user = 'admin'
password = 'password@vascobank123'

credentials = pika.PlainCredentials(user, password)
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

def send_logs(logs):
    message = json.dumps(logs)
    channel.basic_publish(exchange='', routing_key='vascobank.logs', body=message)
    print(" [x] Sent %r" % message)

send_logs(
    {
        "timestamp": "31.01.2021 21.03:48.357",
        "level": "INFO",
        "thread": "main",
        "logger": "com.alexgutjahr.jasonlog.JsonLogApplicationKt",
        "message": "Starting JsonLogApplicationKt using Java 15.0.1 on vortex.fritz.box wit",
        "context": "default"
    }
)