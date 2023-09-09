from mongoengine import connect
from models import *
from json_load import *

uri = "mongodb+srv://zhowtenkooleksiy:OdqjdrrgrJDD64qf@db-hw2-08.u8lqztr.mongodb.net/?retryWrites=true&w=majority"

connect(
    db="hw2_08_1db",
    host=uri,
)

autors = "D:\\HW2_8\\part_1\\part_1\\authors.json"
quotes = "D:\\HW2_8\\part_1\\part_1\\quotes.json"

try:
    load_authors_from_json(autors)
    load_quotes_from_json(quotes)
    print("Вы успешно подключились к MongoDB и загрузили авторов и их цитаты")
except Exception as e:
    print(e)
