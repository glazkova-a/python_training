# -*- coding: utf-8 -*-

from model.contact_model import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*7
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_phones(prefix, maxlen):
    symbols = string.digits + " "*2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_emails(prefix, maxlen):
    symbols = string.ascii_letters + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(name="", surname="")] + [
    Contact(name=random_string("name", 12), middlen=random_string("", 3), surname=random_string("lastname", 15),
            address=random_string("Address", 5), email=random_string_emails("", 9), home_phone=random_string_phones("", 10))
    for i in range(7)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)











