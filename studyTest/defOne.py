#!/usr/bin/env python3
#encoding:utf-8

def fibs(num):
  result=[0,1]
  for i in range(num-2):
      result.append(result[-2]+result[-1])
  return result

print(fibs(4))
