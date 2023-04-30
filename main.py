import numpy as np
from scipy.linalg import eig
import cv2
import os
import socket

HOST = '10.30.200.147'
PORT = 5000

train_path = r"D:\SmartDoorLockFaceID\training_images"
train_images = []
labels = []
for label in os.listdir(train_path):
    label_path = os.path.join(train_path, label)
    for image_name in os.listdir(label_path):
        image_path = os.path.join(label_path, image_name)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        train_images.append(image)
        labels.append(label)
train_images = [cv2.resize(img, (25, 25)) for img in train_images]
train_data = np.array([img.flatten() for img in train_images], dtype=np.float32)
mean_face = np.mean(train_data, axis=0)
train_data -= mean_face

# cv2.imshow('mean face',train_data[1].astype(np.uint8).reshape(100,100))
# cv2.waitKey(0)

covariance = np.cov(train_data, rowvar=False)


eigenvalues, eigenvectors = eig(covariance)
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvectors = eigenvectors[:, sorted_indices]


k = 100
eigenfaces = eigenvectors[:, :k]
test_image = cv2.imread(r"D:\SmartDoorLockFaceID\test_images\test.jpg", cv2.IMREAD_GRAYSCALE)
test_image = cv2.resize(test_image, (25, 25))
test_data = test_image.flatten().astype(np.float32)
test_data -= mean_face
weights = np.dot(test_data, eigenfaces)
distances = np.linalg.norm(train_data - np.dot(weights, eigenfaces.T), axis=1)

min_index = np.argmin(distances)
print("{" + '"Name" : "{}" , "Distance" : {}'.format(labels[min_index],distances[min_index]) + "}" , end="")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    if (distances[min_index]<1000) :
        message = labels[min_index]
    else :
        message = "null"
    s.sendall(message.encode())
