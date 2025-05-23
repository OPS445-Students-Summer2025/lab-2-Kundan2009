#!/usr/bin/env python3

#Author: Kundan Patel
#Author ID: 157024225
#Date created: 2025/05/23

import sys

if len(sys.argv)>1:
    timer =int(sys.argv[1])
else:
    timer=3
while timer!=0:
    print(timer)
    timer=timer-1

print('blast off!')
