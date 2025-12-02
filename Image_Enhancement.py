from PIL import Image, ImageEnhance

def enhance_image(image_path, output_path, contrast=1.5, brightness=1.2, sharpness=1.5):
    
    try:

        image = Image.open(image_path)


        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(contrast)


        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(brightness)


        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(sharpness)


        image.save(output_path)
        print(f"Enhanced image saved at: {output_path}")

    except FileNotFoundError:
        print(f"Error: The file at {image_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
   

    input_image_path = r'C:\Users\alway\Desktop\Image Enhancement\test.jpg'


    output_image_path = r'C:\Users\alway\Desktop\Image Enhancement\enhanced_image.jpg'

   
    enhance_image(input_image_path, output_image_path)

if __name__ == "__main__":
    main()
