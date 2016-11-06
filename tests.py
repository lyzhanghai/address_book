import unittest
from models import *


class TestAddressBook(unittest.TestCase):

    def setUp(self):
        create_tables()

        p = {
            'first_name': 'Ahsan', 'last_name': 'Khan',
            'email': ['ahsan@gmail.com', 'ahsankhan@example.com'],
            'street': ['Street-1', 'Stree-2'],
            'phone': ['+880191142']
        }
        self.p1 = Person.add_person(**p)

        p = {
            'first_name': 'Sirajul', 'last_name': 'Islam',
            'email': ['sirajul@hotmail.com', 'siraj@live.com'],
            'street': ['Street-1', 'Stree-2'],
            'phone': ['+880171142']
        }
        p2 = Person.add_person(**p)

        self.g1 = Group.add_group(name='Group1')
        self.g2 = Group.add_group(name='Group2')

        AddressBook.create(group=self.g1, person=self.p1)
        AddressBook.create(group=self.g2, person=p2)

    def test_add_person(self):
        pson = {
            'first_name': 'New', 'last_name': 'Person',
            'email': ['new_p@yahoo.com'],
            'street': ['Street-1', 'Stree-2'],
            'phone': ['+880151142']
        }
        p = Person.add_person(**pson)
        ab = AddressBook.create(person=p, group=self.g1)

        self.assertEqual(p, ab.person)

    def test_add_group(self):
        g = Group.add_group(name="New Group")
        ab = AddressBook.create(person=self.p1, group=g)

        self.assertEqual(g, ab.group)

    def test_find_person_by_name(self):
        fname = "Ahsan"
        lname = "Person"
        people = AddressBook.find_all_person_by_name(fname)
        self.assertIn(self.p1, people)
        people = AddressBook.find_all_person_by_name(lname)
        try:
            p = Person.get(Person.last_name == lname)
            self.assertIn(p, people)
        except Person.DoesNotExist:
            pass

    def test_find_person_by_email(self):
        p = AddressBook.find_all_person_by_email("new_p@yahoo.com")[0]
        self.assertEqual(p.first_name, "New")
        p = AddressBook.find_all_person_by_email("hotmail")[0]
        self.assertEqual(p.first_name, "Sirajul")

    def test_find_people_by_group(self):
        members = AddressBook.find_people_by_group(self.g2)
        p = Person.get(Person.first_name == 'Sirajul')
        self.assertEqual(p, members[0])

    def test_list_person_groups(self):
        groups = AddressBook.find_groups_by_person(self.p1)
        g = Group.get(Group.name == 'Group1')
        self.assertEqual(g, groups[0])

    def tearDown(self):
        db.close()


if __name__=='__main__':
    unittest.main()
