import sys
if sys.version_info < (3, 8, 0):
    from importlib_metadata import entry_points
else:
    from importlib.metadata import entry_points  # type: ignore


def load_entry_points(install_target):
    entry_prefix = 'backendai_cli_v10'
    for entrypoint in entry_points().get(entry_prefix, []):
        if entrypoint.name == "_":
            cmd_group = entrypoint.load()
            cmdset = cmd_group.commands
            for cmd_name, cmd_obj in cmdset.items():
                install_target.add_command(cmd_obj, name=cmd_name)
        else:
            prefix, _, subprefix = entrypoint.name.partition(".")
            if not subprefix:
                subcmd = entrypoint.load()
                install_target.add_command(subcmd, name=prefix)
            else:
                subcmd = entrypoint.load()
                install_target.commands[prefix].add_command(subcmd, name=subprefix)
