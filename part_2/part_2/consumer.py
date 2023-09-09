import pika
from mongoengine import connect
from models import Contact

# Підключення до MongoDB
uri = "mongodb+srv://zhowtenkooleksiy:OdqjdrrgrJDD64qf@db-hw2-08.u8lqztr.mongodb.net/?retryWrites=true&w=majority"

connect(
    db="hw2_08_2db",
    host=uri,
)

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="contact_queue")

# Обробка повідомлень з черги


def send_email(email):
    # Реалізуйте логіку відправки електронної пошти тут
    print(f"Sending email to {email}")


# Функція-зворотний виклик для обробки повідомлень з черги


def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects.get(id=contact_id)
    send_email(contact.email)
    contact.is_message_sent = True
    contact.save()
    print(f"Email sent for contact: {contact.full_name}")


# Підписка на чергу і обробка повідомлень
channel.basic_consume(
    queue="contact_queue", on_message_callback=callback, auto_ack=True
)

print("Waiting for messages...")
channel.start_consuming()
