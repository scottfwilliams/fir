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


cli.add_command(branch)
cli.add_command(commit)
cli.add_command(discard)
cli.add_command(follow)
cli.add_command(info)
cli.add_command(merge)
cli.add_command(remote)
cli.add_command(replay)
cli.add_command(repo)
cli.add_command(squash)
cli.add_command(stage)
cli.add_command(stash)
cli.add_command(switch)
cli.add_command(sync)
cli.add_command(uncommit)
cli.add_command(unstage)
