FROM python:3.8

ADD A_star_pathfinding.py .
ADD A_star_pathfinding_helper.py .
ADD arial.ttf .

RUN pip3 install pygame

CMD [ "python", "./A_star_pathfinding.py" ]
