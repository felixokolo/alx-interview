#!/usr/bin/python3
"""
UTF-8 Validation code
"""


def bits_length(in_data):
    """
    Gets length of bits of data
    """
    bit = 0
    while (in_data > 0):
        in_data = in_data >> 1
        bit += 1
    return bit


def check_header(data):
    """
    assert header
    """
    pos = 0
    while pos < len(data):
        lent = 1
        if ((data[pos] >> 3) ^ 0x1e) == 0:
            lent = 4
        if ((data[pos] >> 4) ^ 0xe) == 0:
            lent = 3
        if ((data[pos] >> 5) ^ 0x6) == 0:
            lent = 2
        if pos + lent < len(data):
            yield data[pos:pos + lent]
        else:
            yield data[pos:]
        pos += lent


def validUTF8(data):
    """
    Fuction to validate input data contains only UTF-8
    codes
    """

    total_len = 0
    if type(data) is not list or data is None:
        return True
    if len(data) == 0:
        return True
    for i in data:
        if bits_length(i) > 8:
            return False
    for i in check_header(data):
        total_len += len(i)
        if len(i) > 1:
            for j in range(1, len(i)):
                if ((i[j] >> 6) ^ 0x2) != 0:
                    return False
        else:
            if i[0] > 127:
                return False
    if total_len != len(data):
        return False
    return True
