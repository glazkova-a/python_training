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


def test_add_group_to_contact(app, data_contacts, orm, check_ui):
    contact = data_contacts

    group_name = contact.new_group
    if group_name is None:
        contact.new_group = "aaa"
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name=group_name))

    old_contacts = orm.get_contacts_in_group(Group(id="195"))
    app.contact.create_new_contact(contact)
    new_contacts = orm.get_contacts_in_group(Group(id="195"))
    old_contacts.append(contact)

    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
