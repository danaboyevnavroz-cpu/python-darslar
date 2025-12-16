# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 16:48:53 2025

@author: User
"""
        # Tub sonlarni aniqlovchi dastur !

son=int(input("Biror son kiriting>>> "))
a=[]
for i in range(1,son+1):
    if son%i==0:
        a.append(i)
if len(a)==2:
    print("tub son")
else:
    print("tub son emas")
        
    