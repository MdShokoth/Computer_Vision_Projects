"""Play a supplied video; the default video is a synthetic moving-shape example."""
import cv2
from demo_utils import ROOT, video_options

def main():
    cap = video_options('Play a video', str(ROOT / 'sample_video.avi'))
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            cv2.imshow('Video — q to quit', frame)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
