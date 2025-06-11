# Exercise 2: Branching and Merging

## 🎯 Learning Goals
- Understand what branches are and why they're useful
- Create and switch between branches
- Merge changes from one branch to another
- Handle merge conflicts

## 📋 Prerequisites
- Completed Exercise 1
- Basic understanding of Git commits

## 🚀 Let's Get Started!

### Step 1: Check Current Branch

First, let's see which branch you're currently on:

```bash
git branch
```

You should see `main` (or `master`) with an asterisk (*) next to it.

### Step 2: Create Your First Branch

Let's create a new branch for a feature:

```bash
git branch feature/new-section
```

### Step 3: Switch to the New Branch

```bash
git checkout feature/new-section
```

Or use the newer syntax:
```bash
git switch feature/new-section
```

### Step 4: Verify You're on the New Branch

```bash
git branch
```

You should now see `feature/new-section` with the asterisk.

### Step 5: Make Changes on the Branch

Let's add a new section to your file:

```bash
echo "" >> my-first-file.md
echo "## New Feature Section" >> my-first-file.md
echo "This section was added on a feature branch!" >> my-first-file.md
echo "- Branching allows parallel development" >> my-first-file.md
echo "- Each branch can have different features" >> my-first-file.md
```

### Step 6: Commit Your Changes

```bash
git add my-first-file.md
git commit -m "Add new feature section on feature branch"
```

### Step 7: Switch Back to Main

```bash
git checkout main
```

### Step 8: Make Changes on Main

Let's make some changes on the main branch too:

```bash
echo "" >> my-first-file.md
echo "## Main Branch Changes" >> my-first-file.md
echo "This was added on the main branch!" >> my-first-file.md
```

```bash
git add my-first-file.md
git commit -m "Add changes on main branch"
```

### Step 9: Merge the Feature Branch

Now let's merge your feature branch into main:

```bash
git merge feature/new-section
```

## 🎯 Practice Exercises

### Exercise 2.1: Create Multiple Branches
1. Create a branch called `bugfix/typo-fix`
2. Switch to that branch
3. Fix a typo in your file
4. Commit the fix
5. Switch back to main and merge the fix

### Exercise 2.2: Parallel Development
1. Create two branches: `feature/a` and `feature/b`
2. Add different content to each branch
3. Merge both branches into main
4. Observe how Git combines the changes

### Exercise 2.3: Merge Conflicts (Advanced)
1. Create a branch and modify the same line in a file
2. Switch to main and modify the same line
3. Try to merge and resolve the conflict
4. Complete the merge

## 🔍 Key Concepts to Understand

- **Branch**: A separate line of development
- **Main/Master**: The primary branch (usually stable)
- **Feature Branch**: A branch for developing new features
- **Merge**: Combining changes from one branch into another
- **Merge Conflict**: When Git can't automatically merge changes

## 💡 Pro Tips

- Use descriptive branch names (e.g., `feature/user-login`, `bugfix/typo-fix`)
- Keep branches short-lived
- Always merge back to main when done
- Use `git branch -d <branch-name>` to delete branches after merging

## 🚨 Handling Merge Conflicts

If you encounter a merge conflict:

1. Git will mark the conflicted areas in your files
2. Edit the files to resolve conflicts
3. Remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
4. Stage the resolved files with `git add`
5. Complete the merge with `git commit`

## ✅ Check Your Understanding

After completing this exercise, you should be able to:
- [ ] Create new branches
- [ ] Switch between branches
- [ ] Make commits on different branches
- [ ] Merge branches together
- [ ] Understand when conflicts occur
- [ ] Resolve simple merge conflicts

## 🆘 Need Help?

If you get stuck:
1. Use `git branch` to see all branches
2. Use `git status` to understand your current state
3. Use `git log --oneline --graph` to visualize branch history
4. Ask your instructor or peers for help

---

**Next up**: [Exercise 3: Collaborative Workflows](../exercises/03-collaborative-workflows.md) 