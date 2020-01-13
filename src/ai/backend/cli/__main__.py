import click
import pkg_resources


@click.group()
def main():
    '''Unified Command Line Interface for Backend.ai'''
    pass


entry_prefix = 'backendai_cli_v10'
for entrypoint in pkg_resources.iter_entry_points(entry_prefix):
    if entrypoint.name == "_":
        plugin = entrypoint.load().commands
        for command in plugin:
            main.add_command(plugin[command], name=command)
    else:
        main.add_command(entrypoint.load(), name=entrypoint.name)
