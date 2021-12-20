from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact_model import Contact
from pymysql.converters import decoders


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, colomn='group_id')
        name = Optional(str, colomn='group_name')
        header = Optional(str, colomn='group_header')
        footer = Optional(str, colomn='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, colomn='id')
        firstname = Optional(str, colomn='firstname')
        lastname = Optional(str, colomn='lastname')
        deprecated = Optional(datetime, colomn='deprecated')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))


    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), name=contact.name, surname=contact.surname)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))
