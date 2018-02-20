FROM ubuntu:16.04

MAINTAINER Reto Hasler <reto.hasler@asciich.ch>

RUN apt-get update && \
    apt-get install -y \
        python-software-properties \
        pwgen \
        software-properties-common \
        usbutils \
        wget \
        x11-apps \
        qt5-qmake \
        qt5-default \
        qtscript5-dev \
        libqt5webkit5-dev \
        libqt5serialport5-dev \
        libqt5svg5-dev \
        qtdeclarative5-qtquick2-plugin \
        libqt5serialport5-dev \
        libqt5opengl5-dev \
        git \
        libsdl1.2-dev \
        libsndfile-dev \
        flite1-dev \
        libssl-dev \
        libudev-dev \
        libsdl2-dev \
        python-serial \
        python-pexpect

COPY ./files/* /

RUN git clone https://github.com/diydrones/apm_planner
RUN cd /apm_planner && \
    git checkout master && \
    qmake apm_planner.pro && \
    make

RUN chmod +x /*.sh && \
    gpasswd -a root dialout && \
    ln -s /start_apmplanner2.sh /usr/sbin/apmplanner2
