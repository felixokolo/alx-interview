#!/usr/bin/python3
""" Lockboxes """


def open_boxes(keys, boxes):
    """
    Open all boxes in in boxes using keys

    Parameters:
    keys (list): list of keys to open boxes
    boxes (list): list of list of keys

    Returns:
        Set of new keys
    """
    ret = []
    for box in boxes:
        if box['id'] in keys:
            box['state'] = 'opened'
            ret += box['keys']
    return set(ret)


def canUnlockAll(boxes: list) -> bool:
    """
    Checks if all boxes in an array can be opened

    Parameters:
        boxes (list): list of list of keys

        Returns:
            bool true if all boxes can be opened
            fales otherwise
    """

    if len(boxes) == 0:
        return True

    keys = []

    if type(boxes[0]) is list:
        boxes_dict = [{'id': x, 'keys': boxes[x],
                       'state': 'opened' if x == 0 else 'closed'}
                      for x in range(len(boxes))]
    else:
        boxes_dict = boxes
    opened = list(filter(lambda ele: ele['state'] == 'opened', boxes_dict))
    closed = list(filter(lambda ele: ele['state'] == 'closed', boxes_dict))

    for ele in opened:
        keys += ele['keys']

    if len(closed) > 0:
        new_keys = open_boxes(keys, closed)
        if len(new_keys) == 0:
            new_closed = list(filter(lambda ele: ele['state'] == 'closed',
                                     closed))
            if len(new_closed) > 0:
                return False
            else:
                return True
    else:
        return True
    return canUnlockAll(closed)
