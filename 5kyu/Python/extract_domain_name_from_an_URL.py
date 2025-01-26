#!/usr/bin/env python3

import re

def domain_name(url):
    result = re.search("(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.", url).group('name')
    return result

print(f"{domain_name("http://google.com")}")
print(f"{domain_name("http://google.co.jp")}")
print(f"{domain_name("www.xakep.ru")}")
print(f"{domain_name("https://youtube.com")}")
