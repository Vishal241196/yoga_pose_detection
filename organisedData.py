# Organize Dataset
def organize_dataset(dataset_dir, classes):
    images_dir = os.path.join(dataset_dir, "images")
    labels_dir = os.path.join(dataset_dir, "labels")
    train_dir = os.path.join(images_dir, "train")
    val_dir = os.path.join(images_dir, "val")
    train_labels_dir = os.path.join(labels_dir, "train")
    val_labels_dir = os.path.join(labels_dir, "val")

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(train_labels_dir, exist_ok=True)
    os.makedirs(val_labels_dir, exist_ok=True)

    image_files = os.listdir(dataset_dir)
    num_images = len(image_files)
    num_train_images = int(0.8 * num_images)
    train_images = image_files[:num_train_images]
    val_images = image_files[num_train_images:]

    for image_file in train_images:
        if image_file.endswith(('.jpg', '.jpeg', '.png')):
            label_file = os.path.splitext(image_file)[0] + ".txt"
            shutil.copy(os.path.join(dataset_dir, image_file), train_dir)
            shutil.copy(os.path.join(dataset_dir, label_file), train_labels_dir)

    for image_file in val_images:
        if image_file.endswith(('.jpg', '.jpeg', '.png')):
            label_file = os.path.splitext(image_file)[0] + ".txt"
            shutil.copy(os.path.join(dataset_dir, image_file), val_dir)
            shutil.copy(os.path.join(dataset_dir, label_file), val_labels_dir)


# Define your dataset directory and classes
dataset_dir = r'C:\Users\admin\yogaPose\data\TRAIN\trainnData\\yolo_annotations'
classes = ["downdog", "goddess", "plank", "tree", "warrior2"]

# Organize dataset
organize_dataset(dataset_dir, classes)