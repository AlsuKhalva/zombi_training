from fixture.orm import ORMFixture
from model.hw_group import Group
from model.contact import Contact

db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")


try:
    l = db.get_contacts_not_in_group(Group(id='40'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass