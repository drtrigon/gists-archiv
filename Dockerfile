############################################################
# Dockerfile to build gsoc-catimages container images (trivial)
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu:14.04

# File Author / Maintainer
MAINTAINER Example DrTrigon

# Update the repository sources list
RUN apt-get update

################## BEGIN INSTALLATION ######################
# Install gsoc-catimages Following the Instructions at Wikipedia Commons
# Ref: https://commons.wikimedia.org/wiki/User:DrTrigon/file-metadata

## Setup a VirtualBox with osboxes.org Kubuntu_14.04.3-64bit.7z (see http://www.osboxes.org/kubuntu/)...
#RUN apt-get update
#RUN apt-get --yes upgrade
#RUN apt-get --yes autoremove
# vvv not needed look into tasks.py and use the correct install procedure for pip
RUN apt-get --yes install python-pip wget

# Installation of file-metadata etc.
RUN pip install invoke
RUN wget https://gist.githubusercontent.com/drtrigon/2dcbc5fbac1e00f0f89dec9343994e48/raw/d755448ebfbcbf156ee0b01289c34583db31b1d6/tasks.py

# github
RUN invoke install_pywikibot --yes install_file_metadata_git --yes; invoke install_file_metadata_git --yes

##################### INSTALLATION END #####################

RUN echo DONE

## Expose the default port
#EXPOSE 27017
#
## Default port to execute the entrypoint (MongoDB)
#CMD ["--port 27017"]
#
## Set default container command
#ENTRYPOINT usr/bin/mongod