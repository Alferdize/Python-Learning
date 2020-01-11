"""
most_common.py
"""

import collections

C = collections.Counter('helloworld')


print(C.most_common(3))
