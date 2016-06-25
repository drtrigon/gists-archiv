#!/usr/bin/env python
#
# Hi There!
# This script serves for the purpose of installing a testing environment to a
# Kubuntu VirtualBox guest as described in User:DrTrigon/file-metadata:
# https://commons.wikimedia.org/wiki/User:DrTrigon/file-metadata
#
# Inspired by https://github.com/pypa/get-pip/blob/master/get-pip.py
# http://www.pyinvoke.org/

from invoke import task

# Install procedure
def install(ctx, job):
    for cmd in job:
        print ("--- " * 10), "\n", cmd, "\n", ("--- " * 10)
        raw_input("[Enter] to continue, [Ctrl]+C to stop ...")
        ctx.run(cmd)

# Test through system package management
@task
def install_spm(ctx):
    job = [
    "sudo apt-get update",
    "sudo apt-get purge python-pip; sudo apt-get autoremove",
    "wget https://bootstrap.pypa.io/get-pip.py; sudo python get-pip.py",
    "pip show pip",
    "sudo apt-get install python-appdirs python-magic python-numpy python-scipy python-matplotlib python-wand python-skimage python-zbar",
    "sudo apt-get install cmake libboost-python-dev liblzma-dev",
    "sudo pip install file-metadata --upgrade",
    "python -c'import file_metadata; print file_metadata.__version__'",
    ]
    install(ctx, job)

# Test through pip
@task
def install_pip(ctx):
    job = [
    "sudo apt-get update",
    "sudo apt-get purge python-pip; sudo apt-get autoremove",
    "wget https://bootstrap.pypa.io/get-pip.py; sudo python get-pip.py",
    "pip show pip",
    "sudo apt-get install perl openjdk-7-jre python-dev pkg-config libfreetype6-dev libpng12-dev liblapack-dev libblas-dev gfortran cmake libboost-python-dev liblzma-dev libjpeg-dev python-virtualenv",
    "sudo pip install file-metadata",
    "python -c'import file_metadata; print file_metadata.__version__'",
    ]
    install(ctx, job)

# Installation of pywikibot
@task
def install_pywikibot(ctx):
    job = [
    "sudo apt-get install git git-review",
    "git clone --branch 2.0 --recursive https://gerrit.wikimedia.org/r/pywikibot/core.git",
    "cd core/",
    "python pwb.py basic",
    ]
    install(ctx, job)

# Test bot script
@task
def install_file_metadata_bot(ctx):
    job = [
    "$ sudo apt-get install libmagickwand-dev",
    "$ wget https://gist.githubusercontent.com/AbdealiJK/a94fc0d0445c2ad715d9b1b95ec2ba03/raw/492ef4076d5af74b4855fd26f6810f14cff07ec9/file_metadata_bot.py",
    ]
    install(ctx, job)
