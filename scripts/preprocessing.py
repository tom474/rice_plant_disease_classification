from PIL import Image
import numpy as np


def remove_transparency(image: Image.Image) -> Image.Image:
    """
    Removes transparency from an image and ensures it is in RGB mode.

    This function checks whether the input image has an alpha (transparency) channel
    or is in a palette mode that may contain transparency. If so, it first converts
    the image to 'RGBA' mode (if not already), and then flattens the image by converting
    it to 'RGB', effectively removing any transparency information.

    Args:
        image (PIL.Image.Image): The input image which may contain transparency.

    Returns:
        PIL.Image.Image: A new image in 'RGB' mode without any alpha channel.
    """
    if image.mode in ("RGBA", "RGBa", "LA", "La", "PA", "P"):
        image = image.convert("RGBA")
        image = image.convert("RGB")
    return image


def resize_crop(image: Image.Image, width: int, height: int) -> Image.Image:
    """
    Crops the input image to match the target aspect ratio and resizes it to the specified dimensions.

    This function preserves the central portion of the image while cropping excess width or height
    based on the difference between the image's original aspect ratio and the desired output aspect ratio.
    After cropping, the image is resized to the exact target dimensions using high-quality resampling.

    Args:
        image (PIL.Image.Image): The input image to crop and resize.
        width (int): The desired output width.
        height (int): The desired output height.

    Returns:
        PIL.Image.Image: The resized and aspect-ratio-adjusted image.
    """
    original_aspect_ratio = image.width / image.height
    target_aspect_ratio = width / height

    if original_aspect_ratio > target_aspect_ratio:
        # Crop horizontally
        new_width = int(image.height * target_aspect_ratio)
        left = (image.width - new_width) // 2
        upper = 0
        right = left + new_width
        lower = image.height
    else:
        # Crop vertically
        new_height = int(image.width / target_aspect_ratio)
        left = 0
        upper = (image.height - new_height) // 2
        right = image.width
        lower = upper + new_height

    cropped_image = image.crop((left, upper, right, lower))
    resized_image = cropped_image.resize((width, height), Image.Resampling.LANCZOS)
    return resized_image


def preprocess_image(
    image: Image.Image, width: int = 256, height: int = 256, normalize: bool = True
) -> np.ndarray:
    """
    Applies a full preprocessing pipeline to a PIL image for model inference.

    The pipeline performs the following steps:
    1. Removes transparency (alpha channel) and ensures the image is in RGB mode.
    2. Crops the image to preserve the aspect ratio and resizes it to (width, height).
    3. Optionally normalizes pixel values to the [0, 1] range.
    4. Expands dimensions to add a batch dimension for model input (1, H, W, C).

    Args:
        image (PIL.Image.Image): The input image to preprocess.
        width (int, optional): Target width after resizing. Defaults to 256.
        height (int, optional): Target height after resizing. Defaults to 256.
        normalize (bool, optional): Whether to scale pixel values to [0, 1]. Defaults to True.

    Returns:
        np.ndarray: The preprocessed image tensor with shape (1, height, width, 3).
    """
    image = remove_transparency(image)
    image = resize_crop(image, width, height)
    image_array = np.array(image)

    if normalize:
        image_array = image_array.astype("float32") / 255.0

    return np.expand_dims(image_array, axis=0)
