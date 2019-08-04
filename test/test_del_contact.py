import random
from model.contact import Contact


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.form.create(Contact(first_name="VVVVVVV"))
    old_contacts_list = db.get_contacts_list()
    user = random.choice(old_contacts_list)
    app.form.delete_contact_by_id(user.id)
    new_contacts_list = db.get_contacts_list()
    assert len(old_contacts_list) - 1 == len(new_contacts_list)
    old_contacts_list.remove(user)
    assert old_contacts_list == new_contacts_list
    if check_ui:
        def clean(user):
            return Contact(id=user.id, first_name=user.first_name.rstrip())
        assert sorted(list(map(clean, new_contacts_list)), key=Contact.id_or_max) == sorted(app.form.get_contacts_list(),
            key=Contact.id_or_max)

#def test_delete_first_contact(app):
 #   if app.form.count() == 0:
 #       app.form.create(Contact(first_name="VVVVVVV"))
 #   old_contacts_list = app.form.get_contacts_list()
 #   app.form.delete_first_contact()
 #   new_contacts_list = app.form.get_contacts_list()
 #   assert len(old_contacts_list) - 1 == len(new_contacts_list)
 #   old_contacts_list[0:1] = []
 #   assert old_contacts_list == new_contacts_list

