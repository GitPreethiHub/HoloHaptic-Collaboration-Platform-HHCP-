## Overview
The **HoloHaptic Collaboration Platform (HHCP)** is a real-time collaborative platform that integrates holographic displays, haptic feedback, and AI-powered emotion recognition. The platform allows users to communicate via real-time messaging using WebSockets and analyze images with **IBM Watson's Visual Recognition API**.

## Features
- **Real-Time Messaging**: Instant, bi-directional communication between clients using WebSocket technology.
- **AI Image Recognition**: Leverage **IBM Watson** to detect emotions and faces in uploaded images.
- **Holographic Collaboration**: Designed for haptic feedback in future expansions.
- **Dockerized Application**: Easy to deploy anywhere with Docker support.
- **Optional Conda Environment**: For local environments, providing all dependencies.

## Technology Stack
- **Backend**: Flask, Python 3.10+
- **Real-Time Communication**: Flask-SocketIO (WebSocket integration)
- **AI**: IBM Watson Visual Recognition API for image analysis
- **Containerization**: Docker
- **Frontend**: Simple HTML/CSS interface served by Flask

## Prerequisites
- **Docker**: For running the containerized application.
- **Python 3.10+**: If you want to run the application locally without Docker.
- **Conda**: Optional, if you want to manage dependencies via Conda environments.

## Getting Started

### 1. Clone the Repository
clone the repository to your local machine using the following command:
 
git clone https://github.com/Subalakshmisuresh/HoloHaptic-Collaboration-Platform-HHCP-.git

cd HoloHaptic-Collaboration-Platform-HHCP-

### 2. Docker Setup
Build the Docker Image

Once the repository is cloned, build the Docker image. This will set up the container with all the necessary dependencies:
```
docker build -t hhcp-app .

```
### 3.Run the Docker Container
After the image is built, run the container to start the application:
```
docker run -p 5000:5000 hhcp-app
```
The application will now be running, and you can access it in your browser at http://localhost:5000.

### 3.1 Running Locally (Without Docker)
To run the application without Docker, follow these steps:

Install Python Dependencies

Make sure you have Python 3.10+ installed. Then install all the necessary dependencies using pip:
```
pip install -r requirements.txt
```

Run the Flask Application

Once the dependencies are installed, you can run the Flask application locally:

```
flask run --host=0.0.0.0 --port=5000
```
Visit http://localhost:5000 to view the application in your browser.

### 4.Using the Platform
Real-Time Messaging

Once the application is running, you can send real-time messages using the WebSocket functionality. Messages sent from the interface will be broadcast to all connected users.

Open your browser’s console (by pressing F12 or CTRL + SHIFT + I) to view the real-time message logs.

AI Image Recognition (IBM Watson)

The platform integrates IBM Watson Visual Recognition to analyze images and detect faces/emotions.

To use this feature, send an image file (JPEG, PNG) to the /analyze_image endpoint:

Example Image Recognition Request:

You can use curl to upload an image and receive a JSON response with the analysis:

```
curl -X POST http://localhost:5000/analyze_image -F "image=@"C:\Users\SEC\Pictures\images.jpg"
```
The API will return the detected faces, including emotional analysis if available.

### 5.Project Structure
```
HoloHaptic-Collaboration-Platform-HHCP/
│
├── app.py                       # Main Flask application
├── Dockerfile                    # Dockerfile for building the project
├── requirements.txt              # Python dependencies
├── environment.yml               # Optional, for Conda environments
├── README.md                     # Project documentation
├── templates/                    # HTML templates for Flask (if applicable)
│   └── index.html
└── static/                       # Static files (JS, CSS, images)
    └── styles.css

```
### Explanation of Key Files:
app.py: The main Python file that runs the Flask web application. It handles routes, WebSocket communication, and integrates with IBM Watson for image recognition.

Dockerfile: Defines the container setup for Docker. It ensures all dependencies are installed and sets up the app to run in a container.

requirements.txt: Contains the list of Python packages needed for the project, such as Flask, Flask-SocketIO, and IBM Watson SDK.

templates/index.html: A basic HTML page served by Flask, which allows users to interact with the platform.

static/styles.css: A simple CSS file for styling the frontend interface.

### API Endpoints

1. / - Home Route
   
Method: GET

Description: Renders the home page, which includes the messaging interface and image upload functionality.

3. /analyze_image - Image Analysis with IBM Watson
   
Method: POST

Description: Accepts an image upload (JPEG/PNG) and returns the results of IBM Watson's face and emotion detection.

Example Response:
```
{
  "images": [
    {
      "faces": [
        {
          "age": {
            "min": 25,
            "max": 35
          },
          "gender": {
            "gender": "MALE",
            "score": 0.95
          },
          "face_location": {
            "height": 131,
            "left": 75,
            "top": 22,
            "width": 104
          }
        }
      ]
    }
  ]
}
```
### WebSocket Communication
WebSocket Event: message

Description: Sends and receives messages via WebSocket. Every message is broadcast to all connected clients.

### IBM Watson Setup
To use IBM Watson Visual Recognition, you need to:

Create an IBM Cloud Account: If you don't have one, sign up at IBM Cloud.

Create a Visual Recognition Service: Go to the IBM Cloud dashboard, and create a new Visual Recognition instance.

Get Your API Key: In the service credentials, find or create an API key.

Add the API Key to Your Project: Replace your-ibm-watson-api-key-12345 and https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/12345 in app.py with your actual credentials.


