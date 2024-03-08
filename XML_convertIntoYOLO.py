import os
import shutil
import xml.etree.ElementTree as ET

# Step 1: Convert XML Annotations to YOLO Format
def convert_annotations(xml_dir, yolo_dir, classes):
    for xml_file in os.listdir(xml_dir):
        xml_path = os.path.join(xml_dir, xml_file)
        image_id = os.path.splitext(xml_file)[0]  # Extract image ID from XML filename
        yolo_path = os.path.join(yolo_dir, f"{image_id}.txt")  # Construct YOLO annotation file path
        
        try:
            with open(yolo_path, "w") as f:
                tree = ET.parse(xml_path)
                root = tree.getroot()
                size = root.find('size')
                width = int(size.find('width').text)
                height = int(size.find('height').text)

                for obj in root.findall('object'):
                    class_name = obj.find('name').text
                    if class_name not in classes:
                        continue
                    class_id = classes.index(class_name)
                    bbox = obj.find('bndbox')
                    xmin = float(bbox.find('xmin').text)
                    ymin = float(bbox.find('ymin').text)
                    xmax = float(bbox.find('xmax').text)
                    ymax = float(bbox.find('ymax').text)
                    
                    x_center = (xmin + xmax) / (2 * width)
                    y_center = (ymin + ymax) / (2 * height)
                    w = (xmax - xmin) / width
                    h = (ymax - ymin) / height
                    
                    f.write(f"{class_id} {x_center} {y_center} {w} {h}\n")
        except Exception as e:
            print(f"Error processing file {xml_file}: {e}")

dataset_dir = r'C:\Users\admin\yogaPose\data\TRAIN\trainnData'
classes = ["downdog", "goddess", "plank", "tree", "warrior2"]

# Convert annotations to YOLO format
yolo_dir = os.path.join(dataset_dir, "yolo_annotations")
os.makedirs(yolo_dir, exist_ok=True)
xml_dir = os.path.join(dataset_dir, "xml_annotations")
os.makedirs(xml_dir, exist_ok=True)
convert_annotations(xml_dir, yolo_dir, classes)
