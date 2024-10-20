from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, send
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

app = Flask(__name__)
socketio = SocketIO(app)

authenticator = IAMAuthenticator('your-ibm-watson-api-key-12345')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)
visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/12345')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    send(f'Server response: {msg}', broadcast=True)

@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    image = request.files.get('image')
    if image:
        image_path = './static/uploaded_image.jpg'
        image.save(image_path)
        with open(image_path, 'rb') as image_file:
            response = visual_recognition.detect_faces(image_file).get_result()
        return jsonify(response)
    else:
        return jsonify({"error": "No image uploaded"}), 400

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
