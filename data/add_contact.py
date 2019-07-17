from model.contact import Contact
import random
import string


constant = [
    Contact(first_name="first", last_name="last", email="em", email2="em2", email3="em3",
                   day="day", month="mon", year="year", notes="no",
                   homephone="home", mobilephone="mob", workphone="work", secondaryphone="sec",
                   address="add", address2="add2"),
    Contact(first_name="first_1", last_name="last_1", email="em_1", email2="em2_1", email3="em3_1",
            day="day_1", month="mon_1", year="year_1", notes="no_1",
            homephone="home_1", mobilephone="mob_1", workphone="work_1", secondaryphone="sec_1",
            address="add_1", address2="add2_1"),
]


def random_string(prefix, maxlen):
    symbol = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", last_name="", email="", email2="", email3="",
                   day="", month="", year="", notes="",
                   homephone="", mobilephone="", workphone="", secondaryphone="",
                   address="", address2="")] + [
    Contact(first_name=random_string("aaa", 10), last_name=random_string("aaa", 10),
            email=random_string("kaka@mail.ru", 10), email2=random_string("byby@bb.ru", 10),
            email3=random_string("mmm@ya.ru", 10), day=random_string("10", 10),
            month=random_string("April", 10), year=random_string("1990", 10), notes=random_string("1", 10),
            homephone=random_string("12399", 10), mobilephone=random_string("12345", 10),
            workphone=random_string("123456", 10), secondaryphone=random_string("212121", 10),
            address=random_string("Moscow", 10), address2=random_string("Paris", 10))
    for i in range(3)
    ]
