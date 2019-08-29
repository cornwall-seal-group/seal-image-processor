from PIL import Image, ImageOps, ImageFilter
from predictions.pattern_detection import get_pattern_predictions
import uuid
import os
from image.crop import crop_image
from image.normalise import normalise_image
import config

IMAGES_FOLDER = config.IMAGES_FOLDER
ORIGINAL_IMG_FOLDER = 'originals/'
PREDICTIONS_IMG_FOLDER = 'pd_' + config.ITERATION_ID
EXT = '.jpg'


def process_image(seal_name, img_path, image_name):

    img = Image.open(img_path).convert('RGB')

    split_image = image_name.split('.')
    unique_image_name = split_image[0]

    # Find the predictions based on the original image, process and save the images
    process_predictions(img, seal_name, img_path, unique_image_name)


def process_predictions(img, seal_name, original_image_path, unique_img_name):
    processed_images = []
    pattern_predictions = get_pattern_predictions(original_image_path)

    predictions = pattern_predictions['predictions']

    prediction_index = 1
    # Loop through all the predictions
    for prediction in predictions:

        cropped_img = crop_image(img, prediction)
        normalised_img = normalise_image(cropped_img)

        # Create unique name for img (seal + index + prediction probability)
        predicted_img_name = unique_img_name + '-' + \
            str(prediction_index) + '-' + str(prediction.probability) + EXT

        save_normalised_image(predicted_img_name, normalised_img, seal_name)

        processed_images.append(predicted_img_name)
        prediction_index += 1

    return processed_images


def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath


def save_normalised_image(img_name, img, seal_name):
    seal_upload_folder = seal_name + '/' + PREDICTIONS_IMG_FOLDER

    upload_folder = IMAGES_FOLDER + seal_upload_folder
    create_new_folder(upload_folder)

    saved_path = os.path.join(upload_folder, img_name)
    img.save(saved_path)

    return saved_path
