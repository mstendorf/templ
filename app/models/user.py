
class User():

    #constructor
    def __init__(self, name, email,title):
        self.name = name
        self.email = email
        self.title = title

    # std method for representation as string eg. print(user)
    def __repr__(self):
        return """
Name   : %s
Email  : %s
Title  : %s
        """ % (self.name,self.email,self.title)
