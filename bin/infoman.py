from . import env


class SearchManager:
    def __init__(self, identifier):
        self.first = ""
        self.last = ""
        self.phone = int
        self.twitter = ""
        self.misc = []

    # compiles all information into document
    def data_compile(self):
        pass

    # goes out and grabs data from twitter
    def fetch_twitter(self, twitter):
        pass

    # goes out and grabs data from full contact
    def fetch_full_contact(self, *email, twitter, phone):
        pass

    # goes out and grabs data from WhitePages
    def fetch_white_pages(self):
        pass

    # fetches data from facebook
    def fetch_facebook(self):
        pass

    # checks if email has been pwned
    def check_email(self):
        pass

    def fetch_linkedin(self):
        pass


class Person:
    def __init__(self):
        self.first = ""
        self.last = ""
        self.email = ""
        self.twitter = ""
        self.phone = ""
        self.address = ""
        self.facebook = ""
        self.linkedin = ""
        self.youtube = ""
        self.misc_data_entries = []


class DataStorageManager:
    def __init__(self):
        pass
