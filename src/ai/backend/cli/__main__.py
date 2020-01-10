import click
import pkg_resources


@click.group()
def main():
    '''Unified Command Line Interface for Backend.ai'''
    pass


entry_prefix = 'backendai_cli_v10'
for entrypoint in pkg_resources.iter_entry_points(entry_prefix):
    # plugin = entrypoint.load()
    # print(dir(entrypoint))
    # TODO: Each package requires different versions of some packages, we have to somehow unify them :)
    main.add_command(entrypoint.load(), name=entrypoint.name)
    break
