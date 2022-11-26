from streamlit_webrtc import webrtc_streamer
import av
import cv2

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


class VideoProcessor:
    def recv(self, frame):
        frm = frame.to_ndarray(format="bgr24")
        
        CONFIDENCE = 0.5
        SCORE_THRESHOLD = 0.5
        IOU_THRESHOLD = 0.5
        font = cv2.FONT_HERSHEY_COMPLEX
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        rand_lvl = [random.randrange(70, 100) for i in range(0, 50)]
        frame_cntr = 0
        while True:

            ret, frame = frm
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            i = 0
            for (x, y, z, h) in faces:
                frame_cntr += 1

                cv2.rectangle(frm, (x, y), (x + z, y + h), (255, 0, 0), 2)
                if frame_cntr < 100:
                    cv2.putText(frame, f'Вы junior-разработчик на:{random.randrange(0, 100)}%', (x - 6, y), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
                else:
                    i += 1
                    cv2.putText(frame, f'Вы junior-разработчик на:{rand_lvl[i]}%', (x - 6, y), font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)


            x, imag = cv2.imencode('.jpg', frame)

            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + imag.tobytes() + b'\r\n\r\n')

            for x, y, w, h in faces:
                cv2.rectangle(frm, (x, y), (x + w, y + h), (0, 255, 0), 3)

            return av.VideoFrame.from_ndarray(frm, format='bgr24')


webrtc_streamer(key="key", video_processor_factory=VideoProcessor)
