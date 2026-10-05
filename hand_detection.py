"""Course-based computer vision practice; press q to exit webcam demos."""
from demo_utils import video_options
import cv2
from cvzone.HandTrackingModule import HandDetector

def main():
    detector=HandDetector(detectionCon=0.8,maxHands=2)
    cap=video_options('hand detection')
    while True:
        ret,frame=cap.read()
        if not ret:
            break
        hands,frame = detector.findHands(frame)
        if hands:
            hand1=hands[0]
            lmList1=hand1['lmList']
            handType1=hand1['type']
        cv2.imshow('Hand Detection',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
