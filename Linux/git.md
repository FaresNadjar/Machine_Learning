# Git
## Main Git Commands :

- git clone url_of_your_remote_repository   # Clone a repository from a remote repository  
- git add file1 file2    # will add those two files to the index if they were modified  
- git commit -m "Meaningful commit message"   # will commit those two files (locally)  
- git add .   # will add all of the modified files to the index at once  
- git commit -m "Other meaningful commit message"   # will commit all of those files together  
- git push origin master   # send all commit to the remote server

## Same thing on a branch instead of master : 

- git branch my_feature   # Creating the branch  
- git checkout my_feature   # Changing the codebase so that we're on that branch now  
- git checkout -b my_feature   # This does the two previous operations in one ;)  
- git add file1 file2  
- git commit -m "Meaningful commit message"   # We didn't just commit this on the master branch like last time, but on the my_feature one  
- git add .  
- git commit -m "Other meaningful commit message"  
- git push origin my_feature   # Notice: we're not pushing master anymore, you just create a new remote branch

## To Work on that branch :

- git checkout my_feature   # Just making sure you're currently on the right branch!  
- git pull origin my_feature   # Pulling what your coworkers have done so far. 

## Merge a branch to master when we're done modifying : 

- git checkout master  
- git merge my_feature

## Turn a folder into a git repo : 

- git init   # You're done!  
- git remote add origin url_of_your_git_server   # So that you can push your code somewhere. 


