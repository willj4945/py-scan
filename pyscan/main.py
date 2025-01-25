import click
import pyscan.commands

@click.group()
def cli():
    pass

cli.add_command(pyscan.commands.scan)


if __name__ == "__main__":
    cli()
