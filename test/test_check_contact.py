import re


def test_all_fields_on_home_page(app, db):
    if len(db.get_contacts_list()) == 0:
        app.form.create(Contact(first_name="VVVVVVV"))
    list = app.form.get_contacts_list()
    for user in list:
        assert contact_from_home_page.first_name == db.get_all_contact_list(user.id).first_name
        assert contact_from_home_page.last_name == db.get_all_contact_list(user.id).last_name
        assert contact_from_home_page.address == db.get_all_contact_list(user.id).address
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(db.get_all_contact_list(user.id))
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(db.get_all_contact_list(user.id))


#def test_phones_on_contact_view_page(app):
#    contact_from_view_page = app.form.get_contact_from_view_page(0)
#    contact_from_edit_page = app.form.get_contact_info_from_edit_page(0)
#    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))