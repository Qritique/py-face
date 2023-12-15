import face_recognition
import os
import shutil
from sklearn.cluster import DBSCAN

def sort_faces_into_folders(image_folder_path, output_folder_path):
    # Check if the output folder exists, create if it doesn't
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # Load all the images and get their face encodings
    image_paths = [os.path.join(image_folder_path, img) for img in os.listdir(image_folder_path) if img.lower().endswith(('.jpg', '.jpeg', '.png'))]
    face_encodings = []
    for path in image_paths:
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            face_encodings.append(encodings[0])

    # Cluster the face encodings
    if face_encodings:
        clustering_model = DBSCAN(eps=0.5, min_samples=3, metric="euclidean")
        clustering_model.fit(face_encodings)
        labels = clustering_model.labels_
        
        # Create a folder for each person and move images
        for label, path in zip(labels, image_paths):
            if label == -1:
                # Outliers, which couldn't be clustered
                folder_name = "unknown"
            else:
                folder_name = f"person{label + 1}"
            
            # Create folder if it doesn't exist
            person_folder = os.path.join(output_folder_path, folder_name)
            if not os.path.exists(person_folder):
                os.makedirs(person_folder)
            
            # Move image to the respective folder
            shutil.move(path, os.path.join(person_folder, os.path.basename(path)))

# Usage
sort_faces_into_folders('/Users/user/Downloads/snapshots-faceproject', '/Users/user/Downloads/snapshots-faceproject/sorted')
