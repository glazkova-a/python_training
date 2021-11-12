# -*- coding: utf-8 -*-


import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_group2(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="uiuiuiui", header="hjhjhjh", footer="kokokok"))
    app.logout()

def test_add_empty_group2(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()



