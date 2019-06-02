import os
from image.process import process_existing_image
# Image processing
ROOT_FOLDER = '../seal-images/'

# seal-images/
#   LF1/
#       originals/
#       predictions/
#   LF28/
#       originals/
#       predictions/

# Handle folder with images ready to be processed

# For each image, get the predictions from Azure
# Order the predictions by value
# Create an image for each prediction and save with the prediction as the name
# Save the original image and the predictions along with the CSV


def process_all_existing_images():
    originals = list_orignal_files(ROOT_FOLDER)

    for img_path in originals:
        split_path = img_path.split('/')
        seal_name = split_path[2]

        image_name = split_path[4]
        split_image = image_name.split('.')
        unique_image_name = split_image[0]

        print seal_name
        print img_path
        print unique_image_name
        #process_existing_image(seal_name, img_path)


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
