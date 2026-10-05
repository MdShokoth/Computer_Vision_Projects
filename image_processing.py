"""Resize, grayscale, blur, and detect edges; save a labeled contact sheet."""
import cv2
import numpy as np
from demo_utils import image_options, output_dir

def build_views(image):
    resized = cv2.resize(image, (400, 300))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(resized, (7, 7), 0)
    edges = cv2.Canny(resized, 100, 200)
    views = [('Original / resized', resized), ('Grayscale', gray),
             ('Gaussian blur', blur), ('Canny edges', edges)]
    tiles = []
    for label, view in views:
        if view.ndim == 2:
            view = cv2.cvtColor(view, cv2.COLOR_GRAY2BGR)
        tile = np.zeros((340, 400, 3), np.uint8)
        tile[:300] = view
        cv2.putText(tile, label, (14, 325), cv2.FONT_HERSHEY_SIMPLEX, .65, (255, 255, 255), 1)
        tiles.append(tile)
    return np.vstack((np.hstack(tiles[:2]), np.hstack(tiles[2:])))

def main():
    args, image = image_options('Image processing contact sheet')
    sheet = build_views(image)
    target = output_dir(args.output) / 'image_processing.png'
    cv2.imwrite(str(target), sheet)
    print(f'Saved {target}')
    if not args.no_display:
        cv2.imshow('Image processing', sheet)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
