import cv2
import numpy as np

def recognize_face(image_path, known_face_path):
    # Load the pre-trained face recognition model from OpenCV
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Load the known face image and its label
    known_face_image = cv2.imread(known_face_path, 0)  # Load as grayscale
    known_face_label = 1  # You can assign any label you want

    # Train the face recognizer with the known face
    face_recognizer.train([known_face_image], np.array([known_face_label]))

    # Load the image to be recognized
    test_image = cv2.imread(image_path, 0)  # Load as grayscale

    # Perform face recognition on the test image
    label, confidence = face_recognizer.predict(test_image)

    # Display the result
    if label == known_face_label:
        print("Face recognized as the known person with confidence:", confidence)
    else:
        print("Unknown face detected.")

# Replace 'path/to/your/image.jpg' and 'path/to/your/known_face_image.jpg' with the actual file paths
recognize_face('/content/OIP2.jpeg')
