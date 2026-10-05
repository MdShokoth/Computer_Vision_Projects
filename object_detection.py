"""YOLO webcam/video inference using the supplied checkpoint; no training claim."""
import argparse
from pathlib import Path
import cv2
from ultralytics import YOLO
from demo_utils import ROOT

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', default=str(ROOT / 'best.pt'))
    parser.add_argument('--source', default='0')
    parser.add_argument('--confidence', type=float, default=.25)
    args = parser.parse_args()
    if not Path(args.model).is_file():
        parser.error(f'Missing checkpoint: {args.model}')
    model = YOLO(args.model)
    source = int(args.source) if args.source.isdigit() else args.source
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        cap.release()
        parser.error(f'Cannot open source: {args.source}')
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            results = model(frame, conf=args.confidence, verbose=False)
            annotated = results[0].plot()
            cv2.imshow('Object detection — q to quit', annotated)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
