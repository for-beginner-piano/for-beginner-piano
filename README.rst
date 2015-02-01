piano
============

Piano. Beginner friendly Plone development.

Installation
=================

We prefer recommend `pipsi`. 
(Here are installation instructions https://github.com/mitsuhiko/pipsi#readme.)

Once you have pipsi run::

    pipsi install piano
    
OR::

    pip install piano


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

Before using Piano be sure to upgrade setuptools
::

     ~/.local/venvs/piano/bin/pip install -U setuptools
 
Creating a Plone add-on
-------------------------
::

    piano newaddon myaddon
    
