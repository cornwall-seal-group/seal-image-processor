# stargazer

This project processes provided images with the Azure Custom Vision API to find patterns within the images, crop, enhance then stores them.

The idea is for this project to be kicked off as an offline batch processing tool to process either newly uploaded seal images for training, or to re-process existing images.

The `config.py` should be configured with: PROJECT_ID, ITERATION_ID, ITERATION_NAME, PREDICTION_KEY, ENDPOINT for the Azure trained object detection model

The IMAGES_FOLDER should point to the location of your images. In this folder, it is expected the folder structure look like:

```
seal-images/
  LF1/
      originals/
  LF28/
      originals/
```

Once the project has run, the folder structure will look as follows:

```
seal-images/
  LF1/
      originals/
      pd_{iteration}/
  LF28/
      originals/
      pd_{iteration}/
```
