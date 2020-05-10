# Ytopod

Generating rss podcast feed from selected youtube videos.

This app allows you to download youtube videos, convert them to audio and add them to rss feed, which can be added to podcast player. It is meant for listening to conferences and similar videos, where audio is enough and podcast players have many useful features for consuming such content.

# Todo

- [ ] more feeds
  - [ ] edit metadata about feed
  - [ ] assign video to more feeds
  - [ ] ordering per feed
- [x] auth
  - [x] login, protect almost all paths except home
  - [x] Add login mechanizms into UI, buttons, navigation filtering
    - [x] show simple navigation for unauthorized and rich navigation for logged in user
  - [x] first time register, if there is no user
  - [x] before first request check if any user exists, otherwise show first start
    - [x] on register path ~~redirect home~~ raise 404 if there is user already
  - [x] create http auth for podcast protection
- [ ] progress bar for videos being downloaded
  - [x] bootstrap progress bar on `all` site
  - [x] use socket io
  - [x] ~~allow user to close it, maybe cancel the download~~ autoreloads when all downloads are done
  - [ ] think about download cancel, but may be complicated
  - [x] auto ~~close~~ reload, ~~not sure~~
  - [ ] make socket connection only when previous site was from download, so it doesnt make useles socket connecitons on all `all` sites
    - [ ] or make separate page for viewing downloads and don't use `all` page