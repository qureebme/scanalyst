# The function takes a directory (e.g. /g12_1) as an argument.
# Its output is a list of dictionaries about the PMD code analysis
# of the java files in its 'main' directory (e.g. g12_1/main)

# The commented lines of code are for possible modifications,
# if needed later

import os, subprocess

# Reads the installation directory of pmd
file = open("PMD/pmd-bin-location", "r")
__pmdBinDir = file.read().replace("\n", "")
file.close()

def usePMD(code_dir,pickUpMetaDataFun,output_data,commit_data):

    if not os.path.isdir(code_dir):
        raise Exception(code_dir + ' is not a directory')

    os.chdir(code_dir)

    #for folder in code_dir, run analysis
    #for dir in os.listdir('./'): # comment

        #os.chdir(dir)   # comment

    #indent_start
    cmd1 = os.path.join(__pmdBinDir, "run.sh ") + 'pmd -d ' + os.getcwd() + '/src/main/ -R rulesets/java/quickstart.xml -f csv -no-cache'    #default rulesets
    res = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE).communicate()[0]

    res2 = res.decode('utf-8').split('\n') # \r\n on Windows

    #fields = res2[0].split(',')
    fields = ['component', 'severity', 'startLine', 'message', 'resolution']

    values = res2[1].split(',') # a list
    values.pop(0)
    values.pop(0)
    values.pop(5)
    
    dict_res = dict(zip(fields, values))
    
    os.chdir('../')
    #indent_end

        #break

    #os.chdir('../') # comment

    dictList = list()

    for x in dict_res:
        val = dict_res.get(x)
        dictList.append({x:val})

    #dictList.append({'rule':'', 'status':'', 'effort':'', 'debt':'', 'type':'', 'creationDate':'', 'endLine':'', 'squid':''})
    return dictList

#usePMD('./code')
#print(usePMD('./java-project2017'))
