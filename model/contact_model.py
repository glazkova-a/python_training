from sys import maxsize


class Contact:
    def __init__(self, name=None, middlen=None, surname=None, nick=None, company=None, address=None, home_phone=None,
                 mobile_phone=None, work_phone=None, secondary_phone=None, email=None, email2=None, email3=None, birth_day=None, birth_month=None,
                 birth_year=None, ann_day=None, ann_month=None, ann_year=None, address2=None, id=None, all_phones_from_home_page=None):
        self.name = name
        self.middlen = middlen
        self.surname = surname
        self.nick = nick
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.birth_year = birth_year
        self.ann_day = ann_day
        self.ann_year = ann_year
        self.ann_month = ann_month
        self.address2 = address2
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.surname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.name == other.name and self.surname == other.surname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize