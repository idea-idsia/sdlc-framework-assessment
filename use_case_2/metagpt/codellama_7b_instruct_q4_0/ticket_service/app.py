from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import os
from PIL import Image
from io import BytesIO
from google.cloud import vision
from google.oauth2.credentials import Credentials

app = Flask(__name__)

# Load credentials for Google Cloud Vision API
creds = None
if os.path.exists('key.json'):
    with open('key.json', 'r') as f:
        creds = json.load(f)

# If credentials file exists, use it to create a client object
if creds is not None:
    vision_client = vision.ImageAnnotatorClient(credentials=creds)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/images', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        image_id = Image(filename=file.filename, filepath=os.path.join('static/uploads', file.filename)).save()
        return jsonify({'image_id': image_id})
    else:
        return jsonify({'error': 'Invalid request method'})

@app.route('/predictions', methods=['GET'])
def get_predictions():
    if request.method == 'GET':
        image_id = request.args.get('image_id')
        predictions = Image(image_id).get_predictions()
        return jsonify({'predictions': predictions})
    else:
        return jsonify({'error': 'Invalid request method'})

class Image:
    def __init__(self, filename, filepath):
        self.filename = filename
        self.filepath = filepath

    def upload(self, image_file):
        # Save the uploaded image to the static/uploads folder
        image_file.save(os.path.join('static/uploads', self.filename))

    def get_predictions(self):
        # Load the saved image from the static/uploads folder
        with open(self.filepath, 'rb') as f:
            content = f.read()

        # Create a Google Cloud Vision API client object
        if creds is not None:
            vision_client = vision.ImageAnnotatorClient(credentials=creds)

        # Send the image to the Google Cloud Vision API for label detection
        response = vision_client.label_detection(image=content)

        # Get the labels from the response
        labels = response.label_annotations

        # Return a list of Prediction objects
        return [Prediction(label.description, label.score) for label in labels]

class Prediction:
    def __init__(self, label, confidence):
        self.label = label
        self.confidence = confidence
