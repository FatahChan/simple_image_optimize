from PIL import Image
import os

images_names = os.listdir('./input')
allowed_files = ['.jpg', '.png', '.jpeg']
images = []

for image in images_names:
    if image.endswith(tuple(allowed_files)):
        images.append(image)
    

for image in images:
    image_name = image.split('.')
    image_name = ''.join(image_name[:-1])

    img = Image.open('input/' + image)

    keep_aplha = False

    if keep_aplha == False:
        img = img.convert('RGB')

    ## hd is  1280 x 720
    ## resizing the image maintaining the aspect ratio
    if img.width > 1280 or img.height > 1280:
        img.thumbnail((1280, 1280))

    img.save(f'output/{image_name}.webp', method=6, format='webp',exact=keep_aplha, optimize=True, quality=75)