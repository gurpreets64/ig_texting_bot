from instagrapi import Client
import downloader
import schedule
import time

def job():
    # Login to Instagram
    cl = Client()
    cl.login('official_music_reviewer', 'musicmusic64')

    # Get the list of all threads from both the inbox and the pending inbox
    inbox_threads = cl.direct_threads()

    # Iterate over each thread
    for thread in inbox_threads:
        print(f"Thread ID: {thread.id}, Users in thread: {thread.users}")

        # Get and print messages in each thread
        messages = cl.direct_messages(thread.id)
        # Check only the latest message in the thread
        message = messages[0]
        print(f"Message: {message.text}, From: {message.user_id}")

        # If the message is from someone else (not you)
        if message.user_id != cl.user_id:

            if message.clip is not None:
                video_url = message.clip.video_url
                print(f"The video URL is: {video_url}")
                link = str(video_url)
                downloader.non_api(link)
                video_path = 'reel.mp4'
                cl.direct_send_video(video_path, [], thread_ids=[thread.id])
                
                # Delete (hide) the thread after sending the video
                cl.direct_thread_hide(thread.id)
                
            else:
                print("This message does not include a video clip.")

# Schedule the job every 5 minutes
schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)