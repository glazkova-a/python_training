# -*- coding: utf-8 -*-

from model.contact_model import Contact
from model.group import Group
import pytest
import random
import string






#@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create_new_contact(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list, key=Contact.id_or_max)


def test_add_contact_to_group(app, db, data_contacts, orm):
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

    # from home page choose random contact and add to the first group
    contact_list = db.get_contact_list()
    random_contact = random.choice(contact_list)
    app.contact.select_contact_by_id(random_contact.id)
    app.contact.select_add_to_group_by_id(group.id)

    new_contacts = orm.get_contacts_in_group(Group(id=group.id))

    # assert
    old_contacts.append(random_contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
