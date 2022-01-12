from selenium.webdriver.support.select import Select
from model.contact_model import Contact
import re


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

    def select_add_to_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_name("add").click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//option[@value='%s']" % id).click()

    def del_from_group(self):
        wd = self.app.wd
        wd.find_element_by_name("remove").click()

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
        self.name("phone2", contact_model.secondary_phone)
        self.name("email", contact_model.email)
        self.name("email2", contact_model.email2)
        self.name("email3", contact_model.email3)
        self.menu("bday", contact_model.birth_day)
        self.menu("bmonth", contact_model.birth_month)
        self.name("byear", contact_model.birth_year)
        self.menu("aday", contact_model.ann_day)
        self.menu("amonth", contact_model.ann_month)
        self.name("ayear", contact_model.ann_year)
        self.menu("new_group", contact_model.new_group)
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
            elif fieldname == "new_group":
                wd.find_element_by_xpath("//select[5]/option[2]").click()
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

    def del_contact_by_id(self, id):
        wd = self.app.wd
        # open contact list page
        wd.find_element_by_link_text("home").click()
        # select some random contact
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # select 'delete'
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # delete confirmation
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

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
                surname = cells[1].text
                name = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("id")
                all_phones = cells[5].text
                self.contact_cache.append(
                    Contact(name=name, surname=surname, id=id, address=address, all_emails=all_emails,
                            all_phones_from_home_page=all_phones))

        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        surname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(name=name, surname=surname, id=id, address=address, email=email, email2=email2, email3=email3,
                       home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
                       secondary_phone=secondary_phone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        ## secondary_phone is none --> failed due to splitted str
        #secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone)
