FROM python:3.8

RUN apt-get update && apt-get install -y xterm
RUN useradd -ms /bin/bash xterm
USER xterm
WORKDIR /home/xterm

ADD A_star_pathfinding.py .
ADD A_star_pathfinding_helper.py .
ADD arial.ttf .

RUN pip3 install pygame

CMD [ "python3", "./A_star_pathfinding.py" ]
