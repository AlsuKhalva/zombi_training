from model.contact import Contact


def test_edit_first_contact_name(app):
    if app.form.count() == 0:
        app.form.create(Contact(first_name="VVVVVVV"))
    old_contacts_list = app.form.get_contacts_list()
    user = Contact(first_name="ZUMZUM")
    user.id = old_contacts_list[0].id
    app.form.edit_first_contact(user)
    new_contacts_list = app.form.get_contacts_list()
    assert len(old_contacts_list) == len(new_contacts_list)
    old_contacts_list[0] = user
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
