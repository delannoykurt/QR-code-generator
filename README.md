# QR Code Generator 🔳

Une application web simple et rapide pour générer des QR Codes à partir de n'importe quel texte ou URL, développée en Python avec Flask.

## 🚀 Fonctionnalités

- Génération instantanée de QR Code depuis un texte ou une URL
- Affichage du QR Code directement dans le navigateur
- Possibilité de télécharger l’image générée
- Interface web claire et responsive

## 🛠️ Technologies utilisées

- Python 3
- Flask
- qrcode (bibliothèque Python)
- Pillow (pour le rendu d’image)

## 📦 Installation

```bash
git clone https://github.com/ton-utilisateur/QR-code-generator.git
cd qr-code-generator
pip install -r requirements.txt


📂 Structure du projet
qr-code-generator/
├── app.py                # Application Flask
├── templates/
│   └── index.html        # Interface HTML
├── static/
│   └── style.css         # Styles CSS
├── qrcodes/              # Dossier pour stocker les images générées
├── requirements.txt      # Dépendances Python
└── README.md             # Documentation
