from PIL import Image, ImageOps, ImageFilter
from predictions.head_detection import get_head_predictions
import uuid
import os
from image.crop import crop_image
from image.normalise import normalise_image
from image_meta.store import store_seal_img_metadata, store_seal_metadata
import config

IMAGES_FOLDER = config.IMAGES_FOLDER
ORIGINAL_IMG_FOLDER = 'originals/'
PREDICTIONS_IMG_FOLDER = config.ITERATION_ID
EXT = '.jpg'


def process_image(seal_name, img_to_upload):

    # Create a unique filename for the image
    unique_img_name = str(uuid.uuid4())
    img_name = unique_img_name + EXT

    img = Image.open(img_to_upload).convert('RGB')
    saved_path = save_original_image(img_name, img, seal_name)

    prediction_images = process_predictions(
        img, seal_name, saved_path, unique_img_name)

    processed_images = [img_name] + prediction_images

    # Save metadata of seal and its predictions
    seal_folder = IMAGES_FOLDER + seal_name
    store_seal_img_metadata(seal_folder, seal_name, processed_images)

    # Save seal name for reference so we know what seals we have images for
    store_seal_metadata(IMAGES_FOLDER, seal_name)

    return {
        "id": unique_img_name
    }


def process_existing_image(seal_name, img_path, unique_img_name):

    img_name = unique_img_name + EXT
    img = Image.open(img_path).convert('RGB')
    # Remove previously stored row in seal's CSV file

    # Re-find the predictions based on the original image, process and save the images
    prediction_images = process_predictions(
        img, seal_name, img_path, unique_img_name)

    processed_images = [img_name] + prediction_images

    # Update seal's metadata file with new images
    # Save metadata of seal and its predictions
    seal_folder = IMAGES_FOLDER + seal_name
    store_seal_img_metadata(seal_folder, seal_name, processed_images)

    # Save seal name for reference so we know what seals we have images for
    store_seal_metadata(IMAGES_FOLDER, seal_name)


def process_predictions(img, seal_name, original_image_path, unique_img_name):
    processed_images = []
    head_predictions = get_head_predictions(original_image_path)

    predictions = head_predictions['predictions']

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


def save_original_image(img_name, img, seal_name):
    seal_upload_folder = seal_name + '/' + ORIGINAL_IMG_FOLDER
    upload_folder = IMAGES_FOLDER + seal_upload_folder

    create_new_folder(upload_folder)

    saved_path = os.path.join(upload_folder, img_name)
    img.save(saved_path)

    return saved_path


def save_normalised_image(img_name, img, seal_name):
    seal_upload_folder = seal_name + '/' + PREDICTIONS_IMG_FOLDER

    upload_folder = IMAGES_FOLDER + seal_upload_folder
    create_new_folder(upload_folder)

    saved_path = os.path.join(upload_folder, img_name)
    img.save(saved_path)

    return saved_path
