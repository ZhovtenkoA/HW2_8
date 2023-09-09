import pika
from faker import Faker
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

# Генерування фейкових контактів
fake = Faker()
num_contacts = 10

contacts = []
for _ in range(num_contacts):
    contact = Contact(full_name=fake.name(), email=fake.email(), is_message_sent=False)
    contact.save()
    contacts.append(contact)

    contact_id = str(contact.id)

    # Публікація ObjectID у чергу RabbitMQ
    channel.basic_publish(exchange="", routing_key="contact_queue", body=contact_id)

    print(f"Contact created: {contact_id}")

# Відправка повідомлення для кожного контакту
for contact in contacts:
    message = str(contact.id)
    channel.basic_publish(exchange="", routing_key="email_queue", body=message)
    print(f"Message sent for contact: {contact.full_name}")

connection.close()
