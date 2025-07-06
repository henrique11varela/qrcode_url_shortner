from flask import Flask, render_template, request
from io import BytesIO
from utils.QR import create_qr_code

PORT = 5000
HOST = "0.0.0.0"

app = Flask(__name__)

@app.get("/test")
def index_test():
    return render_template("test.html")

@app.get("/qr")
def index_qrcode():
    return render_template("qr_maker.html")

@app.post("/qr")
def create_qrcode():
    data = request.json['text']
    img_str = create_qr_code(data)
    return {
        'image': f'data:image/jpeg;base64,{img_str}'
    }

@app.get("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    print(f'Host: {HOST}')
    print(f'Port: {PORT}')
    app.run(host=HOST, port=PORT)
    
    