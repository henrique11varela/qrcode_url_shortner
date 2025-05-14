from flask import Flask, render_template
from io import BytesIO
import qrcode, base64

PORT = 5000
HOST = "0.0.0.0"

app = Flask(__name__)

@app.route("/qr/<data>")
def create_qrcode(data: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
 
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return {
        'image': img_str
    }

@app.route("/")
def hello_world():
    # create_qrcode('test')
    return render_template("index.html")

if __name__ == "__main__":
    print(f'Host: {HOST}')
    print(f'Port: {PORT}')
    app.run(host=HOST, port=PORT)
    
    