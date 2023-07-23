import streamlit as st
from streamlit_webrtc import webrtc_streamer, MediaStreamConstraints
from streamlit_webrtc.config import MediaTrackConstraints, VideoHTMLAttributes
import mediapipe as mp
import av
import cv2
from streamlit.runtime.scriptrunner import add_script_run_ctx
from pygame import mixer

st.set_page_config(page_title="Low-Fi Nance Band - Drums", page_icon="🎸", layout="wide")
st.title("Low-Fi Nance Band")
st.subheader("Drums")
st.text(
    "March to the beat of your own rhythm on our virtual drums and create musical masterpieces with every strike!"
)

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=2, min_detection_confidence=0.8)
mpDraw = mp.solutions.drawing_utils

isPlaying = False
drums_text = ""

mixer.init()
drum_clap = mixer.Sound("src/assets/drums/hatt.wav")
drum_snare = mixer.Sound("src/assets/drums/snare.mp3")


def video_frame_callback(frame):
    global isPlaying, drums_text

    add_script_run_ctx(ctx=frame)
    img = frame.to_ndarray(format="bgr24")
    frame = cv2.flip(img, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    drums = cv2.imread("src/assets/drums/drums.png")
    drums_box = cv2.rectangle(frame, (0, 0), (115, 50), (0, 0, 255), 1)
    cv2.putText(
        drums_box,
        drums_text,
        (10, 35),
        cv2.FONT_HERSHEY_PLAIN,
        2,
        (255, 255, 255),
        2,
    )
    cv2.addWeighted(drums, 1, frame, 0.7, 0, frame)
    result = hands.process(framergb)
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for id, lm in enumerate(handslms.landmark):
                lmx = int(lm.x * 640)
                lmy = int(lm.y * 480)
                landmarks.append([lmx, lmy, id])
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
        index_finger_1 = landmarks[8]
        if len(landmarks) > 21:
            index_finger_2 = landmarks[29]
        else:
            index_finger_2 = [0, 0]
        if (
            (
                index_finger_2[0] >= 440
                and index_finger_2[0] < 550
                and index_finger_2[1] >= 270
                and index_finger_2[1] < 330
            )
            or (
                index_finger_1[0] >= 440
                and index_finger_1[0] < 550
                and index_finger_1[1] >= 270
                and index_finger_1[1] < 330
            )
        ) and (not isPlaying):
            isPlaying = True
            drums_text = "Snare"
            drum_snare.play()
        elif (
            (
                index_finger_2[0] >= 70
                and index_finger_2[0] < 180
                and index_finger_2[1] >= 300
                and index_finger_2[1] < 360
            )
            or (
                index_finger_1[0] >= 70
                and index_finger_1[0] < 180
                and index_finger_1[1] >= 300
                and index_finger_1[1] < 360
            )
        ) and (not isPlaying):
            isPlaying = True
            drums_text = "Clap"
            drum_clap.play()
        elif (
            (
                (
                    index_finger_2[0] < 70
                    or (index_finger_2[0] >= 180 and index_finger_2[0] < 440)
                    or index_finger_2[0] >= 550
                )
                and (
                    index_finger_2[1] < 300
                    or (index_finger_2[1] >= 360 and index_finger_2[1] < 270)
                    or index_finger_2[1] >= 330
                )
            )
            and (
                (
                    index_finger_1[0] < 70
                    or (index_finger_1[0] >= 180 and index_finger_1[0] < 440)
                    or index_finger_1[0] >= 550
                )
                and (
                    index_finger_1[1] < 300
                    or (index_finger_1[1] >= 360 and index_finger_1[1] < 270)
                    or index_finger_1[1] >= 330
                )
            )
            and isPlaying
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
