from kafka import KafkaConsumer
import cv2
import numpy as np

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'video-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='video-display')

# Function to decode video frames received
def decode_frame(frame):
    nparr = np.frombuffer(frame, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

# Display the video
for message in consumer:
    frame = decode_frame(message.value)
    cv2.imshow('Video Stream', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
