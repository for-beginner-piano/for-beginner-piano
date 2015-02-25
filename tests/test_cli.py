import os
import pytest
from click.testing import CliRunner
from piano import cli
import shutil


@pytest.fixture
def runner():
    return CliRunner()


def initcommand(runner, command, arg):
    os.putenv("piano_test_mode", "1")
    name = arg
    if os.path.exists(name):
        shutil.rmtree(name)
    result = runner.invoke(cli.cli, [command, name])
#    assert result.exit_code == 0
    assert not result.exception
    expected = result.output.split('\n')[3]
    assert expected == 'Initializing {} buildout environment using Plock'.format(name)
    shutil.rmtree(name)


def test_cli(runner):
    result = runner.invoke(cli.cli)
    assert result.exit_code == 0
    assert not result.exception
'''    assert result.output == """Usage: piano [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  newaddon     Create a new plone addon
  newbuildout  initialize a plone site buildout development..."""
'''


def test_cli_newbuildout(runner):
    initcommand(runner, "newbuildout", "plone-site")


def test_cli_init(runner):
    initcommand(runner, "init", "plone-site")
