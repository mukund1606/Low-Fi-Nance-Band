import streamlit as st
from streamlit_webrtc import webrtc_streamer, MediaStreamConstraints
from streamlit_webrtc.config import MediaTrackConstraints, VideoHTMLAttributes
import mediapipe as mp
import av
import cv2
from streamlit.runtime.scriptrunner import add_script_run_ctx
from pygame import mixer

st.set_page_config(
    page_title="Low-Fi Nance Band - Guitar", page_icon="🎸", layout="wide"
)
st.title("Low-Fi Nance Band")
st.subheader("Guitar")
st.text(
    "Unleash your inner rockstar on our virtual guitar and let the music flow from your fingertips!"
)

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.8)
mpDraw = mp.solutions.drawing_utils

isPlaying = False

mixer.init()
e2 = mixer.Sound("src/assets/guitar/e2.mp3")
a2 = mixer.Sound("src/assets/guitar/a2.mp3")
d3 = mixer.Sound("src/assets/guitar/d3.mp3")
g3 = mixer.Sound("src/assets/guitar/g3.mp3")
b3 = mixer.Sound("src/assets/guitar/b3.mp3")
e4 = mixer.Sound("src/assets/guitar/e4.mp3")


string_text = ""


def video_frame_callback(frame):
    global isPlaying, string_text

    add_script_run_ctx(ctx=frame)
    guitar_image = cv2.imread("src/assets/guitar/guitar.png")
    img = frame.to_ndarray(format="bgr24")
    frame = cv2.flip(img, 1)
    string_box = cv2.rectangle(frame, (0, 0), (60, 50), (0, 0, 255), 1)
    cv2.putText(
        string_box,
        string_text,
        (10, 35),
        cv2.FONT_HERSHEY_PLAIN,
        2,
        (255, 255, 255),
        2,
    )
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.addWeighted(guitar_image, 1, frame, 0.7, 0, frame)

    result = hands.process(framergb)
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * 640)
                lmy = int(lm.y * 480)

                landmarks.append([lmx, lmy])
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
        index_finger = landmarks[8]
        if not isPlaying:
            if index_finger[1] >= 192 and index_finger[1] <= 197:
                isPlaying = True
                string_text = "E2"
                e2.play()
            elif index_finger[1] >= 207 and index_finger[1] <= 212:
                isPlaying = True
                string_text = "A2"
                a2.play()
            elif index_finger[1] >= 220 and index_finger[1] <= 225:
                isPlaying = True
                string_text = "D3"
                d3.play()
            elif index_finger[1] >= 235 and index_finger[1] <= 240:
                isPlaying = True
                string_text = "G3"
                g3.play()
            elif index_finger[1] >= 245 and index_finger[1] <= 250:
                isPlaying = True
                string_text = "B3"
                b3.play()
            elif index_finger[1] >= 260 and index_finger[1] <= 265:
                isPlaying = True
                string_text = "E4"
                e4.play()
        else:
            if (
                index_finger[1] < 192
                or (index_finger[1] > 197 and index_finger[1] < 207)
                or (index_finger[1] > 212 and index_finger[1] < 220)
                or (index_finger[1] > 225 and index_finger[1] < 235)
                or (index_finger[1] > 240 and index_finger[1] < 245)
                or (index_finger[1] > 250 and index_finger[1] < 260)
                or index_finger[1] > 265
            ):
                isPlaying = False

    return av.VideoFrame.from_ndarray(frame, format="bgr24")


self_ctx = webrtc_streamer(
    key="self",
    video_frame_callback=video_frame_callback,
    media_stream_constraints=MediaStreamConstraints(
        audio=False,
        video=MediaTrackConstraints(
            aspectRatio=1.3333333333333333,
            facingMode="user",
            frameRate=60,
            height=480,
            latency=0.0,
            width=640,
        ),
    ),
    video_html_attrs=VideoHTMLAttributes(
        controls=False, autoPlay=True, style={"width": "100%"}
    ),
)
