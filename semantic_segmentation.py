"""Pretrained Mask2Former semantic-segmentation demonstration."""
import argparse
from PIL import Image
from transformers import pipeline
from demo_utils import output_dir

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('image', help='Path to your scene photograph')
    parser.add_argument('--output', default='outputs/segmentation')
    args = parser.parse_args()
    image = Image.open(args.image).convert('RGB')
    pipe = pipeline(task='image-segmentation', model='facebook/mask2former-swin-large-ade-semantic')
    directory = output_dir(args.output)
    for index, segment in enumerate(pipe(image)):
        label = segment['label']
        score = segment.get('score')
        print(f'{label}: {score}' if score is not None else label)
        safe_label = ''.join(c if c.isalnum() else '_' for c in label)
        segment['mask'].save(directory / f'{index:03d}_{safe_label}.png')

if __name__ == '__main__':
    main()
