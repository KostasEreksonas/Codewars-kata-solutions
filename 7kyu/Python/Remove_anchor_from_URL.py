#!/usr/bin/env python3

def remove_url_anchor(url):
    return url.split('#', 1)[0]

print(remove_url_anchor("www.codewars.com#about"))
print(remove_url_anchor("www.codewars.com/katas/?page=1#about"))
print(remove_url_anchor("www.codewars.com/katas/"))
