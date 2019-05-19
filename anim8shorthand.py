#!/usr/bin/env python3

import math
import argparse
import xml.etree.ElementTree as ET
from svgpathtools import svg2paths2

parser = argparse.ArgumentParser(description='Add drawing animation to an SVG file')
parser.add_argument('input', help='Input SVG file')
parser.add_argument('--output', default='out_anim.svg', help='Output SVG file')
parser.add_argument('--duration', type=float, default=30.0, help='Total duration in seconds')
parser.add_argument('--classname', default='path', help='A class name that will be used in the output SVG')
args = parser.parse_args()

in_svg = args.input
out_svg = args.output 
total_duration_s = args.duration 
class_name = args.classname 

paths, attributes, svg_attributes = svg2paths2(in_svg)
path_lengths = [p.length() for p in paths]
total_path_length = sum(path_lengths)

ET.register_namespace('', 'http://www.w3.org/2000/svg')
tree = ET.parse(in_svg, ET.XMLParser(encoding='utf-8'))
root = tree.getroot()

speed_s = total_path_length / total_duration_s
start_ms = 0
style = ''

for i, path in enumerate(root.iter('{http://www.w3.org/2000/svg}path')):
    dash = math.ceil(path_lengths[i])
    gap = dash + 2
    offset = dash + 1
    path.set('class', f"{class_name}_{i}")

    duration_ms = math.ceil(path_lengths[i] / speed_s * 1000)
    end_ms = start_ms + duration_ms

    style += f".{class_name}_{i}{{" 
    style += f"stroke-dasharray:{dash} {gap};"
    style += f"stroke-dashoffset:{offset};"
    style += f"animation:{class_name}_draw {duration_ms}ms linear {start_ms}ms forwards;}}"

    start_ms = end_ms

style += f"@keyframes {class_name}_draw" "{100%{stroke-dashoffset:0;}}"

style_el = ET.Element('{http://www.w3.org/2000/svg}style')
style_el.text = style
root.append(style_el)

tree.write(out_svg)
