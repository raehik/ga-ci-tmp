#!/usr/bin/env python3

import math
from typing import Optional

def binary_search(l: list[int], x: int) -> Optional[int]:
    return binary_search_inner(l, x, 0, len(l)-1)

# TODO bad stuff going on with floor and idx_left lol. the indexing is coupled
def binary_search_inner(l: list[int], x: int, idx_left: int, idx_right: int) -> Optional[int]:
    if idx_left == idx_right:
        if x == l[idx_left]:
            return idx_left
        else:
            return None
    else:
        idx = math.floor((idx_left + idx_right) / 2)
        if x < l[idx]:
            return binary_search_inner(l, x, idx_left, idx-1)
        elif x > l[idx]:
            return binary_search_inner(l, x, idx+1, idx_right)
        else: # must be equal
            return idx

print(binary_search([0,1,2,3,4,5,6], 0))
