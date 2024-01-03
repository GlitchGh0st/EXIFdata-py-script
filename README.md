# EXIFdata-py-script
This Python script, leveraging the PIL and piexif libraries, allows users to customize the EXIF data of an image by embedding a custom URL (or any text message) into the ImageDescription tag.


## README for EXIF Data Customizer Script

## Overview

This Python script, leveraging the PIL and piexif libraries, allows users to customize the EXIF data of an image by embedding a custom URL (or any text message) into the ImageDescription tag. This can be particularly useful for adding metadata, such as a reference link or a unique identifier, to images.

## Features

Add Custom URL to EXIF: Embeds a custom URL or text message into the image's EXIF data.

Preserve Existing EXIF Data: If the image already contains EXIF data, the script will only modify the ImageDescription tag and leave the rest of the data intact.

## Prerequisites

Before running this script, ensure you have Python installed on your system along with the following packages:

Pillow (PIL Fork): A powerful library for image processing.
piexif: A library to handle EXIF data of images.

## Install these packages using pip:

pip install Pillow

pip install piexif


## How to Use

Clone the Repository:

git clone [repo-link]
cd [repo-name]

## Running the Script:

Use the function add_url_to_exif(image_path, output_path, url) to add custom EXIF data to your image.
image_path: Path to the original image.
output_path: Path where the modified image will be saved.
url: The custom URL or text message you want to embed in the image's EXIF data.

## Example:

add_url_to_exif("path/to/original/image.jpg", "path/to/output/image.jpg", "https://example.com")

## Important Notes

This script modifies the EXIF data of the image. It is recommended to work on a copy of the image to avoid accidental loss of original data.
The script currently embeds data only in the ImageDescription tag. If you need to customize other EXIF tags, you might need to modify the script accordingly.

## License

Distributed under the MIT License. See LICENSE for more information.
