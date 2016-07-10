############################################################
# Dockerfile to build gsoc-catimages container image
# Based on Ubuntu resp. file_metadata_0.1.0.dev99999999999999
############################################################

# Set the base image to Ubuntu
FROM file_metadata_0.1.0.dev99999999999999

# File Author / Maintainer
MAINTAINER DrTrigon <dr.trigon@surfeu.ch>

# Update the repository sources list
RUN apt-get update

################## BEGIN INSTALLATION ######################
# Install gsoc-catimages Following the Instructions at Wikipedia Commons
# Ref: https://commons.wikimedia.org/wiki/User:DrTrigon/file-metadata

# Installation of pywikibot
#RUN git clone --branch 2.0 --recursive https://gerrit.wikimedia.org/r/pywikibot/core.git /opt/pywikibot-core
#    "cd core/; python pwb.py basic",    # issue: ctx.run stops after this line

# Setup of simple_bot.py
#RUN apt-get -y install libmagickwand-dev
#    #"cd core/; wget https://gist.githubusercontent.com/AbdealiJK/a94fc0d0445c2ad715d9b1b95ec2ba03/raw/1dcd1fb8c168608c28e20ff50e9284700f61b90d/file_metadata_bot.py",
#RUN python pwb.py file_metadata/wikibot/simple_bot.py -cat:SVG_files -limit:5

# Setup of bulk.py
RUN apt-get install python-opencv
RUN pip install retry
RUN wget https://raw.githubusercontent.com/AbdealiJK/file-metadata/95cc2abb3506608266b1faf0da0722433ad6b03b/tests/bulk.py
RUN ln -s /opt/file-metadata/tests tests
RUN python bulk.py -search:'eth-bib' -limit:5 -logname:test -dryrun:1

##################### INSTALLATION END #####################

# Run tests here ... may be do unittests or run a bot script

RUN echo DONE
