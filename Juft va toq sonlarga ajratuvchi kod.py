# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 16:47:35 2025

@author: User
"""

#                Juft va Toq sonlar 

sonlar=list(range(1,50))
toq_sonlar=[]
juft_sonlar=[]
for son in sonlar:
    if son%2==0:
        juft_sonlar.append(son)
    else:
        toq_sonlar.append(son)
print(toq_sonlar)
print(juft_sonlar)
