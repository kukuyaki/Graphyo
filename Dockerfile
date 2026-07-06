FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir networkx matplotlib

COPY . .

CMD ["python", "graph_input.py"]

#a dockerfile that install networkx and matplotlib and then "python graph_input.py"

#graph_input.py do not need this two lib  actually.
#what i want to do is make a virtual enviroment for developing Graphyo, because install pyplotlib in linux is annoying, so many dependencies.

#docker build -t graphyo-env .
#docker run --rm graphyo-env