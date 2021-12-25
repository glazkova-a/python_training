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


def test_add_group_to_contact(app, db, data_contacts, orm, check_ui):
    old_groups = orm.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="aaa"))

    # make sure you have at least 1 contact
    if app.contact.count_contact_entries() == 0:
        app.contact.create_new_contact(data_contacts)

    # from home page choose random contact
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    app.contact.select_contact_by_id(random_contact.id)
    # choose option 1 in group drop down menu and click add to

    random_group = random.choice(old_groups)
    app.contact.select_add_to_group_by_id(random_group.id)
    app.contact.select_group_from_dropdown_by_id(random_group.id)
    # from db chose a contact from known id and find a group
    #orm.get_contacts_in_group(random_contact.id)
    # get contacts in group from db
    app.contact.get_group_list_with_contacts()

    # select group option 3 from drop down menu right top corner

    # read contacts from current page

    # assert


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
