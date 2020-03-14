import os

# Installation directory of sonar-scanner
file = open("CheckStyle/checkstyle-jar-location", "r")
__checkstyle_jar = file.read().replace("\n", "")
file.close()

# Analyses the given file
def analyse(inputPath, outputPath):
    files = os.path.join(inputPath, "*.java") + " " + os.path.join(inputPath, "**/*.java")
    output = "-o " + outputPath
    config = "-c /sun_checks.xml"
    os.system("java -jar " + __checkstyle_jar +" "+ config +" "+ files +" "+ output)
