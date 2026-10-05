"""Small helpers shared by the learning demonstrations."""
import argparse
from pathlib import Path
import cv2

ROOT = Path(__file__).resolve().parent

def image_options(description, default='sample.png'):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('image', nargs='?', default=str(ROOT / default))
    parser.add_argument('--no-display', action='store_true', help='Skip GUI windows')
    parser.add_argument('--output', default=str(ROOT / 'outputs'))
    args = parser.parse_args()
    image = cv2.imread(args.image)
    if image is None:
        parser.error(f'Cannot read image: {args.image}')
    return args, image

def video_options(description, default='0'):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--source', default=default, help='Camera index or video filename')
    args = parser.parse_args()
    source = int(args.source) if args.source.isdigit() else args.source
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        cap.release()
        parser.error(f'Cannot open source: {args.source}')
    return cap

def output_dir(path):
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory
