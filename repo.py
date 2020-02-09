# It is assumed that this code will be run from 
# a directory in which the user has RW access.
import os, git, pydriller
currentDir = os.getcwd()

gitHubRepo = "https://github.com/qureebme/fullStackOpen3.git"
gitDir = gitHubRepo.rsplit('/', 1)[1].rsplit('.')[0] # extract dir name from url, same as project name

assert os.path.exists(gitDir) is False # to ensure the dir doesnt already exist
git.Git(currentDir).clone(gitHubRepo) # clone the repo

repo_ = git.Repo(gitDir)
assert repo_.__class__ is git.Repo
assert not repo_.bare
assert not repo_.is_dirty()  # check if repo is dirty

repo = pydriller.GitRepository(gitDir) # cloned repo object

for commit in pydriller.RepositoryMining(gitDir, only_modifications_with_file_types=['.js']).traverse_commits(): #only .java files later
    hashh = commit.hash
    mssg = commit.msg
    dirs_arg = './code/' + 'g12_' + hashh[0:5]
    os.makedirs(dirs_arg)   # each commit gets a directory

    repo.checkout(hashh)    # check out this commit
    files = repo.files()

    for file in files:
        filename = file # string# component in final stuff

        f = open(file, 'r')
        content = f.read() # content of the current file

        #what shall we do with this content?
        #write it to a file?

        myfilename = dirs_arg + '/' + filename.rpartition('\\')[2]
        currentCode = open(myfilename, 'a+') # code.java in final stuff
        currentCode.write(content)

        # release system resources
        f.close()
        currentCode.close()
    