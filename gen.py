from PIL import Image, ImageOps

base = Image.new('RGBA', (512,512), 'white')

layer1 = Image.open("star.png")
layer2 = Image.open("horse.png")


# Step 1: Resize largest dimension of all inputs down to 512x512
# Step 2: expand image to 512x512 in the event it is not square

layer1 = layer1.resize((512, 512), Image.ANTIALIAS)
layer2 = layer2.resize((512, 512), Image.ANTIALIAS)
layer1 = layer1.rotate(45)
layer2 = layer2.rotate(45)

a = Image.alpha_composite(base, layer1)
b = Image.alpha_composite(a, layer2)
b.show()

# getbbox to get bounding box around objects in images

# ImageOps.crop / expand for zooming
# ImageDraw.Draw.text multiline_text https://pillow.readthedocs.io/en/3.3.x/reference/ImageDraw.html

#translate
# create blank alpha image of same size as original
# movex: copy create large rectangle exluding some number of pixels on either side in x
#        paste the image in the new image thereby translating it in x
# http://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html#rolling-an-image


# Ops
# Zoom
# Translate
# Rotate
