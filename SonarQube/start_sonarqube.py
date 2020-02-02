import os
import platform

cmd = ""
if platform.system() == "Linux":
	cmd = "sonarqube-*/bin/linux-x86-64/sonar.sh console" # Linux
if platform.system() == "Windows":
	cmd = "cd sonarqube-*\\bin\windows-x86-64\ && call StartSonar.bat" # Windows
if platform.system() == "Darwin":
	cmd = "sonarqube-*/bin/macosx-universal-64/sonar.sh console" # Mac

os.system(cmd)