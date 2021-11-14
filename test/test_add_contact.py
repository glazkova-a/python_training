# -*- coding: utf-8 -*-


from model.contact_model import Contact


def test_add_new_contact(app):

    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.create_new_contact(Contact(name="A", middlen="B", surname="C", nick="D", company="Company1",
                                address="111, Street", home_phone="12345678", mobile_phone="12345678",
                                work_phone="12345678", email="aaaa@gmail.com", email2="aaaa@gmail.com",
                                email3="aaaa@gmail.com", birth_day="3", birth_month="March", birth_year="1987",
                                ann_day="16", ann_month="August", ann_year="2000", address2="222, Street"))
    app.return_to_home_page()
    app.session.logout()




