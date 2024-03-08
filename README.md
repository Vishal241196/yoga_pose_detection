# yoga_pose_detection

## Overview
1. Purpose:
This project aims to create an AI tool capable of detecting yoga poses in images with high accuracy. It serves as a valuable resource for yoga enthusiasts and instructors, providing instant feedback on pose correctness and alignment.

2. Technology:
YOLO v5: State-of-the-art object detection model, chosen for its efficiency and accuracy.
Flask: Used to build a web API for seamless integration into web applications.
HTML: Developed a user-friendly interface for uploading images and viewing detection results.

## Project Structure
1. Dependencies: Detailed list of libraries and frameworks used in the project setup.
2. Setup and Usage: Instructions on how to set up and use the project locally.
3. Example: A demonstration of the project in action, showcasing its capabilities.
4. Credits: Acknowledgment of any third-party resources or contributions.

## Challenges: 
- Overcame various challenges during model training and deployment, including dataset preparation and model optimization.

## Solutions:
- Implemented effective solutions to address challenges, resulting in a robust and accurate yoga pose detection system.

- I fine-tuned the YOLOv5 object detection model on five yoga pose classes: "Downdog", "Tree", "Plank", "Goddess", and "Warrior2". With a validation accuracy of over 90%, the model demonstrates remarkable performance in accurately identifying yoga poses.

- My Flask API, implemented in app.py, provides seamless integration for web applications. The frontend comprises index.html, featuring image selection and upload functionality, and prediction.html, displaying detection results and enabling users to upload additional images.
