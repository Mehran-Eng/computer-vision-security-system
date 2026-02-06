from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path='yolov8n.pt'):
        # Load the YOLOv8 model
        self.model = YOLO(model_path)
        # COCO Classes: 0: person, 43: knife
        # Note: 'gun' is not in standard COCO 80 classes usually, but we can check if it exists or use a custom model.
        # For now, we stick to person and knife.
        self.target_classes = [0, 43] 

    def detect(self, frame):
        """
        Run detection on a single frame.
        Returns a list of dicts: {'box': [x1, y1, x2, y2], 'conf': float, 'class': int, 'label': str}
        """
        results = self.model(frame, verbose=False)
        detections = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                cls_id = int(box.cls[0])
                if cls_id in self.target_classes:
                    detections.append({
                        'box': box.xyxy[0].tolist(),
                        'conf': float(box.conf[0]),
                        'class': cls_id,
                        'label': self.model.names[cls_id]
                    })
        return detections
