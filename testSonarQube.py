from SonarQube import sonarqube as sq

# Starts the server
sq.start_server() # Blocking

# Configures the sonar scanner to scan in the given folder
sq.configure("/media/kubby/Data/GitHub/SEM_Project/testSonarQube/src", "DefaultProjectKey")

# Runs the analysis
sq.run_analysis() # Blocking

# Fetches the analysis results
analysisResults = sq.get_analysis_results()
print("\n\nAnalysis results:\n" + analysisResults + "\n\n")

sq.stop_server() # Asynchronous

