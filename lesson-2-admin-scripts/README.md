# Lesson 2: Writing an Admin Script

The first things collaborators see is a folder's name. Include a reminder that this data is sensitive or only for a certain group in the folder's name to provide important context.

Including phrases like INTERNAL or PRIVATE give a clue that the contents should be handled carefully.

See [Box Service Blog: Secure Folders: Name and Describe the Contents](https://boxservice.web.illinois.edu/2019/02/14/secure-folders-name-and-describe-the-contents/) for more tips on name sensitive files.

## The Objective

We want to enforce a naming convention on all of the items in a folder, prepending the text PRIVATE to all file and folder names.  Let's get started:

## The Application

Create a new Python file, `lesson2.py`, and add the following lines from our last exercise.

```python
import sys
from boxsdk import OAuth2, Client

TOKEN = 'VY7Hizc9HrkYG4KzqOfRiwamAtv1vC0C'
auth = OAuth2(None, None, access_token=TOKEN)
box = Client(auth)

me = box.user().get()

print('logged in to box as', me.login)
```

Last time, our script defaulted to the root folder, `0`, when the user did not specify a folder in the command line arguments. 

This time, we'll require two arguments, the folder ID and the prefix to enforce, otherwise the app won't run.

```python
if len(sys.argv) > 2:
    FOLDER_ID = sys.argv[1]
    PREFIX = sys.argv[2]
else:
    print('usage: python3 enforce-folder-name.py <folder-id> <prefix>')
    print('Enforces a name prefix on files and folders')
    exit()
```

We'll retrieve the folder items again. On each item in the iterable, we'll check if the name starts with the prefix. We do this in the `if` statement. The `continue` statement tells the interpreter that this `item` is done being processed so it can go on to the next one.

The `else` statement renames the file if the prefix is not present.

```python
items = folder.get_items()

for item in items:
    if item.name.startswith(PREFIX):
        continue
    else:
        # update the item name if necessary
        new_name = PREFIX + item.name
        print('renaming', item, 'to', new_name)
        item.update_info({'name': new_name})
```
