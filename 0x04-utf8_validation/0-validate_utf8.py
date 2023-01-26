#!/usr/bin/python3
"""
UTF-8 Validation code
"""

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
        if bytes(i) > bytes(255):
            return False
    return True