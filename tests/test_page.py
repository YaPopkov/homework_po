from models.registration_model import FormRegistration, Hobbies
from pages.registration_page import RegistrationPage


class TestPage:

    @staticmethod
    def set_url():
        return 'https://demoqa.com/automation-practice-form'

    def test_form(self, driver_browser):
        user = FormRegistration(
            first_name='Иван',
            last_name='Иванович',
            email='ivan@maivan.ru',
            gender="Other",
            phone_number=7123456789,
            birth_month="November",
            birth_year="2000",
            birth_day="20",
            interests=Hobbies.science.value,
            hobby='Sports',
            photo_path="test_photo.jpg",
            address='USA, 12723 street',
            state='Rajasthan',
            city='Jaiselmer'
        )
        registration = RegistrationPage()

        registration.set_first_name(user.first_name)
        registration.set_last_name(user.last_name)
        registration.set_email(user.email)
        registration.set_gender(user.gender)
        registration.set_phone(user.phone_number)
        registration.set_date_birth()
        registration.set_hobby_one(user.interests)
        registration.set_hobby_two(user.hobby)
        registration.set_photo(user.photo_path)
        registration.set_address(user.address)
        registration.set_state(user.state)
        registration.set_city(user.city)
        registration.click_submit()

        registration.assert_saved_form(
            user.first_name, user.last_name,
            user.email,
            user.gender,
            user.phone_number,
            user.birth_day, user.birth_month, user.birth_year,
            user.interests,
            user.hobby,
            user.photo_path,
            user.address,
            user.state, user.city
        ), "Some field was not corrected"
