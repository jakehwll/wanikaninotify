import os
import requests
from dotenv import load_dotenv
from distutils.log import debug

load_dotenv()

_wanikani = {
  "prefix": "🐊🦀",
  "url": "https://api.wanikani.com",
  "endpoint": "/v2/assignments",
  "params": {
      "lessons": "immediately_available_for_lessons",
      "reviews": "immediately_available_for_review"
  },
  "authorization": os.getenv('WANIKANI_API_TOKEN')
}

_gotify = {
  "prefix": "🐻🔔",
  "url": os.getenv('GOTIFY_API_URI'),
  "endpoint": "/message",
  "authorization": os.getenv('GOTIFY_API_TOKEN')
}

def count(method):
  response = requests.request(
    method="GET", 
    url=f"{_wanikani['url']}{_wanikani['endpoint']}?{_wanikani['params'][method]}", 
    headers={ "Authorization": f"Bearer {_wanikani['authorization']}" }
  )

  if (response.ok):
    json = response.json()
    length = len(json['data'])
    debug(f"{json}")
    debug(f"{length}")
    return length
  else:
    print(f"{_wanikani['prefix']} - Response not happy, error code %s" % response.status_code)
    return None

def notify(title, message):
  response = requests.request(
    method="POST", 
    url=f"{_gotify['url']}{_gotify['endpoint']}", 
    headers={ "X-Gotify-Key": f"{_gotify['authorization']}" },
    data={
      "id": title,
      "title": title,
      "message": message,
      "priority": 2
    }
  )

  if (response.ok == False):
    print(f"{_gotify['prefix']} - Response not happy, error code %s" % response.status_code)

  return response

lessons = count('lessons')
reviews = count('reviews')

if ( lessons > 1 ):
  notify("Lessons", f'You have {lessons} lessons available.')
if ( reviews > 1 ):
  notify("Reviews", f'You have {reviews} reviews available.')