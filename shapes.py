"""Find triangular and quadrilateral contours in an image."""
import cv2
import numpy as np
from cvzone import findContours
from demo_utils import image_options, output_dir

def main():
    args, image = image_options('Shape and contour detection')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 100, 200)
    dilated = cv2.dilate(canny, np.ones((5, 5), np.uint8), iterations=1)
    contours_image, found = findContours(image, dilated, filter=[3, 4], drawCon=True)
    for contour in found:
        print('Bounding box:', contour['bbox'])
    if not found:
        print('No matching contours found.')
    target = output_dir(args.output) / 'shape_contours.png'
    cv2.imwrite(str(target), contours_image)
    if not args.no_display:
        cv2.imshow('Shape contours', contours_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
