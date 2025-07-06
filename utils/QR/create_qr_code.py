import qrcode, base64, io
from PIL import Image
import numpy as np

def text_to_qr_code_image(text: str) -> np.ndarray :
    '''Creates a QRcode image from a string'''
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(f'{text}')
    qr.make(fit=True)
    img_pil = qr.make_image(fill_color="black", back_color="white")
    img = np.array(img_pil)
    return img

def image_to_base64(image_matrix: np.ndarray) -> str :
    '''Creates a base64 string from an image'''
    image = Image.fromarray(image_matrix)
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    return img_base64

def create_qr_code(text: str) -> str:
    '''Creates a base64 string of a QRcode generated from a string'''
    img = text_to_qr_code_image(text)
    img_base64 = image_to_base64(img)
    return img_base64

if __name__ == '__main__':
    print('test')