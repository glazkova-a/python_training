from model.contact_model import Contact


def test_edit_first_contact(app):

    if app.contact.count_contact_entries() == 0:
        app.contact.create_new_contact(Contact(name="Edit_me", surname=""))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="John", surname="Doe")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
