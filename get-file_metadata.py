#!/usr/bin/env python
#
# Hi There!
# This script serves for the purpose of installing a testing environment to a
# Kubuntu VirtualBox guest as described in User:DrTrigon/file-metadata:
# https://commons.wikimedia.org/wiki/User:DrTrigon/file-metadata
#
# Inspired by https://github.com/pypa/get-pip/blob/master/get-pip.py
# http://www.pyinvoke.org/

# Test through system package management
install_spm = [
"sudo apt-get update",
"sudo apt-get purge python-pip; sudo apt-get autoremove",
"wget https://bootstrap.pypa.io/get-pip.py; sudo python get-pip.py",
"pip show pip",
"sudo apt-get install python-appdirs python-magic python-numpy python-scipy python-matplotlib python-wand python-skimage python-zbar",
"sudo apt-get install cmake libboost-python-dev liblzma-dev",
"sudo pip install file-metadata --upgrade",
"python -c'import file_metadata; print file_metadata.__version__'",
]

# Test through pip
install_pip = [
"sudo apt-get update",
"sudo apt-get purge python-pip; sudo apt-get autoremove",
"wget https://bootstrap.pypa.io/get-pip.py; sudo python get-pip.py",
"pip show pip",
"sudo apt-get install perl openjdk-7-jre python-dev pkg-config libfreetype6-dev libpng12-dev liblapack-dev libblas-dev gfortran cmake libboost-python-dev liblzma-dev libjpeg-dev python-virtualenv",
"sudo pip install file-metadata",
"python -c'import file_metadata; print file_metadata.__version__'",
]

# Installation of pywikibot
install_pywikibot = [
"sudo apt-get install git git-review",
"git clone --branch 2.0 --recursive https://gerrit.wikimedia.org/r/pywikibot/core.git",
"cd core/",
"python pwb.py basic",
]

# Test bot script
install_file_metadata_bot = [
"$ sudo apt-get install libmagickwand-dev",
"$ wget https://gist.githubusercontent.com/AbdealiJK/a94fc0d0445c2ad715d9b1b95ec2ba03/raw/492ef4076d5af74b4855fd26f6810f14cff07ec9/file_metadata_bot.py",
]

# Install procedure
install = install_spm + install_pywikibot + install_file_metadata_bot
#install = install_pip + install_pywikibot + install_file_metadata_bot


import subprocess

def run(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()


def main():
    for cmd in install_spm:
        print ("--- " * 10), "\n", cmd, "\n", ("--- " * 10)
        raw_input("[Enter] to continue, [Ctrl]+C to stop ...")
        run(cmd)


if __name__ == "__main__":
    main()
