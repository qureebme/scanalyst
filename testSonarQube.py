from SonarQube import sonarqube

# sonarqube.start_server() sonar-scanner works without the server, maybe its not needed
sonarqube.configure("/media/kubby/Data/GitHub/SEM_Project/testSonarQube/src")
sonarqube.run_analysis()

