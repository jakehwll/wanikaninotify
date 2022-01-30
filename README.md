# wanikaninotify

This is a script for [WaniKani](https://www.wanikani.com/) to send notifications about your lessons hourly, should they be over an increment of 0. The phone notification side of things is achieved via [Gotify](https://gotify.net/). 

# Setup

compose (recommended).

```yaml
version: "3"
services:
  waninotify:
    image: hwll/wanikaninotify
    container_name: waninotify
    environment:
      - WANIKANI_API_TOKEN= # https://www.wanikani.com/settings/personal_access_tokens
      - GOTIFY_API_URI= # https://gotify.domain.com
      - GOTIFY_API_TOKEN= # https://gotify.domain.com/#/applications
    restart: unless-stopped # optional.
```

command.

```sh
# todo
docker run -d 
```