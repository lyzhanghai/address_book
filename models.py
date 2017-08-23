from peewee import *

db = SqliteDatabase('db/address_book.db')


class BaseModel(Model):
    class Meta:
        database = db


class Group(BaseModel):
    """
    This class represents a group in our address book.
    """
    name = CharField()

    @classmethod
    def add_group(cls, name):
        g, _ = cls.get_or_create(name=name)
        return g


class Person(BaseModel):
    """
    This class represents a person in our address book.
    """
    first_name = CharField()
    last_name = CharField()
    full_name = CharField(index=True)

    @classmethod
    def add_person(cls, **kwargs):
        fname = kwargs.get('first_name')
        lname = kwargs.get('last_name')
        full_name = fname + ' ' + lname
        p, _ = cls.get_or_create(first_name=fname, last_name=lname, full_name=full_name)

        emails = kwargs.get('email')
        streets = kwargs.get('street')
        phones = kwargs.get('phone')

        for email in emails:
            Email.create(email=email, email_user=p)

        for street in streets:
            Street.create(address=street, lived_person=p)

        for phone in phones:
            Phone.create(phone_no=phone, phone_user=p)

        return p


class Street(BaseModel):
    address = CharField()
    lived_person = ForeignKeyField(Person, related_name='streets')


class Phone(BaseModel):
    phone_no = CharField()
    phone_user = ForeignKeyField(Person, related_name='phones')


class Email(BaseModel):
    email = CharField()
    email_user = ForeignKeyField(Person, related_name='emails')


class AddressBook(BaseModel):
    """
    This class represents an address book
    """
    person = ForeignKeyField(Person)
    group = ForeignKeyField(Group)

    @classmethod
    def find_all_person_by_name(cls, q):
        """
        Find people searched by name
        :param q: string
        :return: list
        """
        query = cls.select().join(Person).where(
            (Person.full_name.contains(q))
        )

        people = list()
        for p in query:
            people.append(p.person)
        return people

    @classmethod
    def find_all_person_by_email(cls, q):
        """
        Find people searched by email
        :param q: string
        :return: list
        """
        query = cls.select().join(Person).join(Email, on=Email.email_user).where(Email.email.contains(q))

        people = list()
        for p in query:
            people.append(p.person)
        return people

    @classmethod
    def find_people_by_group(cls, group):
        query = cls.select().join(Person).where(cls.group == group)

        people = list()
        for p in query:
            people.append(p.person)
        return people

    @classmethod
    def find_groups_by_person(cls, person):
        query = cls.select().join(Group).where(cls.person == person)

        groups = list()
        for g in query:
            groups.append(g.group)
        return groups


def create_tables():
    db.connect()
    try:
        db.create_tables([Group, Person, Street, Phone, Email, AddressBook])
    except Exception as e:
        pass
