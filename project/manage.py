import click
import os


@click.group()
def cli():
    pass


@cli.command()
def generate_config():

    if not click.confirm('Overwrite?'):
        raise click.Abort()


@cli.command()
def startapp():
    """Start streamlit app on localhost:8501"""
    os.system("streamlit run app/app.py --server.address 'localhost'")


if __name__ == '__main__':
    cli()
