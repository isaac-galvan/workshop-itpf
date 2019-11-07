import csv
import os.path
import sys
from boxsdk import OAuth2, Client


if len(sys.argv) > 2:
    CSV_FILE = sys.argv[1]
    FOLDER_ID = sys.argv[2]
else:
    print('usage: python3 upload-metadata.py <csv_file> <folder_id>')
    print('Uploads the files in the csv with metadata.')
    exit()

TOKEN = 'kMO3WAldsv5q33tsaEz6HpNo3OXYeIg5'
auth = OAuth2(None, None, access_token=TOKEN)
box = Client(auth)

me = box.user().get()
print('logged in to box as', me.login)

folder = box.folder(FOLDER_ID).get()
print('current folder', folder)

with open(CSV_FILE) as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        if os.path.isfile(row[0]):
            # upload the file
            new_file = box.folder(FOLDER_ID).upload(row[0])
            print('uploaded file', new_file)

            # add the metadata
            md = {
                'department': row[1],
                'location': row[2],
                'photographer': row[3]
            }
            applied_metadata = new_file.metadata().set(md)
            print('applied metadata', applied_metadata)
