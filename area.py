#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import MDAnalysis as mda
import argparse
from sys import exit, stderr, stdout

def main(argv):
    return 0

parser = argparse.ArgumentParser(description="")
parser.add_argument('-c', type=str,
                    help='Archivo de coordenadas (.gro)')
parser.add_argument('-f', type=str,
                    help='Archivo de trayectoria (.trr)')
parser.add_argument('-n', type=str,
                    help='Archivo de ìndices (.ndx)')

# Parse arguments
args = parser.parse_args()
# Input checking
if not args.c.endswith('.gro'):
    print('ERROR: El archivo de coordenadas ('+args.c+') no termina en .gro',
          file=stderr)
    exit(1)
if not args.f.endswith('.trr'):
    print('ERROR: El archivo de trayectoria ('+args.f+') no termina en .trr',
          file=stderr)
    exit(1)
if not args.n.endswith('.ndx'):
    print('ERROR: El archivo de ìndices ('+args.n') no termina en .ndx',
          file)stderr)
    exit(1)


if __name__ = '__main__':
    exit(main(args))

