
class PageLocators:
    URL = 'https://demoqa.com/automation-practice-form'

    first_name = '#firstName'
    last_name = '#lastName'
    email = '#userEmail'

    gender_male = '[for="gender-radio-1"]'
    gender_female = '[for="gender-radio-2"]'
    gender_other = '[for="gender-radio-3"]'

    phone = '#userNumber'

    date_birth_field = '#dateOfBirthInput'
    date_birth_month = f'select[class="react-datepicker__month-select"] [value="10"]'
    date_birth_year = f'select[class="react-datepicker__year-select"] [value="1990"]'
    date_birth_day = ".react-datepicker__day--020"

    hobby_field = '#subjectsInput'
    hobby_choose = '[for="hobbies-checkbox-1"]'

    photo = '#uploadPicture'

    address = '#currentAddress'

    state_choose = '#react-select-3-input'
    city_choose = '#react-select-4-input'

    submit = '#submit'

    element_form_one = '.table'
    element_form_two = 'td'

    close_form = '#closeLargeModal'
