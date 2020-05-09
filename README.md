# Ytopod

Generating rss podcast feed from selected youtube videos.

This app allows you to download youtube videos, convert them to audio and add them to rss feed, which can be added to podcast player. It is meant for listening to conferences and similar videos, where audio is enough and podcast players have many useful features for consuming such content.

# Todo

- [ ] more feeds
  - [ ] edit metadata about feed
  - [ ] assign video to more feeds
  - [ ] ordering per feed
- [ ] auth
  - [x] login, protect almost all paths except home
  - [ ] Add login mechanizms into UI, buttons, navigation filtering
    - [ ] show simple navigation for unauthorized and rich navigation for logged in user
  - [ ] first time register, if there is no user
  - [ ] before first request check if any user exists, otherwise show first start
    - [ ] on register path redirect home if there is user already
- [ ] progress bar for videos being downloaded
  - [ ] bootstrap progress bar on `all` site
  - [ ] use socket io
  - [ ] allow user to close it, maybe cancel the download
  - [ ] auto close, not sure