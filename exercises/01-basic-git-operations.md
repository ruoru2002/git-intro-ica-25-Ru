# Exercise 1: Basic Git Operations

## 🎯 Learning Goals
- Understand the Git workflow (working directory → staging area → repository)
- Make your first commit
- View commit history
- Understand the difference between tracked and untracked files

## 📋 Prerequisites
- Git installed and configured
- This repository cloned to your local machine

## 🚀 Let's Get Started!

### Step 1: Check Your Git Status

First, let's see what Git knows about your repository:

```bash
git status
```

You should see information about which files are tracked, modified, or untracked.

### Step 2: Create Your First File

Let's create a simple file to practice with:

```bash
echo "# My First Git Project" > my-first-file.md
echo "" >> my-first-file.md
echo "This is my first file in Git!" >> my-first-file.md
echo "" >> my-first-file.md
echo "## What I Learned Today" >> my-first-file.md
echo "- Git is awesome" >> my-first-file.md
echo "- Version control is important" >> my-first-file.md
```

### Step 3: Check Status Again

```bash
git status
```

Notice that `my-first-file.md` appears as an "untracked file" in red.

### Step 4: Add File to Staging Area

```bash
git add my-first-file.md
```

### Step 5: Check Status One More Time

```bash
git status
```

Now the file should appear in green as "Changes to be committed".

### Step 6: Make Your First Commit

```bash
git commit -m "Add my first file with Git basics"
```

### Step 7: View Commit History

```bash
git log --oneline
```

You should see your commit with a unique hash and your commit message.

## 🎯 Practice Exercises

### Exercise 1.1: Modify and Commit
1. Edit `my-first-file.md` and add a new section
2. Check the status with `git status`
3. Stage your changes with `git add`
4. Commit with a descriptive message

### Exercise 1.2: Multiple Files
1. Create a new file called `notes.txt`
2. Add some content to it
3. Stage and commit both files in separate steps
4. Use `git log` to see your commit history

### Exercise 1.3: Understanding the Staging Area
1. Make changes to multiple files
2. Stage only some of them with `git add <filename>`
3. Check status to see the difference
4. Commit only the staged changes

## 🔍 Key Concepts to Understand

- **Working Directory**: Where you make changes to files
- **Staging Area**: Where you prepare changes for commit
- **Repository**: Where committed changes are permanently stored
- **Commit**: A snapshot of your code at a specific point in time

## 💡 Pro Tips

- Use descriptive commit messages
- Check `git status` frequently
- Use `git log --oneline` for a compact view of history
- Use `git diff` to see what changes you've made

## ✅ Check Your Understanding

After completing this exercise, you should be able to:
- [ ] Create and modify files
- [ ] Stage changes with `git add`
- [ ] Commit changes with descriptive messages
- [ ] View commit history
- [ ] Understand the difference between tracked and untracked files

## 🆘 Need Help?

If you get stuck:
1. Use `git status` to understand your current state
2. Use `git log --oneline` to see your commit history
3. Ask your instructor or peers for help
4. Check the [Git documentation](https://git-scm.com/doc)

---

**Next up**: [Exercise 2: Branching and Merging](../exercises/02-branching-and-merging.md) 