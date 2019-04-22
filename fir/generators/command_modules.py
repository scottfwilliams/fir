from fir.generators import commands

from os.path import abspath, dirname, isdir, join


command_module_tmpl = """import click


@click.group(help='A group that holds a subcommand')
def {0}():
    pass


@{0}.command(name="list", help='Choose a user')
@click.argument("somearg", type=click.STRING)
def _list(somearg):
    pass

"""


def run():
    parent_dir = dirname(abspath(__file__))
    project_root_dir = dirname(parent_dir)
    commands_pkg_dir = join(project_root_dir, "commands")
    print("command modules package path:", commands_pkg_dir)
    assert isdir(commands_pkg_dir)
    for cmd in commands:
        command_module_path = join(commands_pkg_dir, "{}.py".format(cmd))
        print("Creating {}".format(command_module_path))
        with open(command_module_path, "w") as mod_f:
            stmts = command_module_tmpl.format(cmd)
            mod_f.write(stmts)


if __name__ == "__main__":
    run()
