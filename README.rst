piano
=====

.. image:: https://travis-ci.org/for-beginner-piano/for-beginner-piano.svg?branch=master

Piano. Beginner friendly Plone development.

.. warning:: This is very much ALPHA!. In the spirit of release early, here it is.

Installation
============

Prerequisites
-------------
You should have the build tools and Plone dependencies installed.

If you're on Debian or Ubuntu with sudo privileges, We've simplified this for you.
Just run one of the commands below:

For Debian::

    wget -qO- for-beginner-piano.github.io/debian | bash

For Ubuntu::

    wget -qO- for-beginner-piano.github.io/ubuntu | bash


Quick Install
-------------

To install `piano` quickly, run the following commands:

::

    wget -qO- for-beginner-piano.github.io | bash
    source ~/.bashrc

This will use `pipsi` to install the relevant packages in user space.
It also ensures that piano is using the most up-to-date version of
setuptools.

Longer Install
--------------

We prefer and recommend `pipsi`. 

Once you have pipsi, run:

::

    pipsi install for-beginner-piano
    ~/.local/venvs/for-beginner-piano/bin/pip install -U setuptools

.. note:: It is important to ensure that the latest version of setuptools is installed
          for this reason we run the second command above.

    
Usage
=====

To create a new Plone buildout project
--------------------------------------

Use the subcommand `newbuildout` to create a buildout project.

For example, if your project will be called `my-plone-site`:

::

    piano newbuildout my-plone-site
    
.. note:: A buildout is a folder which holds all the settings required to build
          and deploy a Plone site

You'll see output similar to this:

::

    Creating virtualenv... (my-plone-site)
    Installing Buildout...
    Downloading installer (https://launchpad.net/plone/4.3/4.3.3/+download/Plone-4.3.3-UnifiedInstaller.tgz)
    Unpacking installer...
    Unpacking cache...
    Installing eggs...
    Installing cmmi & dist...
    Configuring cache...
    Running Buildout...

Installing non default versions
-------------------------------

For the latest Plone 5 site you could do the following::

    wget for-beginner-piano.github.com/p5; source p5
    piano newbuildout plone5-site
    
for the latest Plone 4 site::

    wget for-beginner-piano.github.com/p4; source p4
    piano newbuildout plone4-site

OR if you prefer the more manual approach, here's an example of installing 
Plone 5 (note the use of the special PIANO_ environment variables::

    export PIANO_EXTENDS=https://raw.github.com/plock/pins/master/plone-5-0
    export PIANO_UNIFIEDINSTALLER_URL=https://launchpad.net/plone/5.0/5.0a2/+download/Plone-5.0a2-UnifiedInstaller.tgz
    export PIANO_UNIFIEDINSTALLER_DIR=Plone-5.0a2-UnifiedInstaller

then run::

    piano newbuildout myplone5

Creating a Plone add-on
-----------------------

This is not working yet, but:

::

    piano newaddon myaddon
    
(coming soon, this command doesn't work yet)

Credits
-------

piano is created and managed by David Bain, it is built on top of plock which was
created and maintained by Alex Clark.


