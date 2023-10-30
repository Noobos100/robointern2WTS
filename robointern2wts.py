import os
import re
import shutil
import msvcrt as m
    

#Clean folders before launching conversion
for filename in os.listdir("configsplitfiles"):
    file_path = os.path.join("configsplitfiles", filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

for filename in os.listdir("results"):
    file_path = os.path.join("results", filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


def robo2wts(template, config):
    
    #split RoboIntern config file into multiple task files
    with open(config, 'r') as f:
        splittext = f.read()

    found = re.findall(r'(<TaskConfig>.*?</TaskConfig>)', splittext, re.M | re.S)
    foundnames=[]
    for i in range(0, len(found)):
        foundnames.append("configsplitfiles\\"+gettaskname(found[i]).replace("/","&")+'.xml')

    #Write every split file to configsplitfile folder

    for i in range(0, len(found)):
        open(foundnames[i], 'x').write(found[i])

    #Count files in configsplitfiles
    countsplit = 0
    for path in os.listdir("configsplitfiles"):
        if os.path.isfile(os.path.join("configsplitfiles", path)):
            countsplit += 1
    print('Tasks found in RoboInternConfig File:', countsplit)

    #Create WTS file format for every split file
    for i in range(0, len(found)):
        writeresult(foundnames[i], template)

    #Count files in results 
    countconv = 0
    for path in os.listdir("results"):
        if os.path.isfile(os.path.join("configsplitfiles", path)):
            countconv += 1
    print('Tasks converted:', countconv)

    #Checks if all files have been converted
    if (countsplit==countconv):
        print("All files have been converted.")
        m.getch()
    #else:
        #catch errors


#Functions that create the WTS file with a RoboIntern file

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

robo2wts("planifitemplate.xml", "robointernconfig.xml")
