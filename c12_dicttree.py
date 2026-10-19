#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

# A simpler example: the pages of a web site (leaves have no "children" key)
site = {"title": "Home", "children": [
    {"title": "News", "children": [
        {"title": "2026"},
        {"title": "Archive"},
    ]},
    {"title": "About", "content": "Best news website"},
]}


def count_pages(node: dict) -> int:
    count = 1  # the page itself
    for child in node.get("children", []):
        count += count_pages(child)
    return count


print(count_pages(site))                         # 5
print(count_pages(site["children"][0]))          # 3: News, 2026, Archive
