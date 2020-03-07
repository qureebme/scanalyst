import sys, csv, json, os, shutil

if len(sys.argv)<2:
    raise ValueError ("The program expects a git URL as an argument")

import repo
repo.checkRepo(sys.argv[1])


from SonarQube import sonarqube as sq
# Starts the server
sq.start_server() # Blocking

output_data=[]
commit_data=[]
with os.scandir("./code/") as entries:
    for entry in entries:
        with open("./code/"+entry.name+'/MetaData.csv', mode='r') as infile:
            reader = csv.reader(infile)
            metaData = {rows[0]:rows[1] for rows in reader}
            commit_data.append(metaData)

        # Configures the sonar scanner to scan in the given folder
        sq.configure("./code/"+entry.name, "DefaultProjectKey")

        # Runs the analysis
        sq.run_analysis() # Blocking

        # Fetches the analysis results
        content = sq.get_analysis_results()
        json_data=json.loads(content)
        for i in json_data["issues"]:
        
            dic={"rule":"","severity":"","status":"","message":"","effort":"",
                "debt":"","type":"","creationDate":"","startLine":"","endLine":"",
                "projectName":metaData["projectID"],
                "creationCommitHash":metaData["commitHash"],
                 "author":metaData["author"],"resolution":"null"}
                
            for j in ["rule","severity","status","message","effort",
                      "debt","type","creationDate","component","resolution"]:
                try:
                    dic[j]=i[j]
                except Exception:
                    continue
            dic["squid"]=dic.pop("rule")
            dic["component"]=dic["component"][18:]
            try:
                dic["startLine"]=i["textRange"]["startLine"]
                dic["endLine"]=i["textRange"]["endLine"]
            except Exception:
                pass
            output_data.append(dic)

import ParsingToCsv as ptc

fieldnames=["projectName","creationDate",
"creationCommitHash","type","squid","component",
"severity","startLine","endLine","resolution",
"status","message","effort","debt","author"]
ptc.make_csv(output_data,"AnalysisResults",fieldnames)

fieldnames=["projectID","commitHash","commitMessage",
"author","authorDate","authorTimezone","committer",
"committerDate","committerTimezone","branches",
"inMainBranch","merge","parents"]

ptc.make_csv(commit_data,"CommitData",fieldnames)


shutil.rmtree("./code", ignore_errors=True)

# sq.stop_server() # Asynchronous
