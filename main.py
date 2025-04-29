from PIL import Image, ImageFilter
import sys

def convert_to_black_and_white(image_path, output_path):
    try:
        # Open the image
        with Image.open(image_path) as img:
            # Convert to grayscale
            img = img.convert('L')
            # Resize to 25x25 while keeping aspect ratio and adding borders
            img.thumbnail((25, 25))
            # Create a new image with white background
            bordered_img = Image.new('L', (25, 25), 255)
            paste_position = ((25 - img.size[0]) // 2, (25 - img.size[1]) // 2)
            bordered_img.paste(img, paste_position)

            # Detect edges to outline borders
            bordered_img = bordered_img.filter(ImageFilter.FIND_EDGES)
            # Convert to black and white (binary)
            bordered_img = bordered_img.convert('1')

            # Save the result
            bordered_img.save(output_path)
            print(f"Image successfully converted and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_image_path> <output_image_path>")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        convert_to_black_and_white(input_path, output_path)