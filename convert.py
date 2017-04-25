import pypandoc

output = pypandoc.convert_file('README.md', 'rst', outputfile="README.rst")
assert output == ""