from pypandoc import convert


def read_md(value):
    return convert(value, 'rst')

with open('README.rst', 'w') as outputfile:
    outputfile.write(read_md('README.md'))
