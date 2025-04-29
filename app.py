from flask import Flask, render_template, request, send_file
import qrcode
import os
from io import BytesIO

app = Flask(__name__)

# Dossier pour stocker temporairement les QR codes
QR_FOLDER = "qrcodes"
os.makedirs(QR_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    qr_img = None
    if request.method == 'POST':
        data = request.form.get('qrdata')

        if data:
            img = qrcode.make(data)

            # On enregistre dans un objet mémoire (pas directement sur disque pour l'instant)
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)

            return send_file(buffer, mimetype='image/png', as_attachment=True, download_name='qrcode.png')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
