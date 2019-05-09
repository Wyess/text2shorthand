#!/usr/bin/env python3

import importlib
import sys
import io
import pyx
import xml.etree.ElementTree as ET
from text2shorthand.common import mecab_result_to_xml
from text2shorthand.common.char import Char
from text2shorthand.common.point import Point as P, PPoint as PP

class Context():
    def __init__(self, shorthand='', dic_csv='', dic_merge_split_yaml='', width=243, height=333/2):
        try:
            self.sh = importlib.import_module(shorthand)
        except ImportError:
            print("Context: Could not import the shorthand module. Exiting...")
            sys.exit(1)

        pyx.unit.set(defaultunit='mm')
        
        self.dic_csv = dic_csv
        self.dic_merge_split_yaml = dic_merge_split_yaml
        self.canvas = pyx.canvas.canvas()
        self.width = width
        self.height = height

    def parse_txt_file(self, in_txt='in.txt'):
        xml = mecab_result_to_xml.parse(in_txt=in_txt, 
            dic_csv=self.dic_csv,
            dic_merge_split_yaml=self.dic_merge_split_yaml)
        self.parse_xml_file(xml=io.StringIO(xml))

    def parse_xml_file(self, xml='in.xml'):
        self.chars = [Char()]

        tree = ET.parse(xml)
        document = tree.getroot()

        for page in document:
            for clause in page:
                for char in clause:
                    params, delim, charclass = '', '', ''
                    for a, v in char.attrib.items():
                        if a == 'class':
                            charclass = v
                        else:
                            params += f'{delim}{a}={v}'
                            delim = ', '
                    try:
                        self.chars.append(eval(f'self.sh.{charclass}({params})'))
                    except AttributeError:
                        pass

        self.chars.append(Char())

    def _connect_all(self):
        for before, char, after in zip(self.chars[:-2], self.chars[1:-1], self.chars[2:]):
            char.connect(before, after)

    def _set_form_all(self):
        for i in range(2):
            for before, char, after in zip(self.chars[:-2], self.chars[1:-1], self.chars[2:]):
                char.set_form()

    def _set_next_head_all(self):
        right = 0
        bottom = 0
        centerline = -self.height / 6
        self.chars[1].head = P(0, centerline + self.chars[1].offset_from_centerline)

        for char in self.chars[1:-1]:
            if char.name == 'space':
                char.to_centerline = False
                char.abs = True

                if right + 10 > self.width:
                    right = 0
                    centerline = min(buttom, centerline - self.height / 5)

                    char.pos = P(right, centerline + char.after.offset_from_centerline)
                else:
                    char.pos = P(right + 10, centerline + char.after.offset_from_centerline)

            char.set_next_head()

            right = max(right, char.get_right_edge() + char.head.x)
            buttom = min(bottom, char.get_bottom() + char.head.y)

    def _draw_all(self):
        idx = 0
        for i, char in enumerate(self.chars):
            if char.name == 'space':
                for j in range(idx, i):
                    if self.chars[j].drawn and (self.chars[j].drawn_extra == False):
                        self.chars[j].draw_extra(canvas=self.canvas)
                else:
                    idx = i
            char.draw(self.canvas)

        for i, char in enumerate(self.chars):
            print(f"{char.name}: {len(char.paths) + len(char.paths_extra)}")
    
    def typeset(self):
        self._connect_all()
        self._set_form_all()
        self._set_next_head_all()
        self._draw_all()

    def write_svg_file(self, out_file='out.svg'):
        self.canvas.writeSVGfile(out_file)

    def write_eps_file(self, out_file='out.eps'):
        self.canvas.writeEPSfile(out_file)

    def write_pdf_file(self, out_file='out.pdf'):
        self.canvas.writePDFfile(out_file)

if __name__ == '__main__':
    context = Context(shorthand='waseda_shorthand', width=150)
    context.parse_xml_file('out.xml')
    context.typeset()
    context.write_svg_file('out.svg')
