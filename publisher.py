from kafka import KafkaProducer
import cv2
import time
import json

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Function to encode video frames before sending
def encode_frame(frame):
    _, buffer = cv2.imencode('.jpg', frame)
    return buffer.tobytes()

# Capture video from file
video_file_path = 'F:/ibrahim/altersource/test_video.mp4'
cap = cv2.VideoCapture(video_file_path)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Send frame to Kafka topic
    producer.send('video-topic', encode_frame(frame))
    time.sleep(0.02)  # to simulate approximately real-time frame rate

cap.release()
producer.close()
