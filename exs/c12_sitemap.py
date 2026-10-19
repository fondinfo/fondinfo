#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

site = {"title": "Home", "children": [
    {"title": "News", "children": [
        {"title": "2026"},
        {"title": "Archive"},
    ]},
    {"title": "About", "content": "Best news website"},
]}


def show(node: dict, indent: int):
    print("    " * indent + node["title"])
    for child in node.get("children", []):
        show(child, indent + 1)


def find_page(node: dict, title: str) -> dict | None:
    if node["title"] == title:
        return node
    for child in node.get("children", []):
        found = find_page(child, title)
        if found is not None:  # compare explicitly: None means "not found"
            return found
    return None


def count_pages(node: dict) -> int:
    count = 1  # the page itself
    for child in node.get("children", []):
        count += count_pages(child)
    return count


show(site, 0)

for title in ["News", "About", "Zoe"]:
    page = find_page(site, title)
    if page is None:
        print(title, "not found")
    else:
        print(title, count_pages(page))
