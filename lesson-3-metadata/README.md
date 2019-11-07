# Chapter 3: Metadata in Box

## What is Metadata?

From [Wikipedia: Metadata](https://en.wikipedia.org/wiki/Metadata):

> Metadata is "data that provides information about other data". In short, it's data about data.

Here are some examples of some types of metadata on some standard types of data you may have to work with:
> A digital image may include metadata that describes how large the picture is, the color depth, the image resolution, when the image was created, the shutter speed, and other data. A text document's metadata may contain information about how long the document is, who the author is, when the document was written, and a short summary of the document. Metadata within web pages can also contain descriptions of page content, as well as key words linked to the content.

SEE [Box: Admin Guide to Metadata](https://community.box.com/t5/How-to-Guides-for-Admins/How-to-Create-the-Right-Metadata-Structure-for-your-Enterprise/ta-p/43960) for details and examples.

## Welcome to North Brickton

You've been hired as the new community liaison for North Brickton. They've aquired a library of digital photographs over the years, and are working to get a handle on what they have.

Your intern is very smart and started a CSV (comma-seperated value) file containing info about these photos, and now you're looking at ways to use that information.

These photos are from [data.gov](https://catalog.data.gov/dataset/lego-diorama-images).
Download the set of photos for this exercise from [Box: Brickton Images](https://app.box.com/s/cm3la0roj6oa3bj2ljcwm0n5q5tms3t4) and extract them to a folder with the exercise files.

### The Data So Far

In our case, the CSV file, `filedata.csv`, has four columns:

```csv
filename, department, location, photographer
```

Each row represents a photo file and contains information about the filename, what city department is this photo related to, whether it was taken indoor or outside, and who the photographer was. 

## Starting Our Script

Create a new file `upload-metadata.py`, and add the following familiar code:

```python
import csv
import os.path
from boxsdk import OAuth2, Client

DEV_TOKEN = 'Sv26tCOFX2paSF5MobgSkXJXpkcvkvO9'
auth = OAuth2(None, None, access_token=DEV_TOKEN)
box = Client(auth)


if len(sys.argv) > 1:
    FOLDER_ID = sys.argv[1]
else:
    print('Specify a folder to enforce naming')
    exit()
```