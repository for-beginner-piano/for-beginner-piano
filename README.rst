piano
============

.. image:: https://travis-ci.org/for-beginner-piano/for-beginner-piano.svg?branch=master

Piano. Beginner friendly Plone development.

Installation
=================

We prefer and recommend `pipsi`. 
(Here are installation instructions https://github.com/mitsuhiko/pipsi#readme.)

Once you have pipsi run::

    pipsi install for-beginner-piano
    ~/.local/venvs/for-beginner-piano/bin/pip install -U setuptools

.. note:: It is important to ensure that the latest version of setuptools is installed
          for this reason we run the second command above.

Usage
=============

To create a new Plone buildout project
------------------------------------------
::

    piano newbuildout my-plone-site
    
.. note: A buildout is a folder which holds all the settings required to build
and deploy a Plone site

You'll see output similar to this::

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
-------------------------
::

    piano newaddon myaddon
    
