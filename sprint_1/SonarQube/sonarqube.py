import os
import os.path as path
import platform
import time
import urllib.request as urllib # replace by urllib2 on Python2

# Useful variables -------------------------------------------------------------

# Installation directory of sonar-scanner
file = open("SonarQube/sonarscanner-folder", "r")
__scanner_folder = file.read().replace("\n", "")
file.close()

# Installation directory of sonarqube server
file = open("SonarQube/sonarserver-folder", "r")
__server_folder = file.read().replace("\n", "")
file.close()

# Directory of the sonarqube server binaries
__server_binaries_folder = path.join(__server_folder, "bin/")
if platform.system() == "Linux":
    __server_binaries_folder += "linux-x86-64/" # Linux
if platform.system() == "Darwin":
    __server_binaries_folder += "macosx-universal-64/" # Mac

# Server -----------------------------------------------------------------------

# Starts the server (BLOCKING)
# Will just do nothing if you call it with the server already started
# TODO make it asynchronous with callback
def start_server():
    # Starts the server
    cmd = path.join(__server_binaries_folder + "sonar.sh console")
    os.system(cmd + " &") # & makes the command execute on the background
    # Makes a basic configuration
    configure("~/", "DefaultProjectKey")
    __wait_for_server_startup()


# Stops the server asynchronously
# TODO optionnal callback
def stop_server():
    os.system(path.join(__server_binaries_folder + "sonar.sh") + " stop &")


# Returns true if the server is up and ready to scan
def __is_server_up():
    try:
        contents = urllib.urlopen("http://localhost:9000/api/system/status").read()
        return contents.find(b'"status":"UP"') != -1
    except:
        return False


# Waits until the server is ready to scan (tests every 2 seconds)
# BLOCKING
def __wait_for_server_startup():
    serverUp = False
    # Sends requests to the api until the response contains status:ON
    while(not __is_server_up()):
        time.sleep(2)


# Scanner ----------------------------------------------------------------------

# Sets the project folder and its name for the scanner
# TODO do a proper modification of the concerned field instead of this shit
# TODO make projectKey optionnal (to be able to change dir without changing key)
# TODO find a solution for the Java binaries
def configure(projectPath, projectKey):
    confPath = path.join(__scanner_folder, "conf/sonar-scanner.properties")
    file = open(confPath, "w+")
    content = "sonar.projectKey=" + projectKey + "\n" \
              "sonar.projectBaseDir=" + projectPath + "\n" \
              "sonar.java.binaries=../../SonarQube/tmp"
    file.write(content)
    file.close()


# Runs an analysis (Blocking)
# TODO make it asynchronous with callback
def run_analysis():
    cmd  = path.join(__scanner_folder, "bin/sonar-scanner")
    os.system(cmd)


# Returns the analysis results in the form of a json string
def get_analysis_results():
    return str(urllib.urlopen("http://localhost:9000/api/issues/search").read(), "utf-8")


