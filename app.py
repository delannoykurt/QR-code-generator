from flask import Flask, render_template, request, send_file, redirect, url_for
import qrcode
import os
from io import BytesIO
from qrcode.image.pil import PilImage

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
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,  # Taille d'un "bloc" du QR
                border=4,     # Taille des bordures
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")


        # On sauvegarde l'image dans le dossier
            qr_img_name = "qr_code.png"
            img.save(os.path.join(QR_FOLDER, qr_img_name))

            return redirect(url_for('home', qr=qr_img_name))


    qr_img_name = request.args.get('qr')
    return render_template('index.html', qr_img=qr_img_name)


@app.route('/qrcodes/<filename>')
def qrcode_file(filename):
    return send_file(os.path.join(QR_FOLDER, filename))



#------------------------------/
if __name__ == "__main__":
    app.run(port=5555, debug=True)
