# The main function (usePMD) takes a directory (e.g. /g12_1) as an argument.
# Its output is a list of dictionaries about the PMD code analysis
# of the java files in its 'main' directory (e.g. g12_1/main).
# Each dictionary contains details about one code issue.

import os, subprocess
'''
# Reads the installation directory of pmd
file = open("PMD/pmd-bin-location", "r")
__pmdBinDir = file.read().replace("\n", "")
file.close()
'''
def usePMD(code_dir,pickUpMetaDataFun,output_data,commit_data):

    dir = code_dir
    if not os.path.isdir(dir):
        raise Exception(dir + ' is not a directory')

    #os.chdir(dir)

    #cmd1 = os.path.join(__pmdBinDir, "run.sh ") + 'pmd -d ' + os.getcwd() + '/src/main/ -R rulesets/java/quickstart.xml -f csv -no-cache'    #default rulesets
    cmd1 = 'pmd -d ' + dir + ' -R rulesets/java/quickstart.xml -f csv -no-cache'    #default rulesets

    output = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    res = output[0]
    err = output[1]
    #print(code_dir)
    if (err):
        print('PMD: something went wrong: ', err)
        return

    res2 = res.decode('utf-8').split('\n') # all code issues
    res2.pop(0)

    fields = ['component', 'severity', 'startLine', 'resolution', 'type','rule'] # best fit
    values = processIssues(res2)

    dictList = list()

    for item in values:
        fullDict = dict()

        for index in range(0,6):
            fullDict[fields[index]] = item[index]
        fullDict['endLine'] = fullDict.get('startLine')
        fullDict['status'] = ""
        fullDict['message'] = ""
        fullDict['effort'] = ""
        fullDict['debt'] = ""
        fullDict['creationDate'] = ""
        fullDict['squid'] = ""
        
        pickUpMetaDataFun(fullDict,code_dir,commit_data)
        
        output_data.append(fullDict)

    #os.chdir('../')
    return dictList

def processIssues(issues):
    cleanedUp = []
    for n in range(0, len(issues)-1):
        thisIssue = issues[n].split(',') # a single issue

        #remove unneeded items
        thisIssue.pop(0)
        thisIssue.pop(0)

        value = cleanUpEntry(thisIssue)
        cleanedUp.append(value)
    return cleanedUp # list of lists

def cleanUpEntry(entry):
    if (len(entry) == 7):
        merge = entry[3] + ', ' + entry[4]
        del entry[3:5]
        entry.insert(3, merge)
        return entry
    else:
        return entry

#usePMD('/code')
#print(usePMD('/java-project2017'))
