#!/usr/bin/env python
# coding: utf-8

import sys
from pathlib import Path
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Convert a gene list into a bed file.')

#文字列オプション
parser.add_argument('species', type=str, help='human or mouse')
#文字列オプション
parser.add_argument('genelist', type=str, help='a gene list file')
#文字列オプション
parser.add_argument('output', type=str, help='output file')
#数値 オプション
parser.add_argument('-m','--mergin', type=int, help='mergin length', default=0)


args = parser.parse_args()

print(args.species)
if args.species == 'mouse':
    f_bed = str(Path(__file__).resolve().parent)+'/data/mouse.bed.gz'
elif args.species == 'human':
    f_bed = str(Path(__file__).resolve().parent)+'/data/human.bed.gz'
else:
    print('specify human or mouse!')
    sys.exit()

# print(Path(__file__).resolve().parent)
df_bed = pd.read_csv(f_bed, sep='\t', header=None)
# print(df_bed.head())

list_genes = list(pd.read_csv(args.genelist, header=None)[0])
# print(list_genes)

df_q = df_bed[df_bed[3].isin(list_genes)]
df_q[1] = df_q[1] - args.mergin
df_q[2] = df_q[2] + args.mergin

df_q.to_csv(args.output, header=None, index=None, sep='\t')
