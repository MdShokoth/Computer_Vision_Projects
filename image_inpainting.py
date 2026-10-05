"""Pretrained Stable Diffusion inpainting; white mask pixels select replacement."""
import argparse
from PIL import Image
import torch
from diffusers import StableDiffusionInpaintPipeline
from demo_utils import output_dir

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('image')
    parser.add_argument('mask')
    parser.add_argument('--prompt', default='A landscape with trees, grass, a path and sky')
    parser.add_argument('--output', default='outputs/inpainting')
    parser.add_argument('--device', choices=['cpu', 'cuda'], default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--seed', type=int, default=42)
    args = parser.parse_args()
    if args.device == 'cuda' and not torch.cuda.is_available():
        parser.error('CUDA requested but unavailable')
    dtype = torch.float16 if args.device == 'cuda' else torch.float32
    pipe = StableDiffusionInpaintPipeline.from_pretrained('runwayml/stable-diffusion-inpainting', torch_dtype=dtype)
    pipe.to(args.device)
    image = Image.open(args.image).convert('RGB').resize((512, 512))
    mask = Image.open(args.mask).convert('L').resize((512, 512), Image.Resampling.NEAREST)
    generator = torch.Generator(device=args.device).manual_seed(args.seed)
    result = pipe(prompt=args.prompt, image=image, mask_image=mask, generator=generator).images[0]
    target = output_dir(args.output) / 'inpainted_image.png'
    result.save(target)
    print(f'Saved {target}')

if __name__ == '__main__':
    main()
