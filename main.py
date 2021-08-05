import click


@click.command()
@click.option('--build', help='Number of greetings.')
@click.option('--name',
              help='The person to greet.')
def cli(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter,no-value-for-parameter
    cli()
