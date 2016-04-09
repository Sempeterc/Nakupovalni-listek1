# -*- coding: utf-8 -*

seznam = []

while True:
    vnos = str(raw_input ("zelite dodati kak izdelek v seznam (da/ne):"))
    if vnos == "da":
        seznam.append(raw_input("prosim napisite izdelek, ki ga zelite dodati na seznam:"))
        print seznam
    elif vnos == "ne":
        print seznam
        break





