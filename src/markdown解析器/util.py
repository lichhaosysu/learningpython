'''
Created on 2013-4-24

@author: Stefan
'''
def lines(file):
    for line in file: yield line
    yield '\n'
    
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
