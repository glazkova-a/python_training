# -*- coding: utf-8 -*-

from model.contact_model import Contact

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
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)




def test_add_group_to_contact(app, data_contacts, db, check_ui):
    contact = data_contacts
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    old_contacts = db.get_contacts_in_group()
    app.contact.create_new_contact(contact)
    new_contacts = db.get_contacts_in_group()
    old_contacts.append(contact)
    assert len(old_contacts)-1 == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list, key=Contact.id_or_max)












