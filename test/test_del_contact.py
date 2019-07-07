from model.contact import Contact


def test_delete_first_contact(app):
    if app.form.count() == 0:
        app.form.create(Contact(first_name="VVVVVVV"))
    old_contacts_list = app.form.get_contacts_list()
    app.form.delete_first_contact()
    new_contacts_list = app.form.get_contacts_list()
    assert len(old_contacts_list) - 1 == len(new_contacts_list)
    old_contacts_list[0:1] = []
    assert old_contacts_list == new_contacts_list

