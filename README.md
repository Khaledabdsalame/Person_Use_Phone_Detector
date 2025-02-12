![download](https://github.com/user-attachments/assets/c4360a56-5253-4d6e-92d2-372f44b8fe03)
# Introduction :
Real-Time Phone Usage Detection with YOLOv10
Welcome to the Real-Time Phone Usage Detection repository! This project leverages the power of YOLOv10, a state-of-the-art object detection model, to detect and monitor phone usage by individuals in real-time using a webcam feed. The system is designed to identify when a person is using a phone by analyzing the spatial relationship between detected persons and phones in the video stream.

**This repository provides a complete implementation, including:**

Real-time object detection using YOLOv10.
     
Overlap detection between person and phone bounding boxes.
     
Customizable video capture resolution for optimal performance.
     
Easy-to-use scripts for deployment and testing.

Whether you're building a surveillance system, a productivity monitoring tool, or just exploring computer vision applications, this project serves as a robust starting point for detecting phone usage in real-time
# Key Features :

- **Real-Time Detection:** Detects phone usage in live video streams with high accuracy.
- **Customizable Resolution:** Supports adjustable video capture resolution for compatibility with various cameras.
- **Overlap Detection:** Uses bounding box overlap logic to determine if a person is using a phone.
- **Lightweight and Efficient:** Built with YOLOv10 for fast and efficient inference.
- **Easy to Use:** Simple setup and deployment process with detailed instructions.
# Uses Case :
- **Surveillance Systems:** Monitor phone usage in restricted areas.
- **Productivity Monitoring:** Track phone usage in workplaces or classrooms.
# Installation :
**Clone the repository:**
```bash
git clone https://github.com/Khaledabdsalame/Person_Use_Phone_Detector.git
cd Person_Use_Phone_Detector
```
**Install:**
```bash
pip install -r requirements.txt
```
**Usage:**
- Run the script to start real-time detection:
```bash
python OpenCv_Phone_Detector.py
```
- Adjust the video capture resolution in the script if needed.
- Press q to exit the application.
# Licence :
MIT License Copyright (c) Khaled Abdsalame From [CSA Team](https://github.com/CSA-club)


