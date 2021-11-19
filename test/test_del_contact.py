from model.contact_model import Contact


def test_del_first_contact(app):

    app.open_home_page()
    if app.contact.count_contact_entries() == 0:
        app.contact.create_new_contact(Contact(name="test"))
    app.contact.del_first_contact()

