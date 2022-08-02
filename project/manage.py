import click


@click.group()
def cli():
    pass


@cli.command()
def generate_config():

    if not click.confirm('Overwrite?'):
        raise click.Abort()


@cli.command()
def runserver():
    pass


if __name__ == '__main__':
    cli()
