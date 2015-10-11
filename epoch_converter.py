#!/usr/bin/env python
import argparse
import time

parser = argparse.ArgumentParser(description='Converts Epoch Time to localtime')

parser.add_argument('epochtime', type=float, nargs='+', help='Example: 1444237762.53936')
args = parser.parse_args()

for epoch in args.epochtime:
	print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(epoch))))
