import os
import cv2

# Set the folder paths (Modify these paths)
input_folder = r"C:\objYol\GlassNoGlass\Data\test\test"  # Replace with your actual image folder path
output_folder = r"C:\objYol\GlassNoGlass\Data\test_greyscale"  # Replace with your desired output path

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Convert images to greyscale
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):  # Supported formats
        img_path = os.path.join(input_folder, filename)
        save_path = os.path.join(output_folder, filename)

        # Read the image
        img = cv2.imread(img_path)
        if img is None:
            print(f"Skipping {img_path}, not a valid image.")
            continue

        # Convert to greyscale
        grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Save the greyscale image
        cv2.imwrite(save_path, grey_img)
        print(f"Converted: {filename} -> {save_path}")

print("✅ Greyscale conversion completed successfully!")
