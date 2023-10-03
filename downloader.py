import requests
import json


def downl_api(link, vCodec = "h264", vQuality = "720", aFormat = "mp3", isAudioOnly = False):

    # URL of the API endpoint
    url = "http://localhost:9000/api/json"  # replace with the actual server address

    # Parameters for the download
    params = {
    "url": link,
    "vCodec": vCodec,
    "vQuality": vQuality,
    "aFormat": aFormat,
    "isAudioOnly": isAudioOnly
    }

    # Headers for the request
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # Send the POST request
    response = requests.post(url, data=json.dumps(params), headers=headers)

    print(response.json())
    stream_url = response.json()['url']

    # Send a GET request to the stream URL
    response = requests.get(stream_url)

    # Save the content to a file
    with open('output.mp4', 'wb') as f:
        f.write(response.content)


def non_api(link):
    # Send a GET request to the stream URL
    response = requests.get(link)

    # Save the content to a file
    with open('reel.mp4', 'wb') as f:
        f.write(response.content)

non_api('https://scontent.cdninstagram.com/v/t50.2886-16/381965999_1014539013217221_8814808887058975310_n.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6InZ0c192b2RfdXJsZ2VuLmNsaXBzLmMyLjEwODAuaGlnaCJ9&_nc_ht=instagram.fixc2-2.fna.fbcdn.net&_nc_cat=109&_nc_ohc=JL860oy6A5YAX9ieQbu&edm=AJXOVykBAAAA&vs=311564194797397_4095221313&_nc_vs=HBksFQAYJEdLOVd4QmJGVzM3RnQ1b0RBRTVLRzl6NmZWUjZicV9FQUFBRhUAAsgBABUAGCRHTmc1eVJaUmxRY25oZllBQU9XazVTRGJqQ1JUYnBSMUFBQUYVAgLIAQAoABgAGwAVAAAm8u6J4fqwl0AVAigCQzMsF0A5VT987ZFoGBJkYXNoX2hpZ2hfMTA4MHBfdjERAHX%2BBwA%3D&_nc_rid=64338fa891&ccb=7-5&oh=00_AfBLa-1vBdX4Qwv-VQHi9GU9XcXgxWXZ6XnJvA8x58d_fg&oe=651AE1BC&_nc_sid=07c3e7')
