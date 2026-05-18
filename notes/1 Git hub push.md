PERSONAL GIT WORKFLOW (ONLY TERMINAL)
🚀 STEP 1: project folder me jao
cd /path/to/your/project


🔍 STEP 2: check repo status
git status


🔍 STEP 3: check correct account (IMPORTANT)
git config user.email

👉 should be:
adeepsingh2053@gmail.com


🔍 STEP 4: check remote (VERY IMPORTANT)
git remote -v

👉 should be:
git@github-personal:username/repo.git
➕ STEP 5: add changes
git add .


✍️ STEP 6: commit
git commit -m "your message here"


🚀 STEP 7: push
git push
⚠️ 🔐 FINAL SAFETY CHECK (ALWAYS DO BEFORE PUSH)
Run this ONLY:
git config user.email

👉 if correct → push safe
👉 if wrong → STOP