import os
from pathlib import Path

import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("-f", "--filepath", type=str, default="config.json", help="Output config file path")
def generate_config(filepath):

    filepath = Path(filepath)

    if filepath.exists():
        if not click.confirm(f"{filepath} already exists, Overwrite?"):
            raise click.Abort()
        else:
            filepath.unlink()


@cli.command()
def startapp():
    """Start streamlit app on localhost:8501"""
    os.system("streamlit run app/app.py --server.address 'localhost'")


if __name__ == "__main__":
    cli()
