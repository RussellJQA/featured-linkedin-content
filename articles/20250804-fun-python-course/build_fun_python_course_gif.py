from pathlib import Path
from PIL import Image, ImageDraw, ImageFont # requires "pip install pillow" 

image_path = Path(__file__).resolve().parent / "images"

outer_box_size = (1920, 1080)
border_width = 182
divider_width = 20

inner_box_size = (outer_box_size[0] - border_width * 2, outer_box_size[1] - border_width * 2)

# Calculate the size of each image box, which is half the width of the inner box minus the divider width
# This assumes two images side by side in the inner box
image_box_size = ((inner_box_size[0] - divider_width) // 2, inner_box_size[1])

def add_title_or_caption(draw, font, text, position_x, position_y):
    bbox = draw.textbbox((0, 0), text, font=font) #
    text_size = (bbox[2] - bbox[0], bbox[3] - bbox[1])  # Calculate text size
    text_x = position_x - text_size[0] // 2 # Center horizontally
    text_y = position_y + text_size[1] // 2 # Center vertically in half of bottom border
    draw.text((text_x, text_y), text, fill=(0, 0, 255), font=font)  # Draw the text in blue (for contrast against the white background)  

def get_image_box(image, image_box_size, image_background_color, image_offset):

    image_box = Image.new('RGB', image_box_size, image_background_color)
    image_box.paste(image, image_offset) #

    return image_box

def get_images(left_image_fn, right_image_fn, title1, title2, caption1, caption2, image_background_color):

    # Get and, if needed, resize left image
    left_image = Image.open(image_path / left_image_fn)
    if left_image.size[0] > image_box_size[0] or left_image.size[1] > image_box_size[1]:
        left_image = left_image.resize(size=image_box_size)

    # Get and, if needed, resize right image
    right_image = Image.open(image_path / right_image_fn)
    if right_image.size[0] > image_box_size[0] or right_image.size[1] > image_box_size[1]:
        right_image = right_image.resize(size=image_box_size)

    # Check image sizes
    assert left_image.size == right_image.size, "Images must be the same size"
    image_size = left_image.size  # Get the size of the images to be pasted into the image boxes

    # Define the offset for the image box, which is the position where the image will be pasted within the image box
    # The offset is calculated to center the image box within the outer box
    image_offset = ((image_box_size[0] - image_size[0]) // 2, (image_box_size[1] - image_size[1]) // 2)

    # Create the image boxes for the left and right images
    # The images are resized to fit within the image box size
    image_box_a = get_image_box(left_image, image_box_size, image_background_color, image_offset)
    image_box_b = get_image_box(right_image, image_box_size, image_background_color, image_offset)

    # Create a divider between the two image boxes
    # The divider is a simple rectangle with a specified width and color
    divider_color = (0, 0, 255)  # Blue line
    divider = Image.new('RGB', (divider_width, inner_box_size[1]), divider_color)

    default_color = (255, 255, 255)  # Default color for the background = white

    # Create the inner box
    inner_box = Image.new('RGB', inner_box_size, default_color)
    inner_box.paste(image_box_a, (0, 0))
    inner_box.paste(divider, (image_box_a.width, 0))
    inner_box.paste(image_box_b, (image_box_a.width + divider.width, 0))

    # Create the outer box
    inner_box_offset = (border_width, border_width)
    outer_box = Image.new('RGB', outer_box_size, default_color)
    outer_box.paste(inner_box, inner_box_offset)

    draw = ImageDraw.Draw(outer_box)

    # Add titles and captions to the outer box
    # The titles and captions are centered above the image boxes
    # The position is calculated based on the size of the outer box and the image boxes
    
    try:
        font = ImageFont.truetype("arial.ttf", 60) # Load a font for the titles and captions
    except IOError:
        font = ImageFont.load_default() # if the specified font isn't available, use a default font

    screenshots: list[Image.Image] = []

    screenshots.append(outer_box.copy()) # Need to use a copy to avoid all screenshots list elements from being the same live instance of outer_box
    add_title_or_caption(draw, font, title1, border_width + image_box_size[0] // 2, border_width // 2)
    screenshots.append(outer_box.copy())
    add_title_or_caption(draw, font, caption1, border_width + image_box_size[0] // 2,  border_width + image_box_size[1])
    screenshots.append(outer_box.copy())
    add_title_or_caption(draw, font, title2, border_width + image_box_a.width + divider.width + image_box_size[0] // 2, border_width // 2)
    screenshots.append(outer_box.copy())
    add_title_or_caption(draw, font, caption2, border_width + image_box_a.width + divider.width + image_box_size[0] // 2,  border_width + image_box_a.height)
    screenshots.append(outer_box.copy())

    return screenshots

if __name__ == "__main__":

    screenshots: list[Image.Image] = []
    
    # Image of a Jupyter notebook which asks an LLM about the "Zen of Python", is titled "Free, Fun, AI-Focused Introduction to Python?", and is captioned "Yes"
    screenshots.append(Image.open(image_path / "coverSlide.png"))

    # Image of a Jupyter notebook which asks an LLM to create a sonnet, is titled "Taught by Google's 'cat man'? - Yes and No",
    # and is captioned "AI Python for Beginners: Taught by Andrew Ng"
    screenshots.append(Image.open(image_path / "sonnetSlide.png"))

    # "#ADD8E6" is the hex code for "light blue", the background color which I'd specified when I prompted ChatGPT to create the images below
    screenshots += get_images("dog.png", "cat.png", "Is this a cat? - No", "Is this a cat? - Yes", "dog", "cat", "#ADD8E6")
    screenshots += get_images("salmon.png", "catfish.png",  "Is this a cat? - No", "Is this a cat? - Yes and No", "salmon", "catfish", "#ADD8E6")
    screenshots += get_images("canoe.png", "catamaran.png", "Is this a cat? - No", "Is this a cat? - Yes and No", "canoe", "catamaran", "#ADD8E6")
    screenshots += get_images("xray.png", "catscan.png", "Is this a cat? - No", "Is this a cat? - Yes and No", "X-ray machine", "CAT scan machine", "#ADD8E6")

    screenshots.append(Image.open(image_path / "myCourseCertificate.png")) # A screenshot of my course certificate

    
    blank_frame = Image.new('RGB', screenshots[0].size, (255, 255, 255)) # Append a final blank, white frame to the GIF
    screenshots.append(blank_frame)

    # Display the 2 initial slides for 5 seconds (5,000 ms) and each of the remaining images for 2 seconds (2,000 ms)
    durations = 2 * [5_000] + 22 * [2_000]

    screenshots[0].save( # Save the 2 initial slides and all 4 stages of each of the titled/captioned composite screenshots together as 1 animated GIF
        image_path / "fun-python-course.gif",
        save_all=True,
        append_images=screenshots[1:],
        duration=durations,
        loop=0 # 0 == Loop indefinitely
    )
