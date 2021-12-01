from selenium.webdriver.support.select import Select
from model.contact_model import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create_new_contact(self, contact_model):
        # init new contact creation
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_in_contact_form(contact_model)
        # submit form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # open contact list page
        wd.find_element_by_link_text("home").click()
        # click "edit" some random image
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_in_contact_form(new_contact_data)
        # submit editing
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def fill_in_contact_form(self, contact_model):
        wd = self.app.wd
        self.name("firstname", contact_model.name)
        self.name("middlename", contact_model.middlen)
        self.name("lastname", contact_model.surname)
        self.name("nickname", contact_model.nick)
        self.name("company", contact_model.company)
        self.name("address", contact_model.address)
        self.name("home", contact_model.home_phone)
        self.name("mobile", contact_model.mobile_phone)
        self.name("work", contact_model.work_phone)
        self.name("email", contact_model.email)
        self.name("email2", contact_model.email2)
        self.name("email3", contact_model.email3)
        self.menu("bday", contact_model.birth_day)
        self.menu("bmonth", contact_model.birth_month)
        self.name("byear", contact_model.birth_year)
        self.menu("aday", contact_model.ann_day)
        self.menu("amonth", contact_model.ann_month)
        self.name("ayear", contact_model.ann_year)
        self.name("address2", contact_model.address2)

    def name(self, fieldname, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(fieldname).click()
            wd.find_element_by_name(fieldname).clear()
            wd.find_element_by_name(fieldname).send_keys(text)

    def menu(self, fieldname, text):
        wd = self.app.wd
        if text is not None:
            if fieldname == "bmonth":
                wd.find_element_by_xpath("//option[@value='3']").click()
            else:
                wd.find_element_by_name(fieldname).click()
            Select(wd.find_element_by_name(fieldname)).select_by_visible_text(text)

    def del_first_contact(self):
        self.del_contact_by_index(0)

    def del_contact_by_index(self, index):
        wd = self.app.wd
        # open contact list page
        wd.find_element_by_link_text("home").click()
        # select some random contact
        wd.find_elements_by_name("selected[]")[index].click()
        # select 'delete'
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # delete confirmation
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def count_contact_entries(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                if cells[1]:
                    surname = cells[1].text
                if cells[2]:
                    name = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(name=name, surname=surname, id=id))
        return list(self.contact_cache)












