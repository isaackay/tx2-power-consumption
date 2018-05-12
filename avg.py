#!/usr/bin/python3

import sys
import os

def average_from_path(path):
	sum = 0.0
	cnt = 0
	with open(path, 'r') as f:
		for line in f:
			sum += float(line)
			cnt += 1
	return sum / cnt

if __name__ == "__main__":
	path = sys.argv[1]
	baseline_path = sys.argv[2]
	print(average_from_path(path) - average_from_path(baseline_path))
