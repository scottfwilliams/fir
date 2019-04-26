import click


@click.group(help='A group that holds a subcommand')
def commit():
    pass


@commit.command(name="list", help='Choose a user')
@click.argument("somearg", type=click.STRING)
def _list(somearg):
    pass

