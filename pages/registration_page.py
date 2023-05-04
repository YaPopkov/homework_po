import os

from selene.support.shared import browser
from locators.page_locators import PageLocators
from selene import be, have, command


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element(PageLocators.first_name)
        self.last_name = browser.element(PageLocators.last_name)
        self.email = browser.element(PageLocators.email)
        self.gender = browser.element(PageLocators.gender_other)
        self.phone = browser.element(PageLocators.phone)

        self.hobby_one = browser.element(PageLocators.hobby_field)
        self.hobby_two = browser.element(PageLocators.hobby_choose)

        self.photo = browser.element(PageLocators.photo)

        self.address = browser.element(PageLocators.address)
        self.state = browser.element(PageLocators.state_choose)
        self.city = browser.element(PageLocators.city_choose)

        self.submit = browser.element(PageLocators.submit)

    def set_first_name(self, first_name):
        self.first_name.should(be.blank).type(first_name)
        return

    def set_last_name(self, last_name):
        self.last_name.should(be.blank).type(last_name)
        return

    def set_email(self, email):
        self.email.should(be.blank).type(email)
        return

    def set_gender(self, gender):
        self.gender.should(have.text(gender)).click()
        return

    def set_phone(self, phone):
        self.phone.should(be.blank).type(phone)
        return

    @staticmethod
    def set_date_birth():
        browser.element(PageLocators.date_birth_field).click()

        browser.element(PageLocators.date_birth_month).click()
        browser.element(PageLocators.date_birth_year).click()
        browser.element(PageLocators.date_birth_day).click()

        return

    def set_hobby_one(self, hobby):
        self.hobby_one.should(be.blank).type(hobby).press_enter()
        return

    def set_hobby_two(self, hobby):
        self.hobby_two.should(have.text(hobby)).click()
        return

    def set_photo(self, photo):
        self.photo.send_keys(os.getcwd() + "/tests/" + photo)
        return

    def set_address(self, address):
        self.address.should(be.blank).type(address)
        return

    def set_state(self, state):
        self.state.should(be.blank).type(state).press_enter()
        return

    def set_city(self, city):
        self.city.should(be.blank).type(city).press_enter()
        return

    def click_submit(self):
        self.submit.perform(command.js.click)
        return

    @staticmethod
    def assert_saved_form(first_name, last_name, email, gender, phone_number,
                          birth_day, birth_month, birth_year, interests, hobby,
                          photo_path, address, state, city):
        name = first_name + ' ' + last_name
        birthday = birth_day + ' ' + birth_month + ',' + birth_year
        state_city = state + ' ' + city

        browser.element(PageLocators.element_form_one).all(PageLocators.element_form_two).even.should(
            have.exact_texts(
                name,
                email,
                gender,
                f'{phone_number}',
                birthday,
                interests,
                hobby,
                photo_path,
                address,
                state_city
            )
        )
        browser.element(PageLocators.close_form).perform(command.js.click)
