### Step 1: Set Up the Environment
```bash
pip install redis kafka-python opencv-python
```

### Step 2: Run the Code and Present
1. Make sure Kafka and a Kafka server are running on your local machine. This typically involves downloading Kafka, extracting it, and running the `zookeeper-server-start` and `kafka-server-start` scripts.
2. Execute the `publisher.py` script to start sending the video frames to Kafka.
3. Run the `subscriber.py` script to receive the video frames and display them.