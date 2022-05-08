FROM ubuntu:latest


# Install some basic utilities
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    wget \
 && rm -rf /var/lib/apt/lists/*

# Create a working directory
ARG user=pymlboot
ARG datadir=/data

RUN mkdir $datadir
WORKDIR $datadir

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' --shell /bin/bash $user \
 && chown -R $user:$user $datadir
RUN echo "${user} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-user

# Install python-dev and build-essential
RUN apt update
RUN apt-get install -y python-dev-is-python3
RUN apt-get install -y build-essential

USER $user

# All users can use /home/user as their home directory
ENV HOME=/home/$user
RUN chmod 777 /home/$user

# Install anaconda
RUN wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh -O /home/$user/anaconda.sh \
 && chmod +x /home/$user/anaconda.sh \
 && /home/$user/anaconda.sh -b -p ~/anaconda3 \
 && rm /home/$user/anaconda.sh
RUN echo $(ls -1 ~/*)
ENV PATH=$HOME/anaconda3/bin:$PATH
ENV CONDA_AUTO_UPDATE_CONDA=false

# Create a Conda Environment
COPY environment.yml .
RUN $HOME/anaconda3/bin/conda env create -f environment.yml \
 && $HOME/anaconda3/bin/conda clean -ya
ENV CONDA_DEFAULT_ENV=py38
ENV CONDA_PREFIX=$HOME/anaconda3/envs/$CONDA_DEFAULT_ENV
ENV PATH=$CONDA_PREFIX/bin:$PATH 
RUN $HOME/anaconda3/bin/conda clean -ya
RUN $HOME/anaconda3/bin/conda init bash
RUN echo "source activate $(head -1 environment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 environment.yml | cut -d' ' -f2)/bin:$PATH

VOLUME $datadir
WORKDIR $datadir

# Set the default command to jupyter notebook
CMD ["bash", "-c", "source ~/.bashrc && jupyter notebook --notebook-dir=/data --ip=* --port=8888 --no-browser --allow-root"]
