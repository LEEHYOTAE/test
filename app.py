import streamlit as st
import cv2
from PIL import Image
import numpy as np
import torch
from ultralytics import YOLO

def main():
    st.title("웹캠 실시간 스트리밍")

    # 웹캠에서 영상을 캡처하기 위한 OpenCV VideoCapture 객체 생성
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("웹캠을 열 수 없습니다.")
        return

    # Streamlit에 실시간으로 영상 표시
    video_placeholder = st.empty()

    while True:
        # 웹캠에서 프레임 읽기
        ret, frame = cap.read()

        # 프레임이 제대로 읽혔는지 확인
        if not ret:
            st.error("프레임을 읽을 수 없습니다.")
            break

        # BGR 프레임을 RGB로 변환
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Streamlit에 video 요소로 표시
        video_placeholder.image(rgb_frame, channels="RGB", use_column_width=True)

    # 사용이 끝난 후 웹캠 해제
    cap.release()

if __name__ == "__main__":
    main()