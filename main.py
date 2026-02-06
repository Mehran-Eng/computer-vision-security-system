import cv2
import threading
from detector import ObjectDetector
from recognizer import FaceIdentifier
from alert import AlertSystem
import time

def main():
    # Initialize modules
    print("Initializing Security System...")
    detector = ObjectDetector(model_path='yolov8n.pt')
    recognizer = FaceIdentifier(reference_dir='reference_images')
    alert_system = AlertSystem()

    # Open Camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Set camera resolution (optional, for performance)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    print("System active. Press 'q' to quit.")

    frame_count = 0
    
    # Store the last recognized name to display it for a few frames
    last_identified_name = None
    identification_cooldown_frames = 30
    frames_since_last_id = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
            
        frame_count += 1
        
        # 1. Object Detection
        # Detect people and weapons
        detections = detector.detect(frame)
        
        person_detected = False
        weapon_detected = False
        
        current_faces = []

        for det in detections:
            x1, y1, x2, y2 = map(int, det['box'])
            cls_id = det['class']
            label = det['label']
            conf = det['conf']
            
            # Determine color and alert status
            color = (0, 255, 0) # Green default
            
            if cls_id == 43: # Knife/Weapon
                color = (0, 0, 255) # Red
                label = f"WEAPON ({label})"
                weapon_detected = True
            elif cls_id == 0: # Person
                person_detected = True
                current_faces.append((x1, y1, x2, y2))
            
            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # 2. Face Recognition (Only if person detected)
        # We process face recognition periodically to save FPS
        identified_name = None
        
        if person_detected and recognizer.enabled:
            # Check every 10 frames
            if frame_count % 10 == 0:
                # Find the largest person box or check all? 
                # For simplicity, we check all detected people
                for (x1, y1, x2, y2) in current_faces:
                    # Face location for face_recognition: (top, right, bottom, left)
                    # We approximate the face to be the top part of the person box if we don't have a face detector
                    # NOTE: YOLO detects full body. Passing full body to face_recognition might fail if the face is small.
                    # Ideally we use a face detector, but face_recognition has one built-in (hog/cnn).
                    # We can pass the cropped person image to identify or just the full frame with approximate location.
                    # Let's try passing the approximate location of the face (top 1/3 of body)
                    
                    face_h = (y2 - y1) // 3
                    face_loc = (y1, x2, y1 + face_h, x1)
                    
                    # Alternatively, just let face_recognition find faces in the crop?
                    # Let's try: crop the person, find face, identify.
                    # Or simpler: just pass the crop to identify logic which can find face.
                    
                    # Let's use the explicit location we estimated to speed it up
                    name = recognizer.identify(frame, face_loc)
                    if name != "Unknown" and name != "Error":
                        identified_name = name
                        last_identified_name = name
                        frames_since_last_id = 0
            
            # Persist the name for a few frames for visual stability
            if last_identified_name and frames_since_last_id < identification_cooldown_frames:
                frames_since_last_id += 1
                identified_name = last_identified_name
            else:
                last_identified_name = None

        # 3. Alerts
        alert_msg = ""
        if weapon_detected:
            alert_system.trigger_alert()
            alert_msg = "WARNING: WEAPON DETECTED"
            cv2.putText(frame, alert_msg, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        
        if identified_name:
            # Check if this person is a "target" (logic can be customized)
            # For now, we alert on ANY identified person
            alert_system.trigger_alert()
            msg = f"TARGET: {identified_name}"
            cv2.putText(frame, msg, (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

        # Show feed
        cv2.imshow('Security Feed', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
