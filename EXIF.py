from PIL import Image
import piexif

def add_url_to_exif(image_path, output_path, url):
    # Load the image
    img = Image.open(image_path)

    # Check if the image has EXIF data
    if "exif" in img.info:
        exif_dict = piexif.load(img.info["exif"])
    else:
        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

    # Embed the URL in the ImageDescription tag
    exif_dict['0th'][piexif.ImageIFD.ImageDescription] = url.encode('utf-8')

    # Generate the new EXIF bytes
    exif_bytes = piexif.dump(exif_dict)

    # Save the image with new EXIF data
    img.save(output_path, exif=exif_bytes)

# Example usage
add_url_to_exif("/home/kali/Desktop/PNG.png", "/home/kali/Desktop/PNG2.png", "Put your custom message with e.g. a >>>>  https://drive.google.com/file/d????????????????????????????????????????????")

