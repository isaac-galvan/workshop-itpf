import sys
from boxsdk import OAuth2, Client

# check for required arguments
if len(sys.argv) > 2:
    FOLDER_ID = sys.argv[1]
    PREFIX = sys.argv[2]
else:
    print('usage: python3 enforce-folder-name.py <folder-id> <prefix>')
    print('Enforces a name prefix on files and folders')
    exit()

# get an authenticated client
TOKEN = 'kMO3WAldsv5q33tsaEz6HpNo3OXYeIg5'
auth = OAuth2(None, None, access_token=TOKEN)
box = Client(auth)

# print the user and working folder
me = box.user().get()
print('box login:', me.login)
folder = box.folder(FOLDER_ID).get()
print('working folder:', folder)

# check if items start with the prefix
items = folder.get_items()
for item in items:
    if item.name.startswith(PREFIX):
        continue
    else:
        # update the item name if necessary
        new_name = PREFIX + item.name
        print('renaming', item, 'to', new_name)
        item.update_info({'name': new_name})
