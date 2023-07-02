FROM python:3.10-slim

ARG CICD_STEP
ENV CICD_STEP=${CICD_STEP}

RUN python3 -m venv /opt/venv

COPY common /app/common
COPY ./${CICD_STEP} /app/${CICD_STEP}
COPY ./${CICD_STEP}.py /app/main.py
COPY ./requirements.txt /app
WORKDIR /app

RUN /opt/venv/bin/pip install -r requirements.txt

RUN pip3 install -r requirements.txt

VOLUME /app/test_results

CMD . /opt/venv/bin/activate && exec python main.py

