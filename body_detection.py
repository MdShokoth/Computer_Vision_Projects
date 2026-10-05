"""Course-based computer vision practice; press q to exit webcam demos."""
from demo_utils import video_options
import cv2
from cvzone.PoseModule import PoseDetector

def main():
    detector=PoseDetector()
    cap=video_options('body detection')
    while True:
        ret,frame=cap.read()
        if not ret:
            break
        frame = detector.findPose(frame)
        llmList, bboxInfo = detector.findPosition(frame)
        if bboxInfo:
            center=bboxInfo['center']
        cv2.imshow('Body Detection',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
