"""Read and copy an image. An included synthetic sample is used by default."""
import cv2
from demo_utils import image_options, output_dir

def main():
    args, image = image_options('Read and copy an image')
    target = output_dir(args.output) / 'image_copy.png'
    cv2.imwrite(str(target), image)
    print(f'Saved {target}')
    if not args.no_display:
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
