FROM ubuntu:16.04

ENV HOME=/root
WORKDIR $HOME

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    git

# install miniconda
ENV PATH=$HOME/miniconda3/bin:$PATH
RUN curl https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh > /root/Miniconda3-latest-Linux-x86_64.sh && \
    chmod u+x /root/Miniconda3-latest-Linux-x86_64.sh && \
    /root/Miniconda3-latest-Linux-x86_64.sh -b && \
    rm /root/Miniconda3-latest-Linux-x86_64.sh && \
    conda update -n base conda

# install packages listed in environment.yml including cpu-optimized tensorflow
COPY environment.yml $HOME/
RUN conda env create /root/environment.yml
ENV PATH=$HOME/miniconda3/envs/workshop/bin:$PATH


COPY . $HOME/

RUN mkdir -p $HOME/model/

EXPOSE 5000

CMD ["python", "app.py"]
