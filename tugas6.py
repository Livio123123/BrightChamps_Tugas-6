
import math

while True:
    print("1. akar ")
    print("2. perpangkatan")
    print("3. keluar")

    a = input("masukan pilihan anda -> ")

    if a=="1":
        angka1 = int(input("angka1-> "))
        angka2 = int(input("angka2-> "))
        print(math.sqrt(angka1))
        print(math.sqrt(angka2))

    if a=="2":
        angka1 = int(input("angka awal-> "))
        angka2 = int(input("angka pangkat-> "))
        print(math.pow(angka1,angka2))

    if a=="3":
        print("sampai jumpa")
        break





