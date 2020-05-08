import base64
def convert(image):
    with open(image, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    bash="data:image/png;base64,"+my_string.decode('utf-8')
    return bash