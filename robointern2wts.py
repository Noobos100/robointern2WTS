import os
import re
data = ""

def copyxml(template, config):

    #split RoboIntern config file into multiple task files
    with open(config, 'r') as f:
        splittext = f.read()

    found = re.findall(r'(<TaskConfig>.*?</TaskConfig>)', splittext, re.M | re.S)
    foundnames=[]
    for i in range(0, len(found)):
        foundnames.append("configsplitfiles\\"+gettaskname(found[i]).replace("/","&")+'.xml')
        
    #Create file for every task
    [open(foundnames[i], 'w').write(found[i]) for i in range(0, len(found))]

    #Create WTS file format for every split file
    [writeresult(foundnames[i], template) for i in range(0, len(found))]

#Creates WTS file with RoboIntern file

#Gets values of RoboIntern config file and stores them in an array
def writeresult(configfile, templatefile):
        with open(configfile, 'r', encoding='utf-8') as conf:
            confdata = conf.read()
            taskname = gettaskname(confdata)
            cmdpath = getcommandpath(confdata)
            taskexectime = gettaskexectime(confdata)
            conf.close()

    #Reads content of template and extracts it to data string variable
        with open(templatefile, 'r', encoding='utf-16') as temp:
            data = temp.read()
            temp.close()
            #Replaces content of extracted template data
            data = data.replace("D:\\talend\\val\DATAWAREHOUSE\DWAR_ALL_MINOR_CHANGE\DWAR_ALL_MINOR_CHANGE\DWAR_ALL_MINOR_CHANGE_run.bat", "D:"+cmdpath+".bat")
            data = data.replace("19:15:00", taskexectime)

    #Writes result to result.xml
        if os.path.exists("results\\"+taskname+".xml"):
            os.remove("results\\"+taskname+".xml")
            pass
        else:
            open("results\\"+taskname+".xml", 'x')

        with open("results\\"+taskname+".xml", 'w', encoding='utf16') as file2:
            file2.write(data)



#searches for taskexectime in template using beginnning and end delimiters (MIGHT NEED TO CHANGE THESE)
def gettaskexectime(data):
    task_match = re.search(r'([0-2][0-3]:[0-5][0-9]:[0-5][0-9])', data)
    if task_match:
        tasktime = task_match.group(1)
        return tasktime

#searches for taskname in template using beginnning and end delimiters (MIGHT NEED TO CHANGE THESE)
def gettaskname(data):
    task_match = re.search(r'<Name>(.*?)</Name>', data)
    if task_match:
        taskname = task_match.group(1)
        return taskname.replace("/","&")

#searches for command path in template using beginnning and end delimiters (MIGHT NEED TO CHANGE THESE)
def getcommandpath(data):
    task_match = re.search(r"D:(.*?).bat", data)
    if task_match:
        taskcmd = task_match.group(1)
        return taskcmd

copyxml("planifitemplate.xml", "robointernconfig.xml")