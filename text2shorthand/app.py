#!/usr/bin/env python3

from .common import context as ct

def run():
    context = ct.Context(shorthand='text2shorthand.shorthand.waseda.chars', 
        dic_csv='text2shorthand/shorthand/waseda/dictionary.csv',
        dic_merge_split_yaml='text2shorthand/shorthand/waseda/merge_split.yaml',
        width=150)
    context.parse_txt_file(in_txt='in.txt')
    context.typeset()
    context.write_svg_file('out.svg')
    context.write_pdf_file('out.pdf')
