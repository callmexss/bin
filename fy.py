"""
File  :    fy.py
Author:    ershan
mail  :    ershan_coding@outlook.com
desc  :    A quick translation tool.
"""

import click
import clipboard
import translators as ts


def translate(query, to_language):
    for provider in [ts.youdao, ts.google, ts.bing, ts.caiyun]:
        if ret := provider(query, to_language=to_language):
            return ret


@click.command()
@click.argument("QUERY", default="")
def fy(query):
    if not query:
        query = clipboard.paste()

    to_lang = "en" if any([not x.isascii() for x in query]) else "zh"
    result = translate(query, to_lang)
    print(result)
    clipboard.copy(result)
    input()


if __name__ == "__main__":
    fy()
