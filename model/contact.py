from sys import maxsize


class Contact:

    def __init__(self, first_name=None, last_name=None, email=None, day=None,
                     month=None, year=None, notes=None,homephone=None, mobilephone=None,
                       workphone=None, secondaryphone=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.day = day
        self.month = month
        self.year = year
        self.notes = notes
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone



    def __repr__(self):
        return "%s:%s" % (self.id, self.first_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
