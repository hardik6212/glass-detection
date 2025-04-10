import os

def rename_images(folder_path, start_number, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Get all image files in the folder (assuming common image formats)
    image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff")
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]
    
    # Sort images to maintain order
    images.sort()
    
    # Rename images and save to output folder
    for index, image in enumerate(images, start=start_number):
        ext = os.path.splitext(image)[1]  # Get the file extension
        new_name = f"img_{index}{ext}"
        old_path = os.path.join(folder_path, image)
        new_path = os.path.join(output_folder, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {image} -> {new_name}")

if __name__ == "__main__":
    folder = r"C:\objYol\data\madukrrai\images"  # Set input folder path here
    start_num = 1  # Set starting number here
    output_folder = r"C:\objYol\CommonMRP\Images"  # Set output folder path here
    rename_images(folder, start_num, output_folder)
