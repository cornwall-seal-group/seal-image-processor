import os
import config
from image.process import process_image

# seal-images/
#   LF1/
#       originals/
#       pd_{iteration}/
#   LF28/
#       originals/
#       pd_{iteration}/

# Handle folder with images ready to be processed

# For each image, get the predictions from Azure
# Order the predictions by value
# Create an image for each prediction and save with the prediction as the name
# Save the original image and the predictions along with the CSV

IMAGES_FOLDER = config.IMAGES_FOLDER


def process_images():
    originals = list_orignal_files(IMAGES_FOLDER)

    for img_path in originals:
        split_path = img_path.split('/')
        seal_name = split_path[2]

        image_name = split_path[4]

        print seal_name
        print img_path
        print image_name
        process_image(seal_name, img_path, image_name)


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
    process_images()
