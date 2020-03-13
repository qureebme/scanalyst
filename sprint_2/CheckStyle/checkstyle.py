import os

def analyse_file(path):
    os.system("java -jar checkstyle-8.30-all.jar -c /sun_checks.xml " + path)
