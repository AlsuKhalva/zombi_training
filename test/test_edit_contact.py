import random
from model.contact import Contact


def test_edit_some_contact_name(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.form.create(Contact(first_name="VVVVVVV"))
    old_contacts_list = db.get_contacts_list()
    index = random.choice(range(len(old_contacts_list)))
    id = old_contacts_list[index].id
    user = Contact(id=id, first_name="ZUMZUM")
    app.form.edit_contact_by_id(id, user)
    new_contacts_list = db.get_contacts_list()
    assert len(old_contacts_list) == len(new_contacts_list)
    old_contacts_list[index] = user
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)
    if check_ui:
        def clean(user):
            return Contact(id=user.id, first_name=user.first_name.rstrip())
        assert sorted(list(map(clean, new_contacts_list)), key=Contact.id_or_max) == sorted(app.form.get_contacts_list(),
                                                                                  key=Contact.id_or_max)

#def test_edit_first_contact_notes(app):
 #   if app.form.count() == 0:
  #      app.form.create(Contact(first_name="VVVVVVV"))
   # old_contacts_list = app.form.get_contacts_list()
    #app.form.edit_first_contact(Contact(notes="Kroha"))
    #new_contacts_list = app.form.get_contacts_list()
    #assert len(old_contacts_list) == len(new_contacts_list)


#def test_edit_first_contact_bday(app):
 #   if app.form.count() == 0:
  #      app.form.create(Contact(first_name="VVVVVVV"))
   # old_contacts_list = app.form.get_contacts_list()
    #app.form.edit_first_contact(Contact(day="4"))
    #new_contacts_list = app.form.get_contacts_list()
    #assert len(old_contacts_list) == len(new_contacts_list)
