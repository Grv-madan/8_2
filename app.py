from flask import Flask, request, render_template, redirect, url_for, send_from_directory

import os

app = Flask(__name__)

# Configure the upload folder and ensure it exists

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

if not os.path.exists(UPLOAD_FOLDER):

   os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')

def index():

   # Show a simple HTML form to upload files and list uploaded images.

   images = os.listdir(app.config['UPLOAD_FOLDER'])

   return render_template('index.html', images=images)

@app.route('/upload', methods=['POST'])

def upload_image():

   if 'image' not in request.files:

       return "No file part", 400

   file = request.files['image']

   if file.filename == '':

       return "No selected file", 400

   # Save the file

   file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

   return redirect(url_for('index'))

@app.route('/uploads/<filename>')

def uploaded_file(filename):

   return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

   if name == "__main__":
      app.run(host="0.0.0.0", port=5000, debug=True)