from model.contact_model import Contact
from random import randrange
import re




def test_assert_random_contact(app):
    if app.contact.count_contact_entries() == 0:
        app.contact.create_new_contact(Contact(name="Assert", surname="Me", address="169, Green St", email="assert@gmail.com",
                                               email2="assert_me@gmail.com", email3="assert_itself@gmail.com", home_phone="0987654",
                                               mobile_phone="56565656", work_phone="345676543", secondary_phone="+1234567890"))

    list_contact_from_home_page = app.contact.get_contact_list()
    index = randrange(len(list_contact_from_home_page))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.id == contact_from_edit_page.id
    assert contact_from_home_page.surname == contact_from_edit_page.surname
    assert contact_from_home_page.name == contact_from_edit_page.name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phones(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                        contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))


def clear_phones(s):
    return re.sub('[() -]', "", s)





def test_assert_all_contacts(app, db):
    if app.contact.count_contact_entries() == 0:
        app.contact.create_new_contact(Contact(name="Assert", surname="Me", address="169, Green St", email="assert@gmail.com",
                                               email2="assert_me@gmail.com", email3="assert_itself@gmail.com", home_phone="0987654",
                                               mobile_phone="56565656", work_phone="345676543", secondary_phone="+1234567890"))
        contact_from_home_page = app.contact.get_contact_list()
        contact_from_db = db.get_contact_list()
        assert contact_from_home_page.id == contact_from_db.id
        assert contact_from_home_page.surname == contact_from_db.surname
        assert contact_from_home_page.name == contact_from_db.name
        assert contact_from_home_page.address == contact_from_db.address
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_db)


