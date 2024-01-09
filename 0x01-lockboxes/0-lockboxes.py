#!/usr/bin/python3
"""Lockboxes Module"""


def canUnlockAll(boxes):
    """canUnlockAll() method"""
    if not boxes or len(boxes) == 1:
        return True

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]

        for key in keys:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
