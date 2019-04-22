import click
import os

from fir.commands.branch import branch
from fir.commands.commit import commit
from fir.commands.discard import discard
from fir.commands.follow import follow
from fir.commands.info import info
from fir.commands.merge import merge
from fir.commands.remote import remote
from fir.commands.replay import replay
from fir.commands.repo import repo
from fir.commands.squash import squash
from fir.commands.stage import stage
from fir.commands.stash import stash
from fir.commands.switch import switch
from fir.commands.sync import sync
from fir.commands.uncommit import uncommit
from fir.commands.unstage import unstage









@click.group()
def cli():
    pass


def get_env_vars(ctx, args, incomplete):
    # Completions returned as strings do not have a description displayed.
    for key in os.environ.keys():
        if incomplete in key:
            yield key


@cli.command(help='A command to print environment variables')
@click.argument("envvar", type=click.STRING, autocompletion=get_env_vars)
def cmd1(envvar):
    click.echo('Environment variable: %s' % envvar)
    click.echo('Value: %s' % os.environ[envvar])


cli.add_command(stash)
