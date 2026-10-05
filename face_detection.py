"""Course-based computer vision practice; press q to exit webcam demos."""
from demo_utils import video_options
import cv2
from cvzone.FaceDetectionModule import FaceDetector

def main():
    detector=FaceDetector()
    cap=video_options('face detection')
    while True:
        ret,frame=cap.read()
        if not ret:
            break
        frame, bboxs = detector.findFaces(frame)
        if bboxs:
            center=bboxs[0]['center']
        cv2.imshow('Face Detection',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
