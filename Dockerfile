FROM python:3.7

ENV PYTHONUNBUFERED 1
RUN mkdir NDS_Choises/
WORKDIR  NDS_Choises/
COPY requirements.txt /NDS_Choises/
RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /NDS_Choises/

