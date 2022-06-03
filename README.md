# wanikaninotify

This is a script for [WaniKani](https://www.wanikani.com/) to send notifications about your reviews and lessons hourly, should more than zero.

The following tech is used.

* WaniKani (for gathering lessons/reviews count).
* Gotify (for sending notifications to your phone).
* Docker (for easy deployment).

## Supported Architectures

The architectures supported by this image are `amd64`, `arm/v7` and. `arm64`

## Version tags

This image provides a singular version, built from the `main` branch.

## Usage

Here are some example snippets to help you get started creating a container.

docker-compose (recommended).

```yaml
# docker-compose.yml
version: "3"
services:
  waninotify:
    image: https://ghcr.io/jakehwll/wanikaninotify
    container_name: wanikaninotify
    environment:
      - WANIKANI_API_TOKEN= # https://www.wanikani.com/settings/personal_access_tokens
      - GOTIFY_API_URI= # https://gotify.domain.com
      - GOTIFY_API_TOKEN= # https://gotify.domain.com/#/applications
    restart: unless-stopped # optional.
```

```sh
docker-compose up -d
```

command.

```sh
# environment variables
export WANIKANI_API_TOKEN=""
export GOTIFY_API_URI=""
export GOTIFY_API_TOKEN=""
# todo
docker run \
  --name="wanikaninotify" \
  -e WANIKANI_API_TOKEN=${WANIKANI_API_TOKEN} \
  -e GOTIFY_API_URI=${GOTIFY_API_URI} \
  -e GOTIFY_API_TOKEN=${GOTIFY_API_TOKEN} \
  --restart unless-stopped \
  ghcr.io/jakehwll/wanikaninotify
```

## Parameters

| Parameter                                   | Function |
| ------------------------------------------- | -------- |
| -e WANIKANI_API_TOKEN=${WANIKANI_API_TOKEN} |
| -e GOTIFY_API_URI=${GOTIFY_API_URI}         |
| -e GOTIFY_API_TOKEN=${GOTIFY_API_TOKEN}     |

## Environment variables from files

You can set any environment variable from a file by using a special prepend FILE__.

As an example:

```sh
docker run \
  --name="wanikaninotify" \
  -e FILE__PASSWORD=./.env
```
