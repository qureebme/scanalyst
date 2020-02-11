import sys, csv, json, os

if len(sys.argv)<2:
    raise ValueError ("The program expects a git URL as an argument")

import repo
repo.checkRepo(sys.argv[1])


from SonarQube import sonarqube as sq
# Starts the server
sq.start_server() # Blocking

output_data=[]
for root, dirs,_ in os.walk("./code/", topdown=False):
    for name in dirs:
        with open(os.path.join(root, name)+'/MetaData.csv', mode='r') as infile:
            reader = csv.reader(infile)
            metaData = {rows[0]:rows[1] for rows in reader}

        # Configures the sonar scanner to scan in the given folder
        sq.configure(os.path.join(root, name), "DefaultProjectKey")

        # Runs the analysis
        sq.run_analysis() # Blocking

        # Fetches the analysis results
        content = sq.get_analysis_results()
        json_data=json.loads(content)
        for i in json_data["issues"]:
            dic={"rule":"","severity":"","status":"","message":"","effort":"",
                "debt":"","type":"","creationDate":"","startLine":"","endLine":"",
                 "projectName":metaData["projectID"],"creationCommitHash":metaData["commitHash"],
                 "author":metaData["author"]}
            for j in ["rule","severity","project","status","message","effort",
                      "debt","type","creationDate"]:
                try:
                    dic[j]=i[j]
                except Exception:
                    continue
            try:
                dic["startLine"]=i["textRange"]["startLine"]
                dic["endLine"]=i["textRange"]["endLine"]
            except Exception:
                pass
            output_data.append(dic)

import ParsingToCsv as ptc
ptc.make_csv(output_data)
           
# sq.stop_server() # Asynchronous
