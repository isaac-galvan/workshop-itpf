import os.path
import glob
import sys
from boxsdk import OAuth2, Client
from imageai.Prediction import ImagePrediction

if len(sys.argv) > 1:
    FOLDER_ID = sys.argv[1]
else:
    print('usage: python3 image-detect-upload.py <destination_folder_id>')
    print('Use image detection software to make predictions.')
    print('Upload the file and predictions to Box.')
    exit()

TOKEN = 'yEUCETgkQSQIitfOBTBHtQKjkRQZ957i'
auth = OAuth2(None, None, access_token=TOKEN)
box = Client(auth)

me = box.user().get()
print('logged in to box as', me.login)

folder = box.folder(FOLDER_ID).get()
print('current folder', folder)

# setup prediction engine
engine = ImagePrediction()
engine.setModelTypeAsDenseNet()
engine.setModelPath('DenseNet-BC-121-32.h5')
engine.loadModel()

# get .jpg files
jpg_files = glob.glob('*.jpg')
for image in jpg_files:
    # run image through prediction engine
    prediction, probablity = engine.predictImage(image)
    prediction_data = {
        'prediction1': prediction[0] + ' : ' + probablity[0].astype(str),
        'prediction2': prediction[1] + ' : ' + probablity[1].astype(str),
        'prediction3': prediction[2] + ' : ' + probablity[2].astype(str),
    }
    new_file = box.folder(FOLDER_ID).upload(image)
    print('uploaded file', new_file)

    # add the metadata
    applied_metadata = new_file.metadata().set(prediction_data)
    print('applied metadata', applied_metadata)


