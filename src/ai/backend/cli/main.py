import click

from .extensions import AliasGroup


@click.group(
    cls=AliasGroup,
    context_settings={
        'help_option_names': ['-h', '--help'],
    },
)
def main() -> click.Group:
    '''Unified Command Line Interface for Backend.ai'''
    pass
