from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os
import cv2
from pathlib import Path
import torch
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
DETECT_FOLDER = 'static/detections/'
Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)
Path(DETECT_FOLDER).mkdir(parents=True, exist_ok=True)

# Load your custom model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/admin/yogaPose/yolov5/runs/train/exp2/weights/best.pt')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            img_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(img_path)

            # Perform detection
            results = model(img_path)
            img = cv2.imread(img_path)

            # Draw rectangles and labels on the image
            for *xyxy, conf, cls in results.xyxy[0]:
                label = f"{results.names[int(cls)]} {conf:.2f}"
                cv2.rectangle(img, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (255,0,0), 2)
                #cv2.putText(img, label, (int(xyxy[0]), int(xyxy[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2)
            
            # Resize the image for better viewing
            img = resize_image(img)
            
            # Save the image with detections
            detect_img_path = os.path.join(DETECT_FOLDER, filename)
            cv2.imwrite(detect_img_path, img)

            # Extract predictions
            predictions = []
            for *xyxy, conf, cls in results.xyxy[0]:
                prediction = {
                    'name': results.names[int(cls)],
                    'confidence': conf.item()
                }
                predictions.append(prediction)

            return render_template('prediction.html', filename=filename, predictions=predictions)
    return render_template('index.html')

def resize_image(image, max_size=800):
    h, w = image.shape[:2]
    # Calculate the scaling factor
    scale = max_size / max(h, w)
    if scale < 1:
        # Resize the image
        new_w = int(w * scale)
        new_h = int(h * scale)
        return cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)
    return image  # Return original image if no resizing is needed

@app.route('/detections/<filename>')
def send_detection_file(filename=''):
    return send_from_directory(DETECT_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)