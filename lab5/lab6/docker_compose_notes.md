How does it work:

upload mp4 file to streamlit, this will be sent to whisper server for transcription, from where the txt file is sent back to the streamlit

- check the faster-whisper on the docker documentation

First, check if already transcribed; if yes, show the transcription to the streamlit, else send to whisper server for transcription

- use redis database to store the transcriptions; ordinary database with keys and values; 

to set up redis, pull it; 

Docker-compose:

- make a yml file for the docker-compose;

- environment variables: `REDIS_HOST=redis` - this is the name of the service in the docker-compose file

- redis : 6379 - the port of the redis service

- https://whisper:8000/

- check volumes on the docker app for the whisper server

- be in the same directory as the compose file -> then run `docker-compose up` -> notice in the docker app in the containers, how they are stacked

- to stop the services, run `docker-compose down` (or CTRL+C twice)

Next exam: 

- more focused on database maybe

- know docker compose

- know how to make a jupyter server instance; connect from host machine to server; with the docker 

- check Dockerfile reference documentation
