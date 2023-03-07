FROM continuumio/miniconda3
RUN apt-get update && apt-get upgrade -y && apt-get -y install g++
COPY ./ ./
WORKDIR /app
RUN conda env create -f /code/environment.yml
ENV PATH /opt/conda/envs/lang_detect/bin:$PATH
RUN /opt/conda/bin/activate lang_detect # activating conda envirionment
CMD python /code/lang_detect.py
