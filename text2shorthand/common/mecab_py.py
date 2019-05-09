#!/usr/bin/env python3

import re
import MeCab
import yaml

def parse(in_txt='in.txt', raw=False, dic_merge_split_yaml=''): 
    with open(in_txt, 'r') as f:
        s = f.read()

    m = MeCab.Tagger()
    s = m.parse(s)
    s = re.sub('\t', ',', s)
    s = '表層形,品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音,符号クラス\n' + s

    if raw:
        return s

    with open(dic_merge_split_yaml) as stream:
        docs = yaml.safe_load_all(stream)
        dic = next(docs)

        for entry in dic:
            target = r'\S*?\n'.join(entry[:-1] + [''])
            s = re.sub(rf"^{target}", f"{entry[-1]}\n", s, flags=re.MULTILINE|re.DOTALL)
        
    return s

if __name__ == '__main__':
    print(parse('in.txt'), end='')
