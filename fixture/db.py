import pymysql.connections
from model.hw_group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), first_name=firstname, last_name=lastname))
        finally:
            cursor.close()
        return list

    def get_groups_with_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups")
            for row in cursor:
                (id,) = row
                list.append(Group(id=str(id)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_all_contact_list(self, id_db):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, mobile, home, work, email, email2, email3"
                           " from addressbook where deprecated = '0000-00-00 00:00:00' and id='%s'" % id_db)
            for row in cursor:
                (id, firstname, lastname, address, mobile, home, work, email, email2, email3) = row
                list = (Contact(id=str(id), first_name=firstname,last_name=lastname, address=address,
                                mobilephone=mobile, homephone=home, workphone=work, email=email,
                                email2=email2, email3=email3))
        finally:
            cursor.close()
        return list