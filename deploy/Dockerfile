FROM python:alpine3.7
RUN apk update && apk add git
WORKDIR /
RUN  git clone https://github.com/prinewgirl/projetomagrathea.git \
     && pip install -r /projetomagrathea/requirements.txt 
RUN apk del git
RUN chmod +x /projetomagrathea/run.sh
ENTRYPOINT ["/projetomagrathea/run.sh"]

