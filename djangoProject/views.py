from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        # Get the user input from the form
        twitter_link = request.POST.get('user_input')

        # Download the Twitter video
        download_twitter_video(twitter_link)

    return render(request, 'home.html')


def download_twitter_video(twitter_link):
    # Get the HTML content of the Twitter page
    response = requests.get(twitter_link)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the video URL in the HTML content
    video_url = soup.find('video').find('source')['src']

    # Download the video
    response = requests.get(video_url)
    with open('twitter_video.mp4', 'wb') as f:
        f.write(response.content)


# Example usage:
# download_twitter_video('https://<TWITTER_LINK>')

# requests
#
# def home(request):
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input')
#         # do something with user_input here
#     return render(request, 'home.html')
#
#
#
# tiktok_url = '<URL>'
# api_url = '<API_URL>' + tiktok_url
#
# response = requests.get(api_url)
# data = response.json()
#
# # Handle the data returned by the API
# # For example, you could save the video to a file
# with open('tiktok-video.mp4', 'wb') as f:
#     f.write(requests.get(data['videoURL']).content)
