import os
import xml.etree.ElementTree as xml

# Installation directory of sonar-scanner
file = open("CheckStyle/checkstyle-jar-location", "r")
__checkstyle_jar = file.read().replace("\n", "")
file.close()

__results_file = "CheckStyle/res";

# Runs the analysis on the given folder
# CheckStyle will then store the results as xml in outputPath
def __run_analysis(inputPath, outputPath):
    files = os.path.join(inputPath, "*.java") + " " + os.path.join(inputPath, "**/*.java")
    output = "-o " + outputPath + " -f xml"
    config = "-c /sun_checks.xml"
    os.system("java -jar " + __checkstyle_jar +" "+ config +" "+ files +" "+ output)

# Parses the xml to a dictionnary with the useful information
def __parse_results(xmlFile):
    res = []
    root = xml.parse(xmlFile).getroot()
    for f in root.findall("file"):
        for error in f.findall("error"):
            dic = {
                "rule":"",
                "severity": error.get("severity"),
                "status":"",
                "message": error.get("message"),
                "effort":"",
                "debt":"",
                "type":"",
                "creationDate":"",
                "startLine": error.get("line"),
                "endLine": error.get("line"),
                "resolution":"null"
            }
            res.append(dic)

    return res

# Analyses the given folder and returns the results as a dictionnary
def analyse(path):
    __run_analysis(path, __results_file)
    results = __parse_results(__results_file)
    os.remove(__results_file)
    return results
