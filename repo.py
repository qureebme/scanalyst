# It is assumed that this code will be run from a directory in which the user has RW access.
# The repository will be cloned to this directory. The program breaks if the repo already
# exists in this directory, or if the cloned repo is empty
# For multiple runs, delete the files created from the previous run.

# On successful execution, a 'code' directory is created in the current directory
# Each sub-directory in code contains the files in the repo for a particular commit
# Each sub-directory is named g12_<first five chars of the commit hash>
import os, git, pydriller, csv
currentDir = os.getcwd()

def checkRepo(url):

    gitHubRepo = url 
    gitDir = gitHubRepo.rsplit('/', 1)[1].rsplit('.')[0] # extract dir name from url, same as project name

    assert os.path.exists(gitDir) is False # to ensure the dir doesnt already exist
    git.Git(currentDir).clone(gitHubRepo) # clone the repo

    repo_ = git.Repo(gitDir)
    assert repo_.__class__ is git.Repo
    assert not repo_.bare
    assert not repo_.is_dirty()  # check if repo is dirty

    repo = pydriller.GitRepository(gitDir) # cloned repo object

    i=0

    for commit in pydriller.RepositoryMining(gitDir, only_modifications_with_file_types=['.java']).traverse_commits():

        i+=1
        
        dirs_arg = './code/' + 'g12_' + str(i)
        os.makedirs(dirs_arg)   # each commit gets a subdirectory in ./code

        repo.checkout(commit.hash)    # check out this commit
        files = repo.files()

        for file in files:
            meta = {} #metadata. this should come with each analyzed file!
            filename = file

            meta['projectID']=commit.project_name
            meta['commitHash']= commit.hash
            meta['component']= filename
            meta['author']= commit.author.name#[0]
            meta['commitMessage']= commit.msg
            meta['authorDate']= commit.author_date
            meta['authorTimezone']= commit.author_timezone
            meta['branches']= commit.branches
            meta['inMainBranch']= commit.in_main_branch
            meta['committer']= commit.committer
            meta['commiterDate']= commit.committer_date
            meta['parents']= commit.parents
            meta['merge']= commit.merge

            #writing data in csv
            w = csv.writer(open(dirs_arg + '/'+"MetaData.csv", "w"))
            for key, val in meta.items():
                w.writerow([key, val])
    
            f = open(file, 'r')
            content = f.read() # content of the current file

            #what shall we do with this content?
            #write it to a file?

            myfilename = dirs_arg + '/' + filename.rpartition('\\')[2]
            currentCode = open(myfilename, 'a+')
            currentCode.write(content)

            # release system resources
            f.close()
            currentCode.close()
checkRepo("https://github.com/dizzam/java-project2017.git")
