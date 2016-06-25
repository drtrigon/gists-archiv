#!/usr/bin/env python
#
# Hi There!
# This script serves for the purpose of installing a testing environment to a
# Kubuntu VirtualBox guest as described in User:DrTrigon/file-metadata:
# https://commons.wikimedia.org/wiki/User:DrTrigon/file-metadata
#
# Usage: invoke install_file_metadata_spm install_pywikibot install_file_metadata_bot; invoke install_file_metadata_bot
#        invoke install_file_metadata_pip install_pywikibot install_file_metadata_bot; invoke install_file_metadata_bot
#        invoke install_file_metadata_pip --yes install_pywikibot --yes install_file_metadata_bot --yes; invoke install_file_metadata_bot --yes
#
# Inspired by https://github.com/pypa/get-pip/blob/master/get-pip.py
#         and http://www.pyinvoke.org/

from invoke import task

# Install procedure
def install(ctx, job, yes=False):
    for cmd in job:
        print "\n", ("--- " * 10), "\n", cmd, "\n", ("--- " * 10)
        if not yes:
            raw_input("[Enter] to continue or [Ctrl]+C to stop ...")
        ctx.run(cmd)

def params(*args, **kwargs):
    kwargs['yes'] = '--yes' if kwargs['yes'] else ''
    return kwargs

# Test through system package management
@task
def install_file_metadata_spm(ctx, yes=False):
    install_pip(ctx, yes=yes)
    install_file_metadata_deps_spm(ctx, yes=yes)
    install_file_metadata(ctx, yes=yes)

def install_pip(ctx, yes=False):
    p   = params(yes=yes)
    job = [
    "sudo apt-get %(yes)s update" % p,
    "sudo apt-get %(yes)s purge python-pip; sudo apt-get %(yes)s autoremove" % p,
    "wget https://bootstrap.pypa.io/get-pip.py; sudo python get-pip.py",
    "pip show pip",
    ]
    install(ctx, job, yes=yes)

def install_file_metadata_deps_spm(ctx, yes=False):
    p   = params(yes=yes)
    job = [
    "sudo apt-get %(yes)s install python-appdirs python-magic python-numpy python-scipy python-matplotlib python-wand python-skimage python-zbar" % p,
    "sudo apt-get %(yes)s install cmake libboost-python-dev liblzma-dev libjpeg-dev libz-dev" % p,    # for dlib, pillow compilation
    ]
    install(ctx, job, yes=yes)

def install_file_metadata(ctx, yes=False):
    p   = params(yes=yes)
    job = [
    "sudo pip install file-metadata --upgrade",
    "python -c'import file_metadata; print file_metadata.__version__'",
    ]
    install(ctx, job, yes=yes)

# Test through pip
@task
def install_file_metadata_pip(ctx, yes=False):
    install_pip(ctx, yes=yes)
    install_file_metadata_deps_pip(ctx, yes=yes)
    install_file_metadata(ctx, yes=yes)

def install_file_metadata_deps_pip(ctx, yes=False):
    p   = params(yes=yes)
    job = [
    "sudo apt-get %(yes)s install perl openjdk-7-jre python-dev pkg-config libfreetype6-dev libpng12-dev liblapack-dev libblas-dev gfortran cmake libboost-python-dev liblzma-dev libjpeg-dev python-virtualenv" % p,
    ]
    install(ctx, job, yes=yes)

# Test through github
@task
def install_file_metadata_git(ctx, yes=False):
    install_pip(ctx, yes=yes)
    install_file_metadata_deps_pip(ctx, yes=yes)
    p   = params(yes=yes)
    job = [
    "sudo apt-get %(yes)s install git" % p,
    "sudo apt-get %(yes)s install libzbar-dev" % p,
    "git clone https://github.com/AbdealiJK/file-metadata.git",
    "cd file-metadata/; sudo pip install -r requirements.txt",
    "cd file-metadata/; python -c'import file_metadata; print file_metadata.__version__'",
    ]
    install(ctx, job, yes=yes)
    # need symlinks in core/ !

# Installation of pywikibot
@task
def install_pywikibot(ctx, yes=False):
    p   = params(yes=yes)
    job = [
    "sudo apt-get %(yes)s install git git-review" % p,
    "git clone --branch 2.0 --recursive https://gerrit.wikimedia.org/r/pywikibot/core.git",
    "cd core/; python pwb.py basic",    # issue: ctx.run stops after this line
    ]
    install(ctx, job, yes=yes)

# Test bot script
@task
def install_file_metadata_bot(ctx, yes=False):
    p   = params(yes=yes)
    job = [
    "sudo apt-get %(yes)s install libmagickwand-dev" % p,
    "cd core/; wget https://gist.githubusercontent.com/AbdealiJK/a94fc0d0445c2ad715d9b1b95ec2ba03/raw/492ef4076d5af74b4855fd26f6810f14cff07ec9/file_metadata_bot.py",
    ]
    install(ctx, job, yes=yes)
