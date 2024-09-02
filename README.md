# SEM Project

A static code analyser that can use SonarQube, CheckStyle or PMD to find errors in any commit of a Java project repository and put them in csv files

Authors:

- Qureeb Hameed
- Gabriel Jorge
- Henrik Sillanpää
- Alexis Vanhalle	

## Installation

First:
    In /SonarQube/sonarscanner-folder and /SonarQube/sonarserver-folder, replace '/home/qureeb/Documents/codebook/snapcraft/PySnap' in the paths to the corresponding path on your PC
    
Then:
    Run this in a terminal (in the same directory as this file)
    ./sprint_2/install.sh

## Usage

Run this in a terminal (in the same directory as this file)
python3 main.py <url-to-your-repo> <code-analysis-tool>

code-analysis-tool is one of pmd, sonar, or checkstyle


