from sys import maxsize


class Contact:

    def __init__(self, id=None, first_name=None, last_name=None, email=None, email2=None, email3=None,
                 day=None, month=None, year=None, notes=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None,
                 address=None, address2=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.day = day
        self.month = month
        self.year = year
        self.notes = notes
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.address = address
        self.address2 = address2
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page


    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.first_name, self.last_name, self.homephone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
