#!/usr/bin/env python3

import sys
import io
import pandas as pd
import jaconv
from ..common import mecab_py

def parse(in_txt='in.txt', dic_csv='', dic_merge_split_yaml='', show_start_end=False):

    s = mecab_py.parse(in_txt=in_txt, raw=False, dic_merge_split_yaml=dic_merge_split_yaml)
    df_doc = pd.read_csv(io.StringIO(s))

    # 表層形,品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音,符号クラス
    df = pd.read_csv(dic_csv, sep=',', comment='#')

    xml = ''
    xml += '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<document>\n'
    xml += '<page>\n'
    xml += '<clause>\n'
    if show_start_end:
        xml += '<char class="CharStart" />\n'
        xml += '<char class="CharSpace" />\n'

    for i, ent in df_doc.iterrows():
        res = df[(df['表層形'] == ent['表層形']) 
               & (df['品詞'] == ent['品詞'])
               & (df['品詞細分類1'] == ent['品詞細分類1'])
               & (df['品詞細分類2'] == ent['品詞細分類2'])
               & (df['品詞細分類3'] == ent['品詞細分類3'])]

        if res.empty:
            res = df[(df['発音'] == ent['発音']) 
                   & (df['品詞'] == ent['品詞'])
                   & (df['品詞細分類1'] == ent['品詞細分類1'])
                   & (df['品詞細分類2'] == ent['品詞細分類2'])
                   & (df['品詞細分類3'] == ent['品詞細分類3'])]

        if res.empty:
            res = df[(df['発音'] == ent['発音']) & (df['品詞'] != '*')]

        if res.empty:
            word = ent['発音']
            ret = []
            for i in reversed(range(1 << (len(word)-1))):
                tmp_word = ''
                for j in range(0, len(word)):
                    tmp_word += word[j]
                    if i & (1 << j):
                        tmp_word += ','

                parts = tmp_word.split(',')

                tmp = []
                for part in parts:
                    if df[(df['発音'] == part) & (df['品詞'] == '*')].empty:
                        break
                else:
                    for part in parts:
                        tmp.append(df.query(f"発音 == '{part}'"))

                    ret.append(tmp)
            
            if len(ret) != 0:
                for c in ret[-1]:
                    cs = c['符号クラス'].values[0].split('|')
                    for cc in cs:
                        xml += f'<char class="{cc}" />\n'

        else:
            cs = res['符号クラス'].values[0].split('|')
            for cc in cs:
                xml += f'<char class="{cc}" />\n'

    if show_start_end:
        xml += '<char class="CharEnd" />\n'

    xml += '</clause>\n'
    xml += '</page>\n'
    xml += '</document>\n'

    return xml

if __name__ == '__main__':
    print(parse(in_txt='in.txt', dic_csv='waseda_dictionary.csv'))

