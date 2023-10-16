import os
import re

def copyxml(template,resultat):
    if os.path.exists(resultat):
        os.remove(resultat)
        pass
    else:
        open(resultat, 'x')

    with open(template, 'r', encoding='utf-16') as file1:
        data = file1.read()

        data = data.replace(getURI(data), "test")
    with open(resultat, 'w', encoding='utf16') as file2:
        file2.write(data)

def getURI(data):
    uri_match = re.search(r'<URI>(.*?)</URI>', data)
    if uri_match:
        uri_value = uri_match.group(1)
        return uri_value

copyxml("template.xml", "resultat.xml")

