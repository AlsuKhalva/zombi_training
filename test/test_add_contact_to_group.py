from model.contact import Contact
from model.hw_group import Group
from fixture.orm import ORMFixture
import random


db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if len(db.get_contacts_list()) == 0:
        app.form.create(
            Contact(first_name="ZUMZUM"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="ZZZ", header="CCC", footer="PPP"))
    contact_list = db.get_contacts_list()
    contact_id = random.choice(contact_list).id
    group_list = db.get_group_list()
    group_id = random.choice(group_list).id
    app.form.add_contact_to_group(contact_id, group_id)