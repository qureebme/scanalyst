# It is assumed that this code will be run from a directory in which the user has RW access.
# The repository will be cloned to this directory. The program breaks if the cloned repo is empty,
# or dirty. For multiple runs, delete the /code directory created from the previous run.

# On successful execution, a 'code' directory is created in the current directory
# Each sub-directory in code contains the files in the repo for a particular commit,
# with the repo's directory structure preserved!
# Each sub-directory is named g12_<an integer>
# MetaData.csv is located in /g12_<an integer>

import os, git, pydriller, csv
import copyDir, shutil

currentDir = os.getcwd()

def checkRepo(url):

    gitHubRepo = url 
    gitDir = gitHubRepo.rsplit('/', 1)[1].rsplit('.')[0] # extract dir name from url, same as project name

    if not (os.path.exists(gitDir)):
        git.Git(currentDir).clone(gitHubRepo) # clone the repo
    else:
        # do some cleanup, just in case...
        cmd2 = 'git checkout master'
        cmd3 = 'git branch -D _PD'

        os.chdir(gitDir)
        os.system(cmd2)
        os.system(cmd3)
        os.chdir('../')

    repo_ = git.Repo(gitDir)
    assert repo_.__class__ is git.Repo
    assert not repo_.bare
    assert not repo_.is_dirty()  # check if repo is dirty

    if not (os.path.exists('./code')):
        os.makedirs('./code')

    repo = pydriller.GitRepository(gitDir) # cloned repo object

    i=0
    for commit in pydriller.RepositoryMining(gitDir, only_modifications_with_file_types=['.java']).traverse_commits():

        i+=1
        dirs_arg = 'g12_' + str(i)      # dir for this commit

        repo.checkout(commit.hash)      # check out this commit
        files = repo.files()            # files in this commit
        os.chdir('./code')
        dirr = '../' + gitDir
        shutil.copytree(dirr, dirs_arg, copy_function=copyDir.copy_dir)
        os.chdir('../') # go back up

        for file in files:
            meta = {} #metadata. this should come with each analyzed file!
            filename = file

            if (filename.endswith('.java')):

                meta['projectID']=commit.project_name
                meta['commitHash']= commit.hash
                meta['committerTimezone']=commit.committer_timezone
                meta['author']= commit.author.name
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
                w = csv.writer(open('./code/' + dirs_arg + '/'+"MetaData.csv", "w", encoding='utf-8'))
                for key, val in meta.items():
                    w.writerow([key, val])
                
                filePath = os.getcwd() + '/' + filename

                f = open(filePath, 'r')
                content = f.read() # content of the current file

                x = './code/' + dirs_arg + filename.replace(gitDir, '')

                currentCode = open( x, 'a+')
                currentCode.write(content)

                # release system resources
                f.close()
                currentCode.close()

#checkRepo("https://github.com/dizzam/java-project2017.git")
