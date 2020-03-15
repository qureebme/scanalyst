# The function takes a directory (e.g. /g12_1) as an argument.
# Its output is a list of dictionaries about the PMD code analysis
# of the java files in its 'main' directory (e.g. g12_1/main)

# The commented lines of code are for possible modifications,
# if needed later

import os, subprocess

def usePMD(code_dir):

    if not os.path.isdir(code_dir):
        raise Exception(code_dir + ' is not a directory')
    
    os.chdir(code_dir)

    #for folder in code_dir, run analysis
    #for dir in os.listdir('./'): # comment

        #os.chdir(dir)   # comment

    #indent_start
    cmd1 = 'pmd -d ' + os.getcwd() + '/src/main/ -R rulesets/java/quickstart.xml -f csv -no-cache'    #default rulesets
    res = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE).communicate()[0]

    res2 = res.decode('utf-8').split('\n') # \r\n on Windows

    fields = res2[0].split(',')
    values = res2[1].split(',')

    dict_res = dict(zip(fields, values))
    dict_res.pop('"Problem"')

    os.chdir('../')
    #indent_end

        #break

    #os.chdir('../') # comment
    dictList = list()
    
    for x in dict_res:
        val = dict_res.get(x)
        dictList.append({x:val})

    return dictList

#usePMD('./code')
print(usePMD('./java-project2017'))