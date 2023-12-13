import streamlit as st
import cv2
import mediapipe as mp

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture(0)
up = False
counter = 0
count = 0
position = None
counter_bench_press = 0
bench_press_up = False
bench_press_down = False
counter_legs = 0
legs_up = False
legs_down = False
counter_curl = 0
curl_up = False
curl_down = False
counter_triceps = 0
triceps_up = False
triceps_down = False

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        points = {}
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            points[id] = (cx, cy)

        cv2.circle(img, points[12], 15, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, points[14], 15, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, points[11], 15, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, points[13], 15, (255, 0, 0), cv2.FILLED)

        # Your existing code for pose analysis and exercise detection

        # Display the counter on the Streamlit app
        st.write(f"Counter: {counter}")

        # Display the OpenCV image in Streamlit
        st.image(img, channels="RGB", use_column_width=True)

# You can add Streamlit UI elements and controls here if needed
