from model.contact_model import Contact
import random
from model.group import Group


def test_del_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(name="Delete_me"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.del_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list, key=Contact.id_or_max)


def test_del_contact_from_group(app, db, data_contacts, orm):
    # make sure you have at least 1 group
    group_list = orm.get_group_list()
    if len(group_list) == 0:
        app.group.create(Group(name="aaa"))

    # make sure you have at least 1 contact
    if app.contact.count_contact_entries() == 0:
        app.contact.create_new_contact(data_contacts)

    # get initial contacts from the first group
    group = group_list[0]
    old_contacts = orm.get_contacts_in_group(Group(id=group.id))

    # from home page choose the first group to see contacts in it
    app.contact.select_group_by_id(group.id)

    # select random contact and remove it from the group
    random_contact = random.choice(old_contacts)
    app.contact.select_contact_by_id(random_contact.id)
    app.contact.del_from_group()

    new_contacts = orm.get_contacts_in_group(Group(id=group.id))

    # assert
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)


