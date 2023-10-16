import os
import re

#Create resultfile if it doesn't exist
def copyxml(template, config, resultat):
    if os.path.exists(resultat):
        os.remove(resultat)
        pass
    else:
        open(resultat, 'x')

#Reads content of template and extracts it to data string variable
    with open(template, 'r', encoding='utf-16') as temp:
        data = temp.read()
        temp.close()

#Gets values of RoboIntern config file and stores them in an array
    with open(config, 'r', encoding='utf-8') as conf:
        confdata = conf.read()
        taskname = gettaskname(confdata)
        cmdpath = getcommandpath(confdata)
        temp.close()
        print(taskname)
        print(cmdpath)

#Replaces content of extracted template data
        data = data.replace("Opera scheduled Autoupdate 1684011439", taskname)
        data = data.replace("C:\\Users\\Charles\\AppData\\Local\\Programs\\Opera\\launcher.exe",cmdpath)

#Writes result to result.xml
    with open(resultat, 'w', encoding='utf16') as file2:
        file2.write(data)


def gettaskname(data):
    task_match = re.search(r'<Name>(.*?)</Name>', data)
    if task_match:
        taskname = task_match.group(1)
        return taskname

def getcommandpath(data):
    task_match = re.search(r'<string>([^ ])</string>', data)
    if task_match:
        task_value = task_match.group(1)
        return task_value

copyxml("template.xml", "config.xml", "resultat.xml")

