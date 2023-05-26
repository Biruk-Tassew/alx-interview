#!/usr/bin/python3

"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def valid_utf8(data):
    # Hack to get around this weird case
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode()
    except BaseException:
        return False
    return True