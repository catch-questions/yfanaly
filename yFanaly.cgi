#!/bin/python3.6
# -*- coding: utf-8 -*-

import pandas as pd
import csv

url1 = 'https://info.finance.yahoo.co.jp/ranking/?kd=1'
dfs1 = pd.read_html(url1)
url11 = 'https://info.finance.yahoo.co.jp/ranking/?kd=1&p=2'
dfs11 = pd.read_html(url11)

url2 = 'https://info.finance.yahoo.co.jp/ranking/?kd=9'
dfs2 = pd.read_html(url2)
url22 = 'https://info.finance.yahoo.co.jp/ranking/?kd=9&p=2'
dfs22 = pd.read_html(url22)

# url3 = 'https://info.finance.yahoo.co.jp/ranking/?kd=19'
# dfs3 = pd.read_html(url3)
# url33 = 'https://info.finance.yahoo.co.jp/ranking/?kd=19&p=2'
# dfs33 = pd.read_html(url33)

# url4 = 'https://info.finance.yahoo.co.jp/ranking/?kd=21'
# dfs4 = pd.read_html(url4)
# url44 = 'https://info.finance.yahoo.co.jp/ranking/?kd=21&p=2'
# dfs44 = pd.read_html(url44)

matched_list = []

dfs1_list = []
dfs2_list = []
# dfs3_list = []
# dfs4_list = []

dfs11_list = []
dfs22_list = []
# dfs33_list = []
# dfs44_list = []


dfs1Arr = str(dfs1[0:50][0]).splitlines()
dfs11Arr = str(dfs11[0:50][0]).splitlines()

for elm in dfs11Arr:
	dfs1Arr.append(elm)

dfs2Arr = str(dfs2[0:50][0]).splitlines()
dfs22Arr = str(dfs22[0:50][0]).splitlines()

for elm in dfs22Arr:
	dfs2Arr.append(elm)

# dfs3Arr = str(dfs3[0:50][0]).splitlines()
# dfs33Arr = str(dfs33[0:50][0]).splitlines()

# for elm in dfs33Arr:
# 	dfs3Arr.append(elm)

# dfs4Arr = str(dfs4[0:50][0]).splitlines()
# dfs44Arr = str(dfs44[0:50][0]).splitlines()

# for elm in dfs44Arr:
# 	dfs4Arr.append(elm)

for str in dfs1Arr:
	if str != "":
		lisStr = str.split()[2]
		if str.split()[2].isdigit():
			dfs1_list.append(lisStr)

for str in dfs2Arr:
	if str != "":
		lisStr = str.split()[2]
		if str.split()[2].isdigit():
			dfs2_list.append(lisStr)

# for str in dfs3Arr:
# 	if str != "":
# 		lisStr = str.split()[2]
# 		if str.split()[2].isdigit():
# 			dfs3_list.append(lisStr)

# for str in dfs4Arr:
# 	if str != "":
# 		lisStr = str.split()[2]
# 		if str.split()[2].isdigit():
# 			dfs4_list.append(lisStr)


df1_set = set(dfs1_list)
df2_set = set(dfs2_list)
# df3_set = set(dfs3_list)
# df4_set = set(dfs4_list)

matched_list = list((df1_set & df2_set))


# matched_list = list((df1_set & df2_set) | (df1_set & df3_set) | (df1_set & df4_set))

print(matched_list)


titleL = matched_list
titleS = list()

for nStr in titleL:
	aStr = nStr.replace('\n','')
	titleS.append(aStr)

with open('yFcsv.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(titleS)

