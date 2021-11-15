def test_edit_first_contact(app):

    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact()
    app.return_to_home_page()
    app.session.logout()
