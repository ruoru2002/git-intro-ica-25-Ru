# Exercise 3: Collaborative Workflows

## 🎯 Learning Goals
- Understand the fork and pull request workflow
- Collaborate with others using GitHub
- Review and merge pull requests
- Use GitHub Issues for project management

## 📋 Prerequisites
- Completed Exercises 1 & 2
- GitHub account
- This repository forked to your account

## 🚀 Let's Get Started!

### Step 1: Fork the Repository

1. Go to the original repository on GitHub
2. Click the "Fork" button in the top right
3. Choose your account as the destination
4. Wait for the fork to complete

### Step 2: Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/git-intro-ica-25.git
cd git-intro-ica-25
```

### Step 3: Add the Original Repository as Upstream

```bash
git remote add upstream https://github.com/ORIGINAL_OWNER/git-intro-ica-25.git
git remote -v
```

You should see both `origin` (your fork) and `upstream` (original repo).

### Step 4: Create a Feature Branch

```bash
git checkout -b feature/student-contribution
```

### Step 5: Make Your Contribution

Let's add a new file to the demo-files directory:

```bash
echo "# Student Contribution" > demo-files/student-work.md
echo "" >> demo-files/student-work.md
echo "## What I Learned" >> demo-files/student-work.md
echo "- Git branching is powerful" >> demo-files/student-work.md
echo "- Collaboration is easier with version control" >> demo-files/student-work.md
echo "" >> demo-files/student-work.md
echo "## My Experience" >> demo-files/student-work.md
echo "This is my first contribution to an open source project!" >> demo-files/student-work.md
```

### Step 6: Commit and Push Your Changes

```bash
git add demo-files/student-work.md
git commit -m "Add student contribution example"
git push origin feature/student-contribution
```

### Step 7: Create a Pull Request

1. Go to your forked repository on GitHub
2. You should see a banner suggesting to create a pull request
3. Click "Compare & pull request"
4. Add a descriptive title and description
5. Click "Create pull request"

## 🎯 Practice Exercises

### Exercise 3.1: Issue-Based Development
1. Create a GitHub Issue describing a feature you want to add
2. Create a branch named after the issue (e.g., `issue-1-add-documentation`)
3. Make changes to address the issue
4. Reference the issue in your commit messages using `#1`
5. Create a pull request that closes the issue

### Exercise 3.2: Code Review Process
1. Pair up with another student
2. Review each other's pull requests
3. Leave constructive comments
4. Request changes if needed
5. Approve and merge the pull request

### Exercise 3.3: Collaborative Editing
1. Multiple students work on the same file
2. Create different branches for different sections
3. Merge changes and resolve conflicts
4. Practice the complete workflow

## 🔍 Key Concepts to Understand

- **Fork**: A copy of someone else's repository in your account
- **Pull Request**: A request to merge changes from one branch/repo to another
- **Code Review**: The process of reviewing code before merging
- **Upstream**: The original repository you forked from
- **Origin**: Your fork of the repository

## 💡 Pro Tips

- Always create a new branch for each feature/fix
- Use descriptive commit messages
- Reference issues in commit messages and PR descriptions
- Keep pull requests small and focused
- Respond to review comments promptly

## 🚨 Best Practices for Collaboration

### Commit Messages
```
feat: add new student contribution example
fix: correct typo in exercise instructions
docs: update README with new information
```

### Pull Request Descriptions
- Clearly describe what the PR does
- Reference related issues
- Include screenshots if UI changes
- Mention any breaking changes

### Code Review
- Be constructive and respectful
- Focus on the code, not the person
- Suggest improvements, don't just point out problems
- Use GitHub's inline commenting feature

## ✅ Check Your Understanding

After completing this exercise, you should be able to:
- [ ] Fork a repository
- [ ] Clone your fork locally
- [ ] Create feature branches
- [ ] Push changes to your fork
- [ ] Create pull requests
- [ ] Review and merge pull requests
- [ ] Use GitHub Issues for project management

## 🆘 Need Help?

If you get stuck:
1. Check GitHub's documentation on [pull requests](https://docs.github.com/en/pull-requests)
2. Use `git remote -v` to verify your remotes
3. Ask your instructor or peers for help
4. Check the [GitHub Guides](https://guides.github.com/)

## 🎉 Congratulations!

You've now learned the complete collaborative workflow! This is the foundation for contributing to open source projects and working in teams.

---

**Next up**: [Exercise 4: Advanced Features](../exercises/04-advanced-features.md) 