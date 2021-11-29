from model.contact_model import Contact


def test_edit_first_contact(app):

    if app.contact.count_contact_entries() == 0:
        app.contact.create_new_contact(Contact(name="Edit_me", middlen="", surname="", nick="H", company="Company1",
                                address="111, Street", home_phone="12345678", mobile_phone="12345678",
                                work_phone="12345678", email="aaaa@gmail.com", email2="aaaa@gmail.com",
                                email3="aaaa@gmail.com", birth_day="3", birth_month="March", birth_year="1987",
                                ann_day="16", ann_month="August", ann_year="1976", address2="222, Street"))
    app.contact.edit_first_contact(Contact(name="Name111", middlen="", surname="", nick="H", company="Company1",
                                address="111, Street", home_phone="12345678", mobile_phone="12345678",
                                work_phone="12345678", email="aaaa@gmail.com", email2="aaaa@gmail.com",
                                email3="aaaa@gmail.com", birth_day="3", birth_month="March", birth_year="1987",
                                ann_day="16", ann_month="August", ann_year="1976", address2="222, Street"))
    app.return_to_home_page()

