"""OCR with regions using Florence-2. Downloads pretrained model files."""
import argparse
from pathlib import Path
from PIL import Image
from transformers import AutoModelForCausalLM, AutoProcessor
from demo_utils import ROOT

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('image', nargs='?', default=str(ROOT / 'sample.png'))
    parser.add_argument('--model', default='microsoft/Florence-2-base')
    args = parser.parse_args()
    image = Image.open(args.image).convert('RGB')
    model = AutoModelForCausalLM.from_pretrained(args.model, trust_remote_code=True)
    processor = AutoProcessor.from_pretrained(args.model, trust_remote_code=True)
    inputs = processor(text='<OCR_WITH_REGION>', images=image, return_tensors='pt')
    outputs = model.generate(**inputs, max_new_tokens=1024)
    text = processor.batch_decode(outputs, skip_special_tokens=False)[0]
    results = processor.post_process_generation(text, task='<OCR_WITH_REGION>', image_size=image.size)
    for label, box in zip(results['<OCR_WITH_REGION>']['labels'], results['<OCR_WITH_REGION>']['quad_boxes']):
        print(label.replace('</s>', '').strip(), box)

if __name__ == '__main__':
    main()
