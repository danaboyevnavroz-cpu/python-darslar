# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 13:49:34 2026

@author: User
"""

#     #while list
    
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n = 1  # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n += 1
#     if takrorlash != "ha":
#         break

# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())
    

#     #while dict
    
# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)

#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")
    
    
#     #remove
    
# cars = ["lacetti", "nexia", "toyota", "nexia", "audi", "malibu", "nexia", "lacetti"]
# car = "lacetti"
# while car in cars:
#     cars.remove(car)

# print(cars)


#     #pop
    
# talabalar = ["hasan", "husan", "olim", "botir"]
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho)
    
#     #misol
    
# savat = []
# while True:
#     mahsulot = input("Savatga mahsulot qo'shing:")
#     savat.append(mahsulot)
#     javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
#     if javob != "ha":
#         break
# print("Dastur tugadi!")




























