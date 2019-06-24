from model.contact import Contact


def test_edit_first_contact_name(app):
    if app.form.count() == 0:
        app.form.create(Contact(first_name="VVVVVVV"))
    app.form.edit_first_contact(Contact(first_name="ZUMZUM"))


def test_edit_first_contact_notes(app):
    if app.form.count() == 0:
        app.form.create(Contact(first_name="VVVVVVV"))
    app.form.edit_first_contact(Contact(notes="Kroha"))


def test_edit_first_contact_bday(app):
    if app.form.count() == 0:
        app.form.create(Contact(first_name="VVVVVVV"))
    app.form.edit_first_contact(Contact(day="4"))
