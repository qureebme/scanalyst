import os, git, pydriller
currentDir = os.getcwd()

gitHubRepo = "https://github.com/qureebme/fullStackOpen3.git"
gitDir = gitHubRepo.rsplit('/', 1)[1].rsplit('.')[0] # extract dir name from url

assert os.path.exists(gitDir) is False # to ensure the dir doesnt already exist
git.Git(currentDir).clone(gitHubRepo) # clone the repo

repo_ = git.Repo(gitDir)
assert repo_.__class__ is git.Repo
assert not repo_.bare
assert not repo_.is_dirty()  # check if repo is dirty

repo = pydriller.GitRepository(gitDir) # cloned repo object

for commit in pydriller.RepositoryMining(gitDir).traverse_commits(): #only .java files later
    hashh = commit.hash
    mssg = commit.msg

    repo.checkout(hashh)
    files = repo.files()
    
    for file in files:
        f = open(file, 'r')
        content = f.read() # content of the current file

        #what shall we do with this content?
        #write it to a file?
        currentCode = open('code.txt', 'a+') # code.java in final stuff
        currentCode.write(content) # append mode: not so useful yet

        # release system resources
        f.close()
        currentCode.close()