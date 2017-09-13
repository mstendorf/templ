
from app.util import *
from app.models import User


users = []
def main():
    global users
    ## do stuff
    print("program started.")


    for i in range(5):
        u = User("fuckboi%d"%i, "fuckboi%d@plebs.com"%i,"Master of %d fuckboys!" % i)
        users.append(u)


    print_user_list(users)
