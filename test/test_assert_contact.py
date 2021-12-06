from model.contact_model import Contact
from random import randrange


def assert_random_contact(app):
    if app.contact.count_contact_entries() == 0:
        app.contact.create_new_contact(Contact(name="Assert", surname="Me", address="169, Green St", email="assert@gmail.com",
                                               email2="assert_me@gmail.com", email3="assert_itself@gmail.com", home_phone="0987654",
                                               mobile_phone="56565656", work_phone="345676543", secondary_phone="+1000000"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    index = randrange(len(contact_from_home_page))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert len(contact_from_home_page.Contact) == len(merge_phones_like_on_home_page(contact_from_edit_page))



def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.name, contact.surname, contact.id, contact.address, contact.email, contact.email2, contact.email3,
                                        contact.home_phone, contact.mobile_phone, contact.work_phone,
                                        contact.secondary_phone]))))

















