# 🔐 Video Encryption & Decryption using Python

## 📌 Overview
This project implements a custom video encryption and decryption system using:
- Permutation (P-box)
- Substitution (S-box)
- XOR-based diffusion

Each video frame is processed block-wise (8×8 blocks) and transformed using a password-based key.

---

## 🚀 Features
- Password-based encryption
- Frame-by-frame processing
- Block cipher-like transformation
- Dynamic key update (feedback mechanism)
- Full decryption support
- Works with any video input

---

## 🛠️ Tech Stack
- Python
- OpenCV
- NumPy

---

## 📂 Project Structure

video-encryption-decryption/
│
├── src/
│   ├── encrypt.py
│   ├── decrypt.py
│   └── utils.py
│
├── samples/
│   ├── input_video.mp4
│   ├── encrypted_sample.mp4
│   └── decrypted_sample.mp4
│
├── requirements.txt
├── README.md
└── .gitignore

---

## ⚙️ Installation

1. Clone the repository:
git clone https://github.com/your-username/video-encryption-decryption.git

2. Go into the folder:
cd video-encryption-decryption

3. Install dependencies:
pip install -r requirements.txt

---

## ▶️ Usage

### Encrypt a Video
python src/encrypt.py

### Decrypt a Video
python src/decrypt.py

Make sure to use the SAME password for encryption and decryption.

---

## 🧠 How It Works

### 1. Key Generation
- Password is converted into a seed
- Generates:
  - P-box (permutation)
  - S-box (substitution)
  - Initial key matrix

### 2. Encryption
- Resize frame to 256x256
- Divide into 8x8 blocks
- Apply permutation and substitution
- Apply XOR diffusion
- Update key using encrypted frame

### 3. Decryption
- Reverse diffusion
- Apply inverse substitution
- Apply inverse permutation

---

## 📊 Workflow

Input Video → Encryption → Encrypted Video  
Encrypted Video → Decryption → Original Video  

---

## ⚠️ Limitations
- Fixed resolution (256x256)
- Not optimized for speed
- Not production-grade encryption

---

## 📈 Future Improvements
- Variable resolution support
- Faster implementation using NumPy
- CLI support (input/output/password)
- Better cryptographic design

---

## 🧪 Example

encrypt_video("my_password", "input.mp4", "encrypted.mp4")  
decrypt_video("my_password", "encrypted.mp4", "decrypted.mp4")

---

## 📜 License
MIT License

---
