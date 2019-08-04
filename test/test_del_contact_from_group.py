from model.contact import Contact
from model.hw_group import Group
from fixture.orm import ORMFixture
import random


db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")


def test_del_contact_from_group(app, db, orm):
    if len(app.form.get_contacts_list()) == 0:
        app.form.create(Contact(first_name="ZUMZUM"))
    if len(app.group.get_group_list()) == 0:
        app.group.create(Group(name="BBB", header="BBB", footer="BBB"))
    if len(db.get_groups_with_contacts()) == 0:
        contact_id = random.choice(db.get_contacts_list()).id
        group_id = random.choice(db.get_group_list()).id
        app.form.add_contact_to_group(contact_id, group_id)
    group_id = random.choice(db.get_groups_with_contacts()).id
    contact_id = random.choice(orm.get_contacts_in_group(Group(id=group_id))).id
    app.form.delete_contact_from_group(group_id)
    assert db.get_contact_by_id(contact_id) not in orm.get_contacts_in_group(Group(id=group_id))