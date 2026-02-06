import cv2
import os
import numpy as np

try:
    import face_recognition
    FACE_REC_AVAILABLE = True
except ImportError:
    FACE_REC_AVAILABLE = False
    print("Warning: face_recognition library not installed. Face identification will be disabled.")

class FaceIdentifier:
    def __init__(self, reference_dir='reference_images'):
        self.known_face_encodings = []
        self.known_face_names = []
        self.enabled = FACE_REC_AVAILABLE
        if self.enabled:
            self.load_reference_images(reference_dir)

    def load_reference_images(self, reference_dir):
        if not os.path.exists(reference_dir):
            os.makedirs(reference_dir)
            print(f"Created reference directory: {reference_dir}. Please add images there.")
            return

        print(f"Loading reference images from {reference_dir}...")
        for filename in os.listdir(reference_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                path = os.path.join(reference_dir, filename)
                try:
                    image = face_recognition.load_image_file(path)
                    encodings = face_recognition.face_encodings(image)
                    if encodings:
                        encoding = encodings[0]
                        self.known_face_encodings.append(encoding)
                        # Use filename without extension as name
                        name = os.path.splitext(filename)[0]
                        self.known_face_names.append(name)
                        print(f"Loaded reference face: {name}")
                    else:
                        print(f"Warning: No face found in {filename}")
                except Exception as e:
                    print(f"Error loading {filename}: {e}")

    def identify(self, frame, location):
        """
        Identify a face at a specific location (top, right, bottom, left).
        """
        if not self.enabled or not self.known_face_encodings:
            return "Unknown"

        # Convert BGR (OpenCV) to RGB (face_recognition)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Get encoding for the specific face location
        try:
            encodings = face_recognition.face_encodings(rgb_frame, [location])
        except Exception as e:
            # Sometimes location might be out of bounds
            return "Error"
        
        if not encodings:
            return "Unknown"

        face_encoding = encodings[0]
        # Tolerance: lower is stricter. 0.6 is default.
        matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, tolerance=0.6)
        name = "Unknown"

        # Check if we have a match
        if True in matches:
            first_match_index = matches.index(True)
            name = self.known_face_names[first_match_index]
        
        return name
