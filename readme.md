# Mashup Generator Project

**Roll Number:** 102303957

------------------------------------------------------------------------

# 🔹 Program 1 -- Command Line Mashup Generator

## 📌 Objective

Develop a command-line Python program that:

1.  Downloads **N YouTube videos** of a given singer\
2.  Converts videos to audio\
3.  Cuts first **Y seconds** from each audio\
4.  Merges all trimmed audios into one final output file

------------------------------------------------------------------------

## 📂 File Name

    102303957.py

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python
-   yt-dlp (YouTube downloading)
-   pydub (Audio processing)
-   ffmpeg (Audio conversion backend)

------------------------------------------------------------------------

## 📥 Installation

Install required packages:

    pip install yt-dlp pydub

Also install **ffmpeg** on your system.

------------------------------------------------------------------------

## ▶️ How to Run

    python 102303957.py "Singer Name" NumberOfVideos AudioDuration OutputFileName.mp3

### Example:

    python 102303957.py "Sharry Maan" 20 30 output.mp3

------------------------------------------------------------------------

## ✅ Validations Included

-   Checks correct number of arguments
-   Ensures videos \> 10
-   Ensures duration \> 20 seconds
-   Handles exceptions
-   Displays appropriate error messages

------------------------------------------------------------------------

## 🔄 Working Flow

1.  Takes input from command line\
2.  Uses yt-dlp to search and download videos\
3.  Converts video to audio\
4.  Trims first Y seconds using pydub\
5.  Merges all audio files\
6.  Generates final mashup file

------------------------------------------------------------------------

# 🔹 Program 2 -- Web Service Mashup Generator

## 📌 Objective

Develop a web-based service where user:

-   Enters singer name\
-   Enters number of videos\
-   Enters duration\
-   Clicks Generate

System generates mashup and downloads ZIP file.

------------------------------------------------------------------------

## 🌐 Live Deployment URL

👉 https://mashup-wheat.vercel.app

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Flask (Backend)
-   HTML + CSS (Frontend)
-   yt-dlp
-   pydub
-   Vercel (Deployment)

------------------------------------------------------------------------

## 📂 Project Structure

    app.py
    requirements.txt
    vercel.json
    templates/
        index.html
    static/
        style.css

------------------------------------------------------------------------

## 🚀 Deployment Steps

1.  Push project files to GitHub\
2.  Import repository in Vercel\
3.  Deploy\
4.  Access live URL

------------------------------------------------------------------------

## ⚠️ Note About Deployment

Vercel is a serverless environment.\
Heavy media processing (yt-dlp + ffmpeg) may face timeout limitations.

For full production usage, deployment on platforms like Render is
recommended.

------------------------------------------------------------------------

# 🎓 Viva Explanation (Short Summary)

This project demonstrates:

-   Integration of external libraries (yt-dlp, pydub)
-   File handling
-   Audio processing
-   Command-line argument handling
-   Web service development using Flask
-   Deployment using cloud platform (Vercel)

The system automates mashup creation by downloading, trimming, and
merging audio files dynamically.

------------------------------------------------------------------------

# ✅ Conclusion

Both command-line and web-based mashup generators are implemented
successfully as per assignment requirements.
