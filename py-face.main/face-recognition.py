import cv2
import face_recognition
import os
from datetime import datetime

# Initialize the video capture object to use the camera.
video_capture = cv2.VideoCapture(1)

# Set the frames per second to 60
video_capture.set(cv2.CAP_PROP_FPS, 60)

# Create the snapshots directory if it doesn't exist
snapshots_dir = os.path.expanduser('~/Downloads/snapshots-faceproject')
os.makedirs(snapshots_dir, exist_ok=True)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color
    rgb_frame = frame[:, :, ::-1]

    # Convert the image to black and white
    gray_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2GRAY)

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(gray_frame)

    # Display the results and take a snapshot if faces are detected
    for top, right, bottom, left in face_locations:
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 255), 2)

        # Take a snapshot
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        snapshot_filename = os.path.join(snapshots_dir, f'face_{timestamp}.png')
        face_image = frame[top:bottom, left:right]
        cv2.imwrite(snapshot_filename, face_image)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture when everything is done
video_capture.release()
cv2.destroyAllWindows()
