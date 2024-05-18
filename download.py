# ytbdownload
download youtube videos
import os
import yt_dlp

def download_video(video_url, download_folder):
    ydl_opts = {
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'format': 'best',
        'noplaylist': True,
        'nocheckcertificate': True,
        'restrictfilenames': True,
        'username': os.getenv('youremail@domain.com'),  # Use environment variable
        'password': os.getenv('yourpassword'),  # Use environment variable
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            print(f"Downloaded: {video_url}")
    except yt_dlp.utils.DownloadError as e:
        print(f"An error occurred while downloading {video_url}: {e}")

def download_videos(video_urls, download_folder):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for video_url in video_urls:
        download_video(video_url, download_folder)

# Example usage:
video_urls = ['the link you want to download',]
download_folder = r'the address you want to save'  # Use raw string to avoid escape sequence issues
download_videos(video_urls, download_folder)
