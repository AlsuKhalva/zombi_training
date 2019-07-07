from model.contact import Contact
from random import randrange


def test_edit_some_contact_name(app):
    if app.form.count() == 0:
        app.form.create(Contact(first_name="VVVVVVV"))
    old_contacts_list = app.form.get_contacts_list()
    index = randrange(len(old_contacts_list))
    user = Contact(first_name="ZUMZUM")
    user.id = old_contacts_list[index].id
    app.form.edit_contact_by_index(index, user)
    new_contacts_list = app.form.get_contacts_list()
    assert len(old_contacts_list) == len(new_contacts_list)
    old_contacts_list[index] = user
    assert sorted(old_contacts_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)


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
