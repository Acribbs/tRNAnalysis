FROM phusion/baseimage:0.11
MAINTAINER Adam Cribbs <adam.cribbs@ndorms.ox.ac.uk>

CMD ["/sbin/my_init"]
ADD . /tmp/repo
WORKDIR /tmp/repo
ENV SHELL /bin/bash
ENV LANG C.UTF-8
FROM continuumio/miniconda3
ADD conda/environments/trnanalysis.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml
RUN echo "source activate $(head -1 /tml/environment.yml | cut -d ' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml| cut -d' ' -f2)/bin:$PATH
ENTRYPOINT ["python"]
CMD ["setup.py develop"]
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
