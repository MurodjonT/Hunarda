import random as r
import datetime as d
class TestDatas:
    login_admin = "admin"
    password_admin = "12345678"

    login = "admin"
    password = "1"
    date = d.datetime.now()
    alpha = "1234567890"
    res = r.choices(alpha, k=3)
    res1 = ''.join(res)
    random_course_name = "course_name{}".format(res1)  # create random name
