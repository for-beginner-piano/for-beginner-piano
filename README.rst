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
For example on Debian or Ubuntu you will need to run the following:

::

    sudo apt-get update
    sudo apt-get install build-essential libssl-dev libxml2-dev libxslt1-dev libbz2-dev zlib1g-dev -y
    sudo apt-get install python-dev python-setuptools python-virtualenv libjpeg62-dev wv poppler-utils -y


Quick Install
-------------

To install `piano` quickly, run the following commands:

::

    wget -qO- goo.gl/NmFSel | bash
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


