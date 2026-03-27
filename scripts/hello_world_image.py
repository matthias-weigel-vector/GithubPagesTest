from PIL import Image, ImageDraw, ImageFont

# Create an image with white background
img = Image.new('RGB', (200, 100), color='white')

# Create Draw object
d = ImageDraw.Draw(img)

# Optionally, you can specify a font and size
# font = ImageFont.truetype("arial.ttf", 15)

# Add text to image
d.text((10, 40), "Hello World", fill="black")  # Use fill to set the color of the text

# Save the image
img.save('_site/hello_world.png')
