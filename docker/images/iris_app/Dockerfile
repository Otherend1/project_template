FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu16.04

# path
ENV CONDA_PATH /opt/miniconda/bin/
ENV PATH $PATH:$CONDA_PATH
RUN echo PATH=$CONDA_PATH:$PATH >> /etc/environment

# install package
RUN apt-get -qq update && \
    apt-get -qq install wget && \
    apt-get -qq install curl && \
    apt-get -qq install bzip2 && \ 
    apt-get -qq install libgtk2.0-dev=2.24.30-1ubuntu1.16.04.2 && \
    apt-get -qq install iputils-ping=3:20121221-5ubuntu2 && \
    apt-get -qq install libcupti-dev=7.5.18-0ubuntu1 && \
    apt-get -qq install zip=3.0-11 && \
    apt-get -qq install unzip=6.0-20ubuntu1 && \
    apt-get -qq install -y libgl1-mesa-glx && \
    apt-get -qq install -y vim && \
    apt-get -qq install -y jq && \
    apt-get -qq autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install miniconda
RUN wget  https://repo.continuum.io/miniconda/Miniconda3-4.3.30-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    /bin/bash /tmp/miniconda.sh -b -u -p /opt/miniconda && \
    ${CONDA_PATH}conda clean -ay

# copy environments
ADD docker/images/iris_app/front_env.yml opt/docker/images/iris_app/front_env.yml
ADD docker/images/iris_app/back_env.yml opt/docker/images/iris_app/back_env.yml

# create environments
RUN ${CONDA_PATH}conda env create -n front_env -f /opt/docker/images/iris_app/front_env.yml && \
    ${CONDA_PATH}conda env create -n back_env -f /opt/docker/images/iris_app/back_env.yml && \
    ${CONDA_PATH}conda clean -ay

# copy project and cd in python
ADD . /opt/sources/project_template/
WORKDIR /opt/sources/project_template/python/

# launch app automatically when the container is launched
CMD /bin/bash -c '(source activate front_env && python ./../front/iris_app/run_front.py) & (source activate back_env && python ./../python/iris/webservice/iris_app/run_backend.py)'
