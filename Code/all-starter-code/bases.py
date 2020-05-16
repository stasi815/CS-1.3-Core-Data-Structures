#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, f'base is out of range: {base}'

    # Decode digits from any base (2 up to 36)
    # for each digit, use the position or the index an the base to digit * base ** index

    decimal_num = 0
    digits = digits[::-1]

    for i in range(len(digits)):
        digit = int(digits[i], base=base)
        decimal_num += digit * base ** i
    return decimal_num


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, f'base is out of range: {base}'
    # Handle unsigned numbers only for now
    assert number >= 0, f'number is negative: {number}'

    # binary (base 2)
    # 10 -> 2:
        # 10/2 = 5: 0
            # 5/2 = 2: 1
                # 2/2 = 1: 0
                    # 1/2 = 0: 1 - then read the remainders bottom up: 1010 = 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0
    # Encode number in any base (2 up to 36)
    result = ""
    while number > 0:
        remainder = number % base
        number -= remainder
        number = number // base
        if remainder > 9:
            remainder = string.ascii_lowercase[remainder-10]
        result = str(remainder) + result
    return result


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, f'base1 is out of range: {base1}'
    assert 2 <= base2 <= 36, f'base2 is out of range: {base2}'

    # start by using decode to decoded digits in base 10 form
    # use encode to turn base 10 digits into desired base form

   # Convert digits from any base to any base (2 up to 36)
    decoded_base10 = decode(digits, base1)
    result = encode(decoded_base10, base2)
    return result




def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print(f'{digits} in base {base1} is {result} in base {base2}')
    else:
        print(f'Usage: {sys.argv[0]} digits base1 base2')
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
