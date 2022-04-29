from faker import Faker

from radar import randint
import datetime
fake = Faker(locale='en_CA')

app = 'WeGoStudy'
wegosty_url = 'http://34.233.225.85/students/admissions'
werosty_home_page_title = ''
consultant_email = 'chris.velasco78@gmail.com'
first_name = fake.first_name()
last_name = fake.last_name()
passport_number = 'PA0940443'
phone_number = fake.phone_number()
pass_number = f'PA{fake.pyint(111, 9999)}'
apt_num = fake.pyint(1111, 9999999)
mailing_address = f'{apt_num}{fake.address()}'
postal_code = fake.postalcode()
user_email = f'{first_name}@{fake.free_email_domain()}'
# date_of_birth = fake.date()

# date = random_date(start=1/1/2018, stop=22/5/2022)

# from datetime import datetime

# d1 = datetime('2008/1/1', '%Y/%m/%d')
# d2 = datetime('2022/1/22', '%Y/%m/%d')
# d3 = random_date(d1, d2)
# print(random_date(d1, d2))

d = datetime.date(randint(1956, 2022), randint(1, 12), randint(1, 28))

