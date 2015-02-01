import os
import requests
import zipfile
from io import BytesIO
from subprocess import call
import click
from click import progressbar
from plock.install import Installer


class Settings(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Piano(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def dependencycheck(self):
        startdir = os.getcwd()
        dirname = "install.plone.dependencies-master"
        os.chdir(".piano/{0}/{0}".format(dirname))
        call('./install_dependencies.sh',
             shell=True,
             executable='/bin/bash')
        os.chdir(startdir)

    def getdependencies(self):
        url = "https://github.com/collective/install.plone.dependencies/archive/master.zip"
        request = requests.get(url)
        with zipfile.ZipFile(BytesIO(request.content)) as zf:
            # from http://stackoverflow.com/questions/12886768/how-to-unzip-file-in-python-on-all-oses
            for member in zf.infolist():
                # Path traversal defense copied from
                # http://hg.python.org/cpython/file/tip/Lib/http/server.py#l789
                words = member.filename.split('/')
                path = ".piano"
                for word in words[:-1]:
                    drive, word = os.path.splitdrive(word)
                    head, word = os.path.split(word)
                    if word in (os.curdir, os.pardir, ''):
                        continue
                    path = os.path.join(path, word)
                    zf.extract(member, path)
        self.dependencycheck()

    def plockit(self):
        test = os.getenv("piano_test_mode", False)
        print("Initializing {} buildout environment using Plock".format(self.name))
        plock = Installer()
        plock.install_plone(self.settings, test=test)


@click.group()
@click.pass_context
def cli(name):
    pass


@cli.command()
@click.argument('name')
def newbuildout(name):
    """initialize a plone site buildout development environment"""
    settings = Settings(
        add_on=False,
        extra=False,
        install_dir=name,
        list_addons=False,
        no_buildout=False,
        no_unified=False,
        no_venv=False,
        raw=False,
        unified=True,
        unified_only=False,
        )
    _piano = Piano(name=name,
                   settings=settings)

    cmds = ['getdependencies',
            'plockit']
    with progressbar(cmds) as bar:
        for cmd in bar:
            getattr(_piano, cmd)()


@cli.command()
@click.argument('name')
def newaddon(name):
    """Create a new plone addon"""
    print("Creating an addon called {}".format(name))
    print("this doesn't actually do anything yet, but it will")
