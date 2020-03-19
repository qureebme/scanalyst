import os
import glob
import xml.etree.ElementTree as xml

# Installation directory of checkstyle jar
file = open("CheckStyle/checkstyle-jar-location", "r")
__checkstyle_jar = file.read().replace("\n", "")
file.close()

__results_file = "/tmp/checkstyleoutput.xml"

# Runs the analysis on the given folder
# CheckStyle will then store the results as xml in outputPath
def __run_analysis(inputPath, outputPath):
    filesRegex = os.path.join(inputPath, "**/*.java")
    filesList = glob.glob(filesRegex, recursive=True)
    output = "-o " + outputPath + " -f xml"
    config = "-c /sun_checks.xml"
    cmd = "java -jar " + __checkstyle_jar +" "+ config +" "+ output
    for f in filesList:
        cmd += " " + f
    if(len(filesList) > 0):
        os.system(cmd)

# Parses the xml to a dictionnary with the useful information
def __parse_results(xmlFile,pickUpMetaDataFun,path,output_data,commit_data):
    # If the results file doesn't exist
    if(not os.path.isfile(xmlFile)):
        return
    # Parses the results file
    root = xml.parse(xmlFile).getroot()
    for f in root.findall("file"):
        for error in f.findall("error"):
            dic = {
                "severity": error.get("severity"),
                "status":"",
                "message": error.get("message"),
                "effort":"",
                "debt":"",
                "type":"",
                "creationDate":"",
                "startLine": error.get("line"),
                "endLine": error.get("line"),
                "resolution":"null",
                "component": f.get("name"),
                "squid": ""
            }
            pickUpMetaDataFun(dic,path,commit_data)
            output_data.append(dic)

# Analyses the given folder and returns the results as a dictionnary
def analyse(path,pickUpmetaDataFun,output_data,commit_data):
    __run_analysis(path, __results_file)
    __parse_results(__results_file,pickUpmetaDataFun,path,output_data,commit_data)
    if(os.path.isfile(__results_file)): os.remove(__results_file)
