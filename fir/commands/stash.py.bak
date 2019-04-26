import click


@click.group(help='A group that holds a subcommand')
def stash():
    pass


@stash.command(name="list", help='Choose a user')
@click.argument("user", type=click.STRING)
def _list(user):
    click.echo('Chosen user is %s' % user)
