# Py-Face 🔍 , open-source face recognition. 

### Requirements:
1. **Operating System:** macOS or Linux
2. **Python Libraries:** `cv2`, `face_recognition`, `os`, `datetime`
3. **Directory:** Create a directory named `snapshots-faceproject` in your Downloads folder.

### Setup Instructions:
1. **Install Required Libraries:**
    - To install `cv2` and `face_recognition`, run:
        ```
        pip install opencv-python-headless
        pip install face_recognition
        ```
    - `os` and `datetime` should import natively, if they don't follow PyPi.org

2. **Set Up the Directory:**
    - Create a directory named `snapshots-faceproject` in your Downloads folder. This directory will store the captured snapshots.

3. **Run the Script:**
    - Copy the provided Python code into a file, say `main.py`.
    - Open a terminal and navigate to the directory containing `main.py`.
    - Run the script using Python:
        ```
        python main.py
        ```

### Disclaimer:
- This script only works on macOS and Linux systems.
- Ensure that your camera is correctly connected and functional.
- Make sure the `snapshots-faceproject` directory exists and is accessible for writing.
- Edit `cv2.VideoCapture(num)` num to your camera's order in a webcam list.

### Instructions:
- When the script is executed, it will access your camera (specified as `cv2.VideoCapture(1)`).
- The script captures the video feed and detects faces in real-time.
- Detected faces will be framed with a rectangle on the live video feed.
- If a face is detected, the script will capture and save a snapshot of the detected face in the `snapshots-faceproject` directory with a timestamp.

### Notes:
- Press 'q' on the keyboard to quit the script.
- Adjust the camera index in `cv2.VideoCapture()` if you have multiple cameras.
- Ensure necessary permissions for accessing the camera and writing to the specified directory.
