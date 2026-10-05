"""Course-based computer vision practice; press q to exit webcam demos."""
from demo_utils import video_options
import cv2

def main():
    cap=video_options('read webcam')
    while True:
        ret,frame=cap.read()
        if not ret:
            break
        cv2.imshow('Video',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
