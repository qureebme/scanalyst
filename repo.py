import os, git
currentDir = os.getcwd()

gitHubRepo = "https://github.com/qureebme/fullStackOpen3.git"
gitDir = gitHubRepo.rsplit('/', 1)[1].rsplit('.')[0] # extract dir name from url
#print(gitDir) # name of the local git dir

assert os.path.exists(gitDir) is False # to ensure the dir doesnt already exist

git.Git(currentDir).clone(gitHubRepo) # clone the repo

repo = git.Repo(gitDir)
assert repo.__class__ is git.Repo
assert not repo.bare
assert not repo.is_dirty()  # check if repo is dirty