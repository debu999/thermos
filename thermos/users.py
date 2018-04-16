class Users:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def initials(self):
        return "{}. {}.".format(self.fname[0], self.lname[0])

    def __repr__(self):
        return self.initials()

    def getfullname(self):
        return " ".join([self.fname, self.lname]).strip()
