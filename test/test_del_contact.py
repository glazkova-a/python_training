from model.contact_model import Contact


def test_del_first_contact(app):

    if app.contact.count_contact_entries() == 0:
        app.contact.create_new_contact(Contact(name="Delete_me"))
    old_contacts = app.contact.get_contact_list()
    app.contact.del_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []


