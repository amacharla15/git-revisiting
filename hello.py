
#Initialization
"""
git init -- Initializing the git repo

ls -la -- .git

cd ..

"""
# Commit Phase
"""
git status -- ran before commiting or running git add . , so I got untracked 

to track:
git add . --success
git status - shows to be commited

commit:

git commit -m

ran git log to check commit message, author details 

"""

#Github repo creating and connection 
"""
create a github repo: git revisit 

ran the command: git remote add origin https://github.com/amacharla15/git-revisiting.git
 to connect repo 
 to confirm, : git remote -v

 could see: git remote -v

  just added the above comments and tried pushing the file using the commands:
  for the first push : git push -u origin main  
  git add .
  git status
  git commit -m "connected to repo successfully"
   git push


"""
# checkout commands 
#branch a reference itself(head)
"""
git checkout main

hello akshith 

created a new branch: git branch feature1 
switched to the new branch : git checkout feature1 
--added a line in that new branch "This is extra line" and committed and tried checking main all these changes are reverted back

"""

#merge commands

"""
tried merging bot the main and feature branch and recived a merge conflict
accepted current changes --git merge feature1
as I was already in main branch 
"""

#Rebase command

"""
since merge gives some issues in real life scenarios working in teams etc, we try rebase


"""