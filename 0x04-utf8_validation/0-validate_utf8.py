#!/usr/bin/python3
"""
UTF-8 Validation code
"""


def get_unicode(in_data):
    """
    Gets the Unicode equivalent of input data
    """
    chunks = []
    bit = 0
    while (in_data > 0):
        bit = 0xff & in_data
        in_data = in_data >> 8
        chunks.append(bit)
    return chunks[::-1]


def check_header(data, header, lent):
    """
    assert header
    """
    if data & (0xff << (8 - lent)) == header:
        return True
    return False


def validUTF8(data):
    """
    Fuction to validate input data contains only UTF-8
    codes
    """

    if type(data) is not list or data is None:
        return False
    if len(data) == 0:
        return False
    for i in data:
        chunks = get_unicode(i)
        if len(chunks) > 4:
            return False
        if len(chunks) == 1:
            if not check_header(chunks[0], 0b0, 1):
                return False
        if len(chunks) == 2:
            if not (check_header(chunks[0], 0b110, 3) and
                    check_header(chunks[0], 0b10, 2)):
                return False
        if len(chunks) == 3:
            if not (check_header(chunks[0], 0b1110, 4) and
                    check_header(chunks[1], 0b10, 2) and
                    check_header(chunks[2], 0b10, 2)):
                return False
        if len(chunks) == 4:
            if not (check_header(chunks[0], 0b11110, 5) and
                    check_header(chunks[1], 0b10, 2) and
                    check_header(chunks[2], 0b10, 2) and
                    check_header(chunks[3], 0b10, 2)):
                return False

    return True
