# We receive the prediction bounding box as the following values in %
# This needs to convert the %'s to pixels and crop the image accordingly
# {
#    height: 0.494349241,
#    left: 0.0181922168,
#    top: 0.0303361267,
#    width: 0.4266795,
# }


def crop_image(img, prediction):
    image_width = img.width
    image_height = img.height

    b_box = prediction.bounding_box
    b_height = b_box.height
    b_width = b_box.width
    b_top = b_box.top
    b_left = b_box.left

    left = b_left*image_width
    upper = b_top*image_height
    right = left + (b_width*image_width)
    lower = upper + (b_height*image_height)

    if (right - left < 1):
        if (image_width - right > 1):
            right = right+1
        else:
            left = left-1

    if (upper - lower < 1):
        if (image_height - lower > 1):
            lower = lower-1
        else:
            upper = upper+1

    print (left, upper, right, lower)
    return img.crop((left, upper, right, lower))
