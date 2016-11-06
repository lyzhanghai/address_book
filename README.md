# Ginger Address Book
This is a simple address book.

## Prerequisite
- Python 3
- SQLite3
- Peewee [Installation command `pip3 install peewee`]

## Design questions
* Q: Find person by email address (can supply any substring, ie. "comp" should
  work assuming "alexander@company.com" is an email address in the address
  book) - discuss how you would implement this without coding the solution.
* A: To implement this we could simply use some library that indexes items and offers full-text search. If we 
  use 'in' to look 'substr' into a string, then this solution might become too expensive.
  
## API Documentation

### Person.add_person
This method adds a person to the person table and returns person object.
This object later use to create an address book instance because address book is only a relation between Person and Group.

### Group.add_group
This method adds a group to the group table and returns group object.
This object later use to create an address book instance because address book is only a relation between Person and Group.

### AddressBook.find_people_by_group
This method returns a list of members of a given group. Specify an instance of a Group object as the argument to the method.

### AddressBook.find_groups_by_person
This method returns a list of groups a given person belongs to. Specify 
an instance of a Person object as the argument to the method.

### AddressBook.find_all_person_by_name
This method returns a list of people that match the given keyword with both the names. 
We make another field named full_name by concatenating both first_name and last_name. We match the full name of the people in our address book.

### AddressBook.find_all_person_by_email
This method returns a list of people whose emails match the given keyword.
A keyword can be the whole email or just a prefix and we'll still match it.
