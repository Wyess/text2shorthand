#!/usr/bin/env python3

from .common import context as ct

def run(shorthand=None, in_txt=None, out=None):
    if shorthand in {'nakane', 'sangiin', 'shugiin', 'svsd', 'waseda'}:
        context = ct.Context(shorthand=f'text2shorthand.shorthand.{shorthand}.chars',
            dic_csv=f'text2shorthand/shorthand/{shorthand}/dictionary.csv',
            dic_merge_split_yaml=f'text2shorthand/shorthand/{shorthand}/merge_split.yaml',
            width=150)
        context.parse_txt_file(in_txt=in_txt)
        context.typeset()
        context.write_log_xml(out_xml='log.xml')
        if out.endswith('.svg'):
            context.write_svg_file(out)
        elif out.endswith('.pdf'):
            context.write_pdf_file(out)
        elif out.endswith('.eps'):
            context.write_eps_file(out)
        else:
            context.write_pdf_file(out)
    else:
        print(f'{shorthand} is not supported.')
