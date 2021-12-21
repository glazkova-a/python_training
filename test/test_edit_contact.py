from model.contact_model import Contact
from random import randrange

def test_edit_some_contact(app, db, check_ui):

    if app.contact.count_contact_entries() == 0:
        app.contact.create_new_contact(Contact(name="Edit_me", surname=""))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(name="John", surname="Doe")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list, key=Contact.id_or_max)

