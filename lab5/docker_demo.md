hands-on-exam-1 - 2 parts: 
 1 part scraping, data then put in pd dataframe
  be familiar with seaborn, pandas, matplotlib,
 2 part pandas

if you dont manage to do the first part, do something - make your own data, download from online etc.


Demo:
docker - similar to virtual machines, just the operation part, not the hardware

streamlit - useful; check it out; good for visualizations

move to webapp folder, and run streamlit run app.py

save the model with pickle to a file - used for serialization; the file saved is binary; open this file then in the app.py with pickle again
we can then dockerize the app

main terms: docker image & docker container

docker file - the blueprint 
the imgae - snapshot of the environment/software and all the dependencies
container - the running process, created from the image

important to have the same python version for the whole process, model creation and the docker

use docker build on docker docs to check the documentation

run: docker build -t my-st-app . (goes through all the commands in the docker file, pip install takes the longest time, the other things are fast because they are cached) -> this builds the image - you can see it in docker desktop

run: docker images

we can make the image into a container

run: docker ps


view the app through docker desktop by clicking the container's port

check docker hub for images

the data does not persist; every time you restart, it will be lost; use dockerfile reference  - VOLUME (tells the image which directory to use for storing files); another is ENV (put some extra variables to the image)

important concept: docker compose (make a docker compose yml file which specifies all of the parameters, which containers to run)

try jupyter into docker (likely on exam)

command for building images: docker build -t my-st-app ./python 

can also execute commands in the exec tab in the container on docker desktop

there is a task on the exam with docker compose

install conda on the container system first (?) and then creating the environment, then run to activate the environment -> check online, maybe only start with creating env


exam: creating env, export it, create env from file, know both venv and conda but only use one here; create repo, clone locally, make change, push change; web scraping a bit - can do it both in a static way and with javascript, -> save the link of the page (beautifulsoup here?), can use selenium or not, not necessary. no fancy javascript; then pandas part, visualziations with matplotlib & a bit of seaborn (there will be one plot with seaborn); aggregate this, export this.. (include/exclude index, header..) - things from the notebook
