import distutils.core
import errno
import locale
import os
import requests
import shutil
import tarfile
import zipfile
from io import BytesIO
from subprocess import call
import click
from click import progressbar
from plock.install import Installer
from plock.config import EXTENDS


def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
                print('Directory not copied. Error: %s' % e)


def _mkdir(newdir):
    """
       from http://code.activestate.com/recipes/82465-a-friendly-mkdir/
       works the way a good mkdir should :)
        - already exists, silently complete
        - regular file in the way, raise an exception
        - parent directory(ies) does not exist, make them as well
    """
    if os.path.isdir(newdir):
        pass
    elif os.path.isfile(newdir):
        raise OSError("a file with the same name as the desired "
                      "dir, '%s', already exists." % newdir)
    else:
        head, tail = os.path.split(newdir)
        if head and not os.path.isdir(head):
            _mkdir(head)
        # print "_mkdir %s" % repr(newdir)
        if tail:
            os.mkdir(newdir)


class Settings(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Piano(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.home = os.getenv("HOME")
        self.buildoutdir = os.path.join(self.home, ".buildout")
        self.extendsdir = os.path.join(self.home, ".buildout", "extends-cache")

    def create_extends_cache(self):
        _mkdir(self.extendsdir)
         
    def create_default_cfg(self):
        _mkdir(self.buildoutdir)
        # print "path:",self.buildoutdir
        cfg = """[buildout]
eggs-directory = {0}/eggs
download-cache = {0}/downloads
extends-cache = {0}/extends-cache"""
        self.buildoutcahe = path = "{}/.buildout".format(self.home)
        f = open('{}/{}'.format(path, 'default.cfg'), 'w+')
        f.write(cfg.format(path))
        f.close()
        self.eggs_dir = "{}/eggs".format(path)
        self.download_dir = "{}/downloads".format(path)

    def dependencycheck(self):
        startdir = os.getcwd()
        dirname = "install.plone.dependencies-master"
        os.chdir(".piano/{0}/{0}".format(dirname))
        call('./install_dependencies.sh',
             shell=True,
             executable='/bin/bash')
        os.chdir(startdir)

    def getdependencies(self):
        return  # temporarily disabled
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

    # def populatecache(self):
    #    #move eggs and downloads to $HOME/.buildout/
    #    copy("{}/eggs".format(self.buildoutdir),
    #         "{}/eggs".format(self.buildoutcache))

    def plockit(self):
        test = os.getenv("piano_test_mode", False)
        msg = "\nInitializing {} buildout environment using Plock".format(self.name)
        click.echo(click.style(msg, fg='green'))
        plock = PianoInstall()
        plock.install_plone(self.settings, test=test)


class PianoInstall(Installer):
    def create_cache(self, test=False):
        """
        Create cache directories for eggs and downloads
        """
        # override self.directory
        home = os.getenv("HOME")
        self.cachepath = "{}/.buildout".format(home)

        if test:
            return
        path_to_installer = self.download_unifiedinstaller()
        print("Unpacking installer...")
        tar = tarfile.open(path_to_installer)
        tar.extractall(self.directory)
        tar.close()

        package_folder = os.path.basename(path_to_installer)
        package_folder = package_folder.split('.tgz')[0]
        package_folder = os.path.join(self.directory, package_folder)
        path_to_cache = "{}/packages/buildout-cache.tar.bz2".format(package_folder)
        print("Unpacking cache...")
        tar = tarfile.open(path_to_cache)
        tar.extractall(self.directory)
        tar.close()

        buildout_cache = "%s/buildout-cache" % self.directory

        print("Installing eggs...")
        dst_eggs = "%s/eggs" % self.cachepath
        src_eggs = "%s/eggs" % buildout_cache
        distutils.dir_util.copy_tree(src_eggs, dst_eggs)

        print("Installing cmmi & dist...")
        dst_downloads = "%s/downloads" % self.cachepath
        src_downloads = "%s/downloads" % buildout_cache
        distutils.dir_util.copy_tree(src_downloads, dst_downloads)

    def install_plone(self, args, test=False):
        """
        Install Plone with Buildout
        """

        if args.list_addons:
            if args.install_dir:
                print("Usage: plock -l")
                exit()
            locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
            if args.raw:
                self.list_addons(raw=True)
            else:
                self.list_addons()
            exit()
        if args.raw:
            print("Usage: plock --list-addons --raw")
            exit()

        if args.install_dir:
            self.directory = args.install_dir
        else:  # Quit if no install dir
            print("Usage: plock <DIR>")
            exit()

        # Create install directory if it does not exist
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)

        if not args.no_venv:
            self.create_venv()
        if not args.no_buildout:
            self.install_buildout()
        if args.unified or args.unified_only:
            self.create_cache(test=test)
        if args.extra:
            self.create_cfg((EXTENDS, args.extra))
        else:
            self.create_cfg((EXTENDS, ))
        if args.unified or args.unified_only:
            # don't add a download_cache()
            # self.add_download_cache()
            self.clean_up(test=test)

        if args.unified_only:
            print("Only downloading installer cache, bye!")
            exit()

        if args.add_on:
            print("Installing addons...")
            self.install_addons(args)

        self.run_buildout(args, test=test)
        print("Done, now run:\n\n%s/bin/plone fg\n" % self.directory)


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
        extra="http://goo.gl/Rp2Uk8",
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
            'create_default_cfg',
            'create_extends_cache',
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
