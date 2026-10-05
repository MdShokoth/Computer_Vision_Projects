"""Consecutive-frame motion detection, not person or intruder identification."""
import argparse
from pathlib import Path
import cv2
import numpy as np
from demo_utils import ROOT, output_dir

def motion_regions(previous_gray, current_gray, min_area=1000):
    difference = cv2.absdiff(previous_gray, current_gray)
    _, mask = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boxes = [cv2.boundingRect(c) for c in contours if cv2.contourArea(c) >= min_area]
    return boxes

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', default='0', help='Camera index or video filename')
    parser.add_argument('--min-area', type=float, default=1000)
    parser.add_argument('--no-display', action='store_true')
    parser.add_argument('--save', action='store_true', help='Opt in to saving motion frames')
    parser.add_argument('--output', default=str(ROOT / 'outputs' / 'motion'))
    parser.add_argument('--max-frames', type=int, default=0, help='0 means until EOF or quit')
    args = parser.parse_args()
    source = int(args.source) if args.source.isdigit() else args.source
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        cap.release()
        parser.error(f'Cannot open source: {args.source}')
    previous = None
    frame_count = detected_count = 0
    directory = output_dir(args.output) if args.save else None
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            frame_count += 1
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            boxes = motion_regions(previous, gray, args.min_area) if previous is not None else []
            previous = gray.copy()
            for x, y, w, h in boxes:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if boxes:
                detected_count += 1
                cv2.putText(frame, 'Motion detected', (10, 35), cv2.FONT_HERSHEY_SIMPLEX, .8, (0, 0, 255), 2)
                if directory is not None:
                    cv2.imwrite(str(directory / f'motion_{frame_count:06d}.jpg'), frame)
            if not args.no_display:
                cv2.imshow('Motion detection — q or Esc to quit', frame)
                if cv2.waitKey(1) & 0xFF in (ord('q'), 27):
                    break
            if args.max_frames and frame_count >= args.max_frames:
                break
    finally:
        cap.release()
        if not args.no_display:
            cv2.destroyAllWindows()
    print(f'Processed {frame_count} frames; motion in {detected_count} frames.')

if __name__ == '__main__':
    main()
