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

for commit in pydriller.RepositoryMining(gitDir).traverse_commits():
    hashh = commit.hash
    mssg = commit.msg

    repo.checkout(hashh)
    files = repo.files()
    
    for file in files:
        f = open(file, 'r')
        f.close()