import os
import config
from image.process import process_existing_image, process_image

# seal-images/
#   LF1/
#       originals/
#       {iteration}/
#   LF28/
#       originals/
#       {iteration}/

# Handle folder with images ready to be processed

# For each image, get the predictions from Azure
# Order the predictions by value
# Create an image for each prediction and save with the prediction as the name
# Save the original image and the predictions along with the CSV

NEW_IMAGES_FOLDER = config.NEW_IMAGES_FOLDER
IMAGES_FOLDER = config.IMAGES_FOLDER


def process_images():
    for subdir, dirs, files in os.walk(NEW_IMAGES_FOLDER):
        for file in files:
            img_path = os.path.join(subdir, file)
            process_image(subdir, img_path)


def process_all_existing_images():
    originals = list_orignal_files(IMAGES_FOLDER)

    for img_path in originals:
        split_path = img_path.split('/')
        seal_name = split_path[2]

        image_name = split_path[4]
        split_image = image_name.split('.')
        unique_image_name = split_image[0]

        print seal_name
        print img_path
        print unique_image_name
        process_existing_image(seal_name, img_path, unique_image_name)


def list_orignal_files(dir):
    r = []
    subdirs = [x[0] for x in os.walk(dir)]
    for subdir in subdirs:
        # Only look through the orignals folders
        if 'originals' in subdir:
            files = os.walk(subdir).next()[2]
            if (len(files) > 0):
                for file in files:
                    r.append(subdir + "/" + file)
    return r


if __name__ == '__main__':
    process_all_existing_images()
