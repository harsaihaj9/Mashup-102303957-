import sys
import os
import yt_dlp
from pydub import AudioSegment

def download_videos(singer_name, num_videos):
    print("Downloading videos...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True,
        'noplaylist': True
    }

    os.makedirs("downloads", exist_ok=True)

    search_query = f"ytsearch{num_videos}:{singer_name} songs"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])

    print("Download completed.")


def convert_and_trim(duration):
    print("Converting and trimming audio files...")

    trimmed_files = []
    os.makedirs("trimmed", exist_ok=True)

    for file in os.listdir("downloads"):
        file_path = os.path.join("downloads", file)

        try:
            audio = AudioSegment.from_file(file_path)
            trimmed_audio = audio[:duration * 1000]

            output_file = os.path.join("trimmed", file.split(".")[0] + ".mp3")
            trimmed_audio.export(output_file, format="mp3")

            trimmed_files.append(output_file)

        except Exception as e:
            print(f"Error processing {file}: {e}")

    print("Conversion and trimming completed.")
    return trimmed_files


def merge_audios(audio_files, output_filename):
    print("Merging audio files...")

    if not audio_files:
        print("No audio files to merge.")
        return

    combined = AudioSegment.empty()

    for file in audio_files:
        audio = AudioSegment.from_mp3(file)
        combined += audio

    combined.export(output_filename, format="mp3")
    print(f"Final merged file created: {output_filename}")


def main():
    # Check correct number of parameters
    if len(sys.argv) != 5:
        print("Usage: python 102303957.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer_name = sys.argv[1]

    try:
        num_videos = int(sys.argv[2])
        duration = int(sys.argv[3])
    except ValueError:
        print("NumberOfVideos and AudioDuration must be integers.")
        sys.exit(1)

    output_filename = sys.argv[4]

    # Input validation
    if num_videos <= 10:
        print("NumberOfVideos must be greater than 10.")
        sys.exit(1)

    if duration <= 20:
        print("AudioDuration must be greater than 20 seconds.")
        sys.exit(1)

    try:
        download_videos(singer_name, num_videos)
        trimmed_files = convert_and_trim(duration)
        merge_audios(trimmed_files, output_filename)
        print("Mashup created successfully!")

    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
