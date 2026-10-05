"""Course-based computer vision practice; press q to exit webcam demos."""
from demo_utils import video_options
import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
from cvzone import findContours

def main():

    cap=video_options('color contour detection')
    myColorFinder=ColorFinder(trackBar=False)
    hsvVal={'hmin': 17, 'smin': 29, 'vmin': 93, 'hmax': 72, 'smax': 98, 'vmax': 144}
    while True:
        ret,frame=cap.read()
        if not ret:
            break
        imgColor,mask=myColorFinder.update(frame, hsvVal)
        imgContours, conFound =findContours(frame,mask)
        if conFound:
            print(conFound[0]['center'])
        imgStack=cvzone.stackImages([frame,imgColor,mask, imgContours],4,0.5)  
        cv2.imshow('Color Detection',imgStack)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
