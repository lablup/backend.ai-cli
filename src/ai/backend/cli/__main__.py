import click


@click.group()
def main():
    pass


@main.command()
def mgr():
    '''Manager CLI'''
    click.echo(f"Hello Manager")


@main.command()
def ag():
    '''Agent CLI'''
    click.echo(f"Hello Agent")
