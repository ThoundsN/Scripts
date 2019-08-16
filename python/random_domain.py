#!/usr/bin/python3

import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

with open("Generated_domain.txt", 'w', encoding='utf-8') as w :
    for i in range(122222):
        w.write(randomString(5)+'.dev.jupiterone.io')
        w.write('\n')

w.close()
