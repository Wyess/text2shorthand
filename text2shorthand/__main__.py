#!/usr/bin/env python3

import argparse
import text2shorthand.app as app

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Text-to-shorthand converter') 
    parser.add_argument('input', help='Input text file')
    parser.add_argument('output', help='Output file (.svg|.eps|.pdf)')
    parser.add_argument('shorthand', help='Shorthand method (nakane|sangiin|shugiin|waseda')
    args = parser.parse_args()
    app.run() 
