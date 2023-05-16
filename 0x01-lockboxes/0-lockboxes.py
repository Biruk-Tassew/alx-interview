#!/usr/bin/python3

"""
Method to determine if all boxes can be opened
Using prototype: def can_unlock_all(boxes)
"""


def can_unlock_all(boxes):
    """
    Check if boxes can be unlocked
    """
    for target_key in range(1, len(boxes) - 1):
        for box_idx in range(len(boxes)):
            if target_key in boxes[box_idx] and target_key != box_idx:
                break
        if not target_key in boxes[box_idx] and target_key != box_idx:
            return target_key in boxes[box_idx] and target_key != box_idx
    return True
