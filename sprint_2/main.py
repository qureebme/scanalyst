import sys, csv, json, os, shutil

def pickUpMetaData(dic,path,commit_data):    
    with open(path+'/MetaData.csv', mode='r') as infile:
        reader = csv.reader(infile)
        metaData = {rows[0]:rows[1] for rows in reader}
        commit_data.append(metaData)               
        dic["projectName"]=metaData["projectID"]
        dic["creationCommitHash"]=metaData["commitHash"]
        dic["author"]=metaData["author"]
    return dic,commit_data

def LaunchPMD(path,output_data,commit_data):
    from PMD import pmd2 as pmd
    pmd.usePMD(path,pickUpMetaData,output_data,commit_data)
    
    
def LaunchCS(path,output_data,commit_data):
    from CheckStyle import checkstyle as ch
    ch.analyse(path,pickUpMetaData,output_data,commit_data)
    


def LaunchSQ(path,output_data,commit_data):
    from SonarQube import sonarqube as sq
    # Starts the server
    sq.start_server() # Blocking
    # Configures the sonar scanner to scan in the given folder
    sq.configure(path, "DefaultProjectKey")

    # Runs the analysis
    sq.run_analysis() # Blocking

    # Fetches the analysis results
    content = sq.get_analysis_results()
    json_data=json.loads(content)
    dic={}
    for i in json_data["issues"]:

        dic={"rule":"","severity":"","status":"","message":"","effort":"",
            "debt":"","type":"","creationDate":"","startLine":"","endLine":"",
            "projectName":"",
            "creationCommitHash":"",
             "author":"","resolution":"null"}
            
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
        
        pickUpmetaData(dic,path,commit_data)
        output_data.append(dic)
        

Launch={
    "sonar":LaunchSQ,
    "checksyle":LaunchCS,
    "pmd":LaunchPMD
    }
sys.argv.append("main.py https://github.com/zeebe-io/zeebe-test-template-java")
sys.argv.append("checksyle")


if len(sys.argv)<3:
    raise ValueError ("The program expects a git URL followed by the scanner wanted as arguments")

if sys.argv[2] not in Launch.keys():
    raise ValueError("scanner name incorrect: "+ sys.argv[2],"Names are:" + str([i for i in Launch.keys()]))

scanner=sys.argv[2]
import repo
repo.checkRepo(sys.argv[1])

output_data=[]
commit_data=[]

with os.scandir("./code/") as entries:
    
    for entry in entries:
            Launch[scanner]("./code/"+entry.name,output_data,commit_data)
            
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
