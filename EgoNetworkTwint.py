def first_degree_followers(user, f, ego_follows):

    twint.run.Followers(user)
    # save them in a list
    ids = twint.output.users_list
        
    #ids.extend(followers)
    for i in ids:
        f.write(str(i.followers) + "  " + str(i.username)  + "  " + str(ego_follows) + "  " + str(c.Username) + "\n")
    #time.sleep(randint(5, 30)
    print('1st degree followers scraped')
    
    return ids
#-------------------------------------------------------
def first_degree_friends(user, f, ego_follows):

    twint.run.Following(user)
    # save them in a list
    ids2 = twint.output.users_list
        
    #ids.extend(followers)
    for i in ids2:
        f.write(str(ego_follows) + "  " + str(c.Username) + "  " + str(i.followers) + "  " + str(i.username) + "\n")
    #time.sleep(randint(5, 30)
    print('1st degree friends scraped')

    return ids2
#---------------------------------------------------------
def second_degree_followers(users, f):

    ids = []
    for user in users:
        try:
            #ids = []
            c = twint.Config()
            c.Username = user.username
            c.Store_object = True
            c.User_full = True
            #c.Hide_output = True
            twint.run.Followers(c)
            ids = twint.output.users_list
            #time.sleep(randint(5, 30)
            for i in ids:
                f.write(str(i.followers) + "  " + str(i.username) + "  " + str(user.followers) + "  " + str(user.username) +  "\n")
        except Exception:
            pass
    print('2nd degree followers scraped')

#---------------------------------------------------------
def second_degree_friends(users, f):

    ids = []
    for user in users:
        try:
            c = twint.Config()
            c.Username = user.username
            c.Store_object = True
            c.User_full = True
            #c.Hide_output = True
            twint.run.Following(c)
            ids = twint.output.users_list
            #time.sleep(randint(5, 30)
            for i in ids:
                f.write(str(user.followers) + "  " + str(user.username) + "  " + str(i.followers) + "  " + str(i.username) + "\n")
        except Exception:
            pass
    print('2nd degree friends scraped')
    
    return ids
#---------------------------------------------------------
import twint
from importlib import reload
from time import time
from random import randint

c = twint.Config()
c.Username = ""
c.Store_object = True
c.User_full = True
ego_follows = ""

f  = open(c.Username +'-twitter-network.txt', 'w')

print('Retrieving user data...')

first_degree_followers = first_degree_followers(c, f, ego_follows)

twint.output.users_list = []
        
first_degree_friends = first_degree_friends(c, f, ego_follows)

twint.output.users_list = []

second_degree_followers(first_degree_followers, f)

twint.output.users_list = []

second_degree_friends(first_degree_friends, f)
       
f.close()
print('Twitter network ready...')
