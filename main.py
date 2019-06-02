import os

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
    list_files(ROOT_FOLDER)


def list_files(dir):
    r = []
    subdirs = [x[0] for x in os.walk(dir)]
    for subdir in subdirs:
        # Only look through the orignals folders
        if '/originals/' in subdir:
            files = os.walk(subdir).next()[2]
            if (len(files) > 0):
                for file in files:
                    r.append(subdir + "/" + file)
    print r


if __name__ == '__main__':
    process_all_existing_images()
