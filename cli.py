import click
import tsol

@click.group()
def cli():
	pass

# registers a new username
@cli.command()
@click.argument('name')
def echo(name):
	print(name)