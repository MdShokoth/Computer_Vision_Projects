"""Course-based computer vision practice; press q to exit webcam demos."""
import cv2
import numpy as np

def main():
    canvas=np.zeros((512,512,3),dtype=np.uint8)
    cv2.line(canvas,(0,0),(511,511),(0,255,0),15)
    cv2.rectangle(canvas,(100,0),(300,150),(255,0,0),-1)
    cv2.putText(canvas,"Opencv Practice",(10,500),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    cv2.imshow("Canvas with shape",canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
