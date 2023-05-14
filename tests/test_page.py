import allure

from models.registration_model import FormRegistration, Hobbies
from pages.registration_page import RegistrationPage


class TestPage:

    def test_form(self, setup_browser):
        with allure.step("Set user data"):
            user = FormRegistration(
                first_name='Иван',
                last_name='Иванов',
                email='ivan@ivanmail.ru',
                gender="Other",
                phone_number=7111111111,
                birth_month="November",
                birth_year="1990",
                birth_day="20",
                interests=Hobbies.science.value,
                hobby='Sports',
                photo_path="photo_test.jpg",
                address='USA, 12723 street',
                state='Rajasthan',
                city='Jaiselmer')

        with allure.step("Initialize form page"):
            registration = RegistrationPage(setup_browser)

        with allure.step("Open test urls"):
            registration.open_browser()

        with allure.step("Transmitted user data"):
            registration.registration_user(user)

        with allure.step("Compare transmitted and real data"):
            registration.assert_saved_form(user), \
                "Some field was not corrected"
