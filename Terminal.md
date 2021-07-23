# Terminal

`clear` empty the terminal screen

`ls` list files and directories
 
`ls -la` list all including hidden content

## .git

`git clone` getting the repositories contents on github

`git status` shows files that were updated, created or deleted

`git add FILENAME` adds file to git

`git add .` adds all new content to git

`git commit -m ”TITLE” -m “DESCRIPTION”` 

`git init` ???

`git remote add origin SSH-KEY` add a reference to the remote repository on github

`git remote -v` shows any remote repositories connected to this repo

`git push -u origin master` set upstream when first initiating a new repository, after that `git push` suffices

git push origin master push to origin = git repo master = master branch

### Branching
`git branch` shows all branches

`git checkout -b feat` checkout switches to another branch, `-b` tells it to create a new branch, 
*feat* is the name of the new branch

`git merge` merge branches locally

`git diff BRANCHNAME` see difference between current branch and BRANCH