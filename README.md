# Face Recognition

A Python-based project that implements real-time face detection and recognition using OpenCV. This repository contains scripts for training a model on custom datasets, detecting faces in images/videos, and recognizing known faces.

## 📂 Project Structure

- **Core Scripts:**
  - `faces_train.py`: Reads the dataset from the `faces/` directory, detects faces, and trains the LBPH (Local Binary Patterns Histograms) recognizer. Saves the trained model to `face_trained.yml`.
  - `face_recognition.py`: Loads the trained model and performs face recognition, typically via webcam or on static images.
  - `face_detect.py`: Basic script to detect faces in an image using Haar Cascades.
  - `haarcascade_face.xml`: Pre-trained Haar Cascade classifier used for face detection.

- **Utilities & Learning:**
  - `vidCapture.py`: Helper to test video capture from a webcam.
  - `draw.py`, `contours.py`, `transformations.py`: Various utility scripts demonstrating OpenCV functions like drawing, contour detection, and image transformations.
  - `rescale.py`: Utility to rescale frames or images.

## 🛠️ Prerequisites

To run this project, you need Python installed along with the following libraries:

- **OpenCV** (specifically `opencv-contrib-python` for the face module)
- **NumPy**

## 📥 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/manankasturia/Face-Recognition.git](https://github.com/manankasturia/Face-Recognition.git)
   cd Face-Recognition

2. **Install Dependencies:**
   ```bash
   pip install opencv-contrib-python numpy
Note: We use opencv-contrib-python instead of just opencv-python to ensure the cv2.face module (required for the LBPH recognizer) is available.

## 🚀 Usage

1. **Prepare your Dataset**
   Organize your training images in the faces/ directory. The structure should ideally be:
   ```bash
   faces/
    ├── Person_Name_1/
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   └── ...
    ├── Person_Name_2/
    │   ├── image1.jpg
    │   └── ...
Make sure the images clearly show the face of the person you want to recognize.

2. **Train the Model**
   Run the training script to generate the model file (face_trained.yml) and save feature data (features.npy, labels.npy).
   ```bash
   python faces_train.py

3. **Run Face Recognition**
   Once trained, you can run the recognition script. This will likely open your webcam or process an image to identify the people trained in step 2.
   ```bash
   python face_recognition.py

## 📸 Other Features

- **Basic Detection:** Run python `face_detect.py` to simply detect faces without recognition.
- **Group Photos:** Scripts like `group_faceDetect.py` are designed to handle images with multiple faces.
- **Image Processing:** Explore files like `contours.py`, `gradients_edges.py`, and `colorSpaces.py` to see examples of different computer vision techniques.
