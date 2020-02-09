import os
import platform

def start_server():

    # Starts the server
    path = __file__[:__file__.rfind("/")+1]
    cmd = path + "sonarqube-*/bin/"
    if platform.system() == "Linux":
        cmd += "linux-x86-64/sonar.sh console" # Linux
    if platform.system() == "Darwin":
        cmd += "macosx-universal-64/sonar.sh console" # Mac
    os.system(cmd + " &") # & makes the command execute on the background
    # Makes a basic configuration
    configure("~/")


def configure(projectPath, projectKey="DefaultProjectKey"):
    # TODO do a proper modification of the concerned field instead of this shit
    # TODO do a pattern matching to find the file (in case the version changes) 
    path = __file__[:__file__.rfind("/")+1] + "" \
           "sonar-scanner-4.2.0.1873-linux/conf/sonar-scanner.properties"
    file = open(path, "w+")
    content = "sonar.projectKey=" + projectKey + "\n" \
              "sonar.projectBaseDir=" + projectPath + "\n"
    file.write(content)
    file.close()


def run_analysis():
    cmd  = __file__[:__file__.rfind("/")+1] + "" \
           "sonar-scanner-4.2.0.1873-linux/bin/sonar-scanner"
    os.system(cmd) 
