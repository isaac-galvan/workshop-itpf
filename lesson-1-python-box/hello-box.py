import sys
from boxsdk import OAuth2, Client

# handle auth and create box api client
TOKEN = 'VY7Hizc9HrkYG4KzqOfRiwamAtv1vC0C'
auth = OAuth2(None, None, access_token=TOKEN)
box = Client(auth)

# get user details from box
me = box.user().get()

# print function writes to screen
# here we write the login attribute
print('logged in to box as', me.login)

# print api response in dictionary
print(me.response_object)

# 0 is always the user's root folder
MY_FOLDER_ID = 0

# sys.argv is list of command line arguments
# len function returns count of list items
# get second command line arg if present
# indexes are 0-based
if len(sys.argv) > 1:
    MY_FOLDER_ID = sys.argv[1]

# get folders details from box
my_folder = box.folder(MY_FOLDER_ID).get()
# print info about folder
print('current folder', my_folder)

# get an iterator of the folder's items
# we can execute commands for each item
items = my_folder.get_items()
for i in items:
    print(i)