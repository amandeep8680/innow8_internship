✅ STEP 1 — Project Setup
Create project
Create accounts app
Create posts app
Install DRF
✅ STEP 2 — Models

Create models in this order:

Profile (accounts)
Post
Like
Comment

👉 Then:

makemigrations
migrate


1. USER SYSTEM (accounts app)
🔹 Use built-in User (don’t create your own)

Django already gives:

username
email
password
🔹 Create Profile model
✅ Fields:
user → OneToOne(User)
dob → DateField
profile_pic → ImageField
bio → TextField
🔗 Connection:

👉 One user → one profile

User 1 ─── 1 Profile
🧩 2. POST MODEL (posts app)
✅ Fields:
user → ForeignKey(User)
image → ImageField
caption → TextField
created_at → DateTimeField
🔗 Connection:

👉 One user → many posts

User 1 ─── ∞ Posts
🧩 3. LIKE MODEL (VERY IMPORTANT)
✅ Fields:
user → ForeignKey(User)
post → ForeignKey(Post)
🔗 Connection:

👉 Many users can like many posts

User ∞ ─── ∞ Post
        (through Like)
⚠️ Why NOT store count?

Because:

Same user could like multiple times ❌
You lose tracking ❌

👉 Instead:

Count = number of Like objects for that post
🧩 4. COMMENT MODEL
✅ Fields:
user → ForeignKey(User)
post → ForeignKey(Post)
text → TextField
created_at → DateTimeField
🔗 Connection:
User 1 ─── ∞ Comments
Post 1 ─── ∞ Comments
📊 FINAL MODEL RELATION (IMPORTANT VISUAL)
User
 │
 ├── Profile (1-1)
 │
 ├── Post (1-many)
 │       │
 │       ├── Like (many-many via model)
 │       └── Comment (1-many)



