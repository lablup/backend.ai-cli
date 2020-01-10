import click
import pkg_resources


@click.group()
def main():
    '''Unified Command Line Interface for Backend.ai'''
    pass


commands = {}
entry_prefix = 'backendai_cli_v10'
for entrypoint in pkg_resources.iter_entry_points(entry_prefix):
    # plugin = entrypoint.load()
    # print(dir(entrypoint))
    commands[entrypoint.name] = entrypoint.load()
    break
for command in commands:
    main.add_command(commands[command], name=command)
