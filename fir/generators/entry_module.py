#!/bin/python

from os.path import abspath, dirname, isdir, join

from fir.generators import commands


entry_module_tmpl = """import click
import os

{cmd_import_stmts}

@click.group()
def cli():
    pass


def get_env_vars(ctx, args, incomplete):
    # Completions returned as strings do not have a description displayed.
    for key in os.environ.keys():
        if incomplete in key:
            yield key


{adds_cmds_to_cli}"""

# E.g. "from fir.commands.branch import branch"
import_cmd_tmplt = "from fir.commands.{0} import {1}\n"

# E.g. "cli.add_command(stash)"
add_cmd_tmplt = "cli.add_command({0})\n"


def run():
    parent_dir = dirname(abspath(__file__))
    pkg_root_dir = dirname(parent_dir)
    print("fir root package path:", pkg_root_dir)
    assert isdir(pkg_root_dir)

    import_statements = []
    cli_add_command_statements = []
    for cmd in commands:
        # add import statement for the module to the list
        import_stmt = import_cmd_tmplt.format(cmd, cmd)
        import_statements.append(import_stmt)
        add_stmt = add_cmd_tmplt.format(cmd)
        cli_add_command_statements.append(add_stmt)
    import_mods = "".join(import_statements)
    add_mods = "".join(cli_add_command_statements)
    entry_module_cntnt = entry_module_tmpl.format(cmd_import_stmts=import_mods,
                                                  adds_cmds_to_cli=add_mods)
    entry_module_path = join(pkg_root_dir, "entry.py")
    with open(entry_module_path, "w") as mod_f:
        mod_f.write(entry_module_cntnt)


if __name__ == "__main__":
    run()
