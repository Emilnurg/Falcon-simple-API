from peewee import *
import uuid, random, string

psql_db = PostgresqlDatabase(
    'orgdb',
    user='orguser',
    password='12345',
    host='127.0.0.1'
)


class BaseModel(Model):
    class Meta:
        database = psql_db


class OrgUser(BaseModel):
    username = CharField(unique=True)


def init_tables():
    psql_db.create_tables([OrgUser], safe=True)


def delete_tables():
    psql_db.drop_tables([OrgUser])


def generate_users(num_users):
    letters = string.ascii_lowercase
    for i in range(num_users):
        user_name = ''.join(random.choice(letters) for i in range(10))
        OrgUser(username=user_name).save()
