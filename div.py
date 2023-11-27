#模擬改良版除法器


''' 老師教的方法
#初始化
remainder |= dividend #放置被除數 在 remainder 的右半邊
remainder <<= 1
for _ in range(32):
    print(f'{remainder=:0>64b}')
    #remainder 左半邊 - divisor 放到 remainder 左半邊
    remainder = (((remainder >> 32) - divisor) << 32) | (remainder & 0xFFFFFFFF)

    #如果 remainder < 0:
    if (remainder >> 32) < 0:
        #restore remainder 左半邊 by adding divisor
        remainder = (((remainder >> 32) + divisor) << 32) | (remainder & 0xFFFFFFFF)

        #remainder 左移 1 bit
        remainder <<= 1
        continue

    remainder <<= 1
    remainder |= 1
print(f'{remainder=:0>64b}')


quotient = remainder & 0xFFFFFFFF
remainder = remainder >> 33
print(f'{remainder=}')
print(f'{quotient=}')
'''

import random

def simulate_div(divisor, dividend) -> (int, int):
    remainder = 0
    #print(f'{divisor=}', f'{dividend=}', f'{remainder=}')
    #初始化
    remainder |= dividend #放置被除數 在 remainder 的右半邊
    for _ in range(32):
        #print(f'{remainder=:0>64b}') 每次回圈開始remainder狀態
        #remainder 左移 1 bit
        remainder <<= 1
        #remainder 左半邊 - divisor 放到 remainder 左半邊
        remainder = (((remainder >> 32) - divisor) << 32) | (remainder & 0xFFFFFFFF)

        #如果 remainder < 0:
        if remainder < 0:
            #restore remainder 左半邊 by adding divisor
            remainder = (((remainder >> 32) + divisor) << 32) | (remainder & 0xFFFFFFFF)
            #remainder 左移 1 bit
            continue
        remainder |= 1
        
    #print(f'{remainder=:0>64b}') 完成迴圈後remainder狀態


    quotient = remainder & 0xFFFFFFFF
    remainder = remainder >> 32
    #print(f'{remainder=}')
    #print(f'{quotient=}')
    return (remainder, quotient)

def val_div(divisor, dividend) -> (int, int):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return (remainder, quotient)

def test_div():
    for _ in range(100000):
        divisor = random.randint(0, 2**32)
        dividend = random.randint(0, 2**32)
        remainder, quotient = simulate_div(divisor, dividend)
        val_remainder, val_quotient = val_div(divisor, dividend)
        assert remainder == val_remainder
        assert quotient == val_quotient

if __name__ == '__main__':
    test_div()