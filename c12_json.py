#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

# A tree of nested dictionaries (JSON-like), using the schema.org vocabulary
org = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Acme",
    "address": {
        "@type": "PostalAddress",
        "addressLocality": "Modena",
        "addressCountry": "IT",
    },
    "founder": {"@type": "Person", "name": "Ann Lee"},
    "subOrganization": [
        {"@type": "Organization", "name": "Research",
         "subOrganization": [
             {"@type": "Organization", "name": "AI Lab"},
         ]},
        {"@type": "Organization", "name": "Sales"},
    ],
}

# Access by key (dict) and by index (list)
print(org["address"]["addressLocality"])         # Modena
print(org["subOrganization"][0]["name"])         # Research


def count_orgs(node: dict) -> int:
    count = 1  # the organization itself
    # a leaf has no "subOrganization" key: the loop does nothing (base case)
    for sub in node.get("subOrganization", []):
        count += count_orgs(sub)
    return count


print(count_orgs(org))                           # 4: Acme, Research, AI Lab, Sales
print(count_orgs(org["subOrganization"][0]))     # 2: Research, AI Lab
print(count_orgs(org["subOrganization"][1]))     # 1: Sales

# From data to JSON text, and back
text = json.dumps(org, indent=2)
print(text)
copy = json.loads(text)
print(copy == org)                               # True
print(count_orgs(copy))                          # 4
