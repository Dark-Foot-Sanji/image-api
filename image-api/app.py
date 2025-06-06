from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)

# Define the image folder
IMAGE_FOLDER = 'static'
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

# Route: Home Page
@app.route('/')
def home():
    return "📸 Image API is running!"

# Route: List all images
@app.route('/images')
def list_images():
    files = os.listdir(IMAGE_FOLDER)
    image_urls = [f"http://localhost:5000/image/{file}" for file in files]
    return jsonify(image_urls)

# Route: Get specific image by filename
@app.route('/image/<filename>')
def get_image(filename):
    return send_from_directory(app.config['IMAGE_FOLDER'], filename)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
