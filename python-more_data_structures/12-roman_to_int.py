#!/usr/bin/python3
def to_subtract(list_num):
    S = 0
    M = max(list_num)

    for n in list_num:
        if M > n:
            S += n

    return (M - S)


def roman_to_int(strings):
    if not strings:
        return 0

    if not isinstance(strings, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for ch in strings:
        for r_num in list_keys:
            if r_num == ch:
                if rom_n.get(ch) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [rom_n.get(ch)]
                else:
                    list_num.append(rom_n.get(ch))

                last_rom = rom_n.get(ch)

    num += to_subtract(list_num)

    return (num)
