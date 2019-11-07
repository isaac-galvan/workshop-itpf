# Lesson One: Python and Box SDK

> cloud storage API + machine learning = endless possibilities

In this lesson, we will:

* Start the Python command line
* Install the `boxsdk` packing using `pip`
* Create an app in the dev console
* Write an app to list a folder's contents
* Loop through a `List` with `for`
* Read a command line argument

Python is an "interpreted" language, meaning programs are not compiled, and instead the code is executed in order and immediately.

With Python and a cloud storage API, we can script how we upload and manage our data for repeatable outcomes. Protect your Python data management scripts like any other code or dataset.

In this lesson, we'll get started using the Box SDK for Python.

Start Python 3 from the command line with `python` command, or `python3` on some systems.

``` bash
# check which version of Python
$ python3 --version
Python 3.7.4
```

## Installing the Box SDK for Python

To install the [Box SDK for Python](https://github.com/box/box-python-sdk), use the following command:

```bash
$ python3 -m pip install boxsdk
```

This gets the package from the [Python Package Index](https://pypi.org), or PyPI, which is a repository of software for the Python programming language. Using PyPI, you can easily find and install libraries to do just about anything.

## Starting Your First App

In development, we'll use a **Developer Token**. Working with a development token has several advantages:

* Available to any Box user with no admin intervention
* Don't need to understand OAuth complex token release/refresh processes
* Start developing proof of concept in minutes
* Limits scope to the user who generated token
* Don't need to be guarded closely as regular token since they expire in one hour

### Creating a Custom App in Box

When logged in to your developer account, visit the  to create a custom app and get started.

1. Log in to the [Developer Console](https://app.box.com/developers/console)
2. Select "Custom App" option and then Next
3. Select "Standard OAuth 2.0" and then Next
4. Provide a unique name for your application

For more info, see [Box Developer Guides: Setup with OAuth 2.0](https://developer.box.com/en/guides/applications/custom-apps/oauth2-setup/)

### Create a Developer Token

After you've created your custom app, you can create a Developer Token.

1. Go to the [Developer Console](https://app.box.com/developers/console) and select your custom app.
2. From the sidebar, select **Configuration**.
3. In the Developer Token section, select **Generate Developer Token**

See more at [Box Developer Guides: Developer Tokens](https://developer.box.com/en/guides/authentication/access-tokens/developer-tokens/)

## Your First Python App

Create a new file and save it as `lesson-1.py`. This will be the script that will run your program and can be shared and updated. To run the code in `lesson-1.py`, run the following command in your terminal:

```bash
$ python3 lesson-1.py

```

### Importing the BoxSDK

Add the following line to your `lesson-1.py` file:

```python
from boxsdk import OAuth2, Client
```

You are importing two classes from the `boxsdk` library for use in your application. The `OAuth2` class handles managing your user authentication to Box, and the `Client` provides access to the Box API endpoints.

### Using Variables

**Variables** store references to objects. They are created when a statement assigns a value to a name using an **assignment statement**.

Here we're defining a few **variables** to store refences to a string (for the dev token) and two object instances representing an authentication class and an API client.

To create a Box client authenticated by developer token, add these lines to your `lesson-1.py` file:

```python
# the token you generated in dev console
TOKEN = 'VY7Hizc9HrkYG4KzqOfRiwamAtv1vC0C'

auth = OAuth2(None, None, access_token=TOKEN)
box = Client(auth)
```

[PEP-8](https://www.python.org/dev/peps/pep-0008/) suggests using all upper case for variables that are "constant" and should not change over the execution of your Python application. See [PEP-8](https://www.python.org/dev/peps/pep-0008/) for more code formatting suggesions.

### Call the Box API

To call the API, we'll be executing a **method** of the `Client` object. **Methods** are functions that run on an instance of a class, and use it's state to perform the action.

Let's make our first API call to Box. We'll use the following methods to call the Users API endpoint and get the details of the currently authenticated user.

```python
me = box.user().get()
print('logged in to Box as', me.login)
```

The `print` function types text to the screen. We're passing two arguments, the first a string in single quotes,  and the second a reference to the `me` object's `login` attribute.

We can print out a **dictionary** of the Box API's full response to our request. A dictionary is a collection of key/value pairs.

```python
print(me.response_object)
```

Now we'll contact the `Folder` API endpoint and get information about your root folder.

```python
MY_FOLDER_ID = 0
my_folder = box.folder(MY_FOLDER_ID).get()
print('current folder', my_folder)
```

The `.folder()` method takes a parameter, a folder id, and requests it's details from the API. `0` is always the user's root folder.

The `my_folder` variable now references an object pointing to your root folder in Box, and we can use the `get_items()` method to get an interable of the folder's subfolders and files.

```python
items = my_folder.get_items()
for i in items:
    print(i)
```

## Python Command Line Application

Let's make this app more useful by letting it get the contents of a folder you specify at runtime. We'll need to import the `sys` library, which provides access to some variables maintained by the Python interpreter.

```python
import sys
```

We need to change the value of `MY_FOLDER_ID` if a command-line parameter is given. After the line where we assign the `MY_FOLDER_ID` variable a default value of 0, let's add:

```python
if len(sys.argv) > 1:
    MY_FOLDER_ID = sys.argv[1]
```

Now we can run `python3 lesson-1.py` again, but with a parameter, and our application will display the contents of the folder with the ID you provided. Try this with one of your folders:

```bash
$ python3 lesson-1.py 91911893299
current folder <Box Folder - 91911893299 (sample-images)>
<Box File - 549795389166 (ampersand-creative-co-pp_oXEb2H48-unsplash.jpg)>
<Box File - 549791442083 (apostolos-vamvouras-FjvIsYAqoic-unsplash.jpg)>
<Box File - 549795846679 (ariana-suarez-J7rRzjba-kY-unsplash.jpg)>
<Box File - 549795683119 (arlindo-camacho-6AMtsqdAHCo-unsplash.jpg)>
<Box File - 549795111099 (collins-lesulie-Q7QM2WSOTs4-unsplash.jpg)>
...
```