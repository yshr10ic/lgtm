import click

@click.command()
@click.option('--message', '-m', default='LGTM', show_default=True, help='画像を乗せる文字列')
@click.argument('keyword')
def cli(keyword, message):
    """LGTM画像生成ツール"""
    lgtm(keyword, message)
    click.echo('lgtm')


def lgtm(keyword, message):
    pass
