
# 🎵 Mashup Generator

This project contains two implementations of a Mashup Generator:

1. **Program 1** – Command Line Mashup Generator  
2. **Program 2** – Web-Based Mashup Generator  

---

## 🔹 Program 1 – Command Line Application

### 📌 Description
A Python script that:

- Downloads multiple YouTube videos of a given singer
- Converts them to audio
- Trims the first N seconds from each file
- Merges all trimmed audio clips into one final mashup file

### 📂 File
```
102303957.py
```

### 🛠 Requirements
- Python 3.x
- yt-dlp
- pydub
- ffmpeg (must be installed on system)

### 📦 Install Dependencies
```
pip install yt-dlp pydub
```

### ▶️ Usage
```
python 102303957.py "Singer Name" NumberOfVideos Duration OutputFile.mp3
```

### Example
```
python 102303957.py "Sharry Maan" 20 30 output.mp3
```

---

## 🔹 Program 2 – Web Application

### 📌 Description
A web-based version of the mashup generator where users can:

- Enter singer name
- Enter number of videos
- Enter duration (seconds)
- Generate and download mashup as a ZIP file

### 🌐 Live Deployment
https://mashup-wheat.vercel.app

### 🛠 Technologies Used
- Flask
- HTML
- CSS
- yt-dlp
- pydub

### 📂 Project Structure
```
app.py
requirements.txt
vercel.json
templates/
static/
```

### 📦 Install Dependencies (Local Run)
```
pip install -r requirements.txt
```

### ▶️ Run Locally
```
python app.py
```

---

## ⚠️ Notes

- Ensure `ffmpeg` is installed and accessible via system PATH.
- Media processing can take time depending on number of videos selected.

---

## 📜 License
This project is created for educational purposes.
