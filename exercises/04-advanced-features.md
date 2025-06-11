# Exercise 4: Advanced Features

## 🎯 Learning Goals
- Use Git hooks for automation
- Set up GitHub Actions for CI/CD
- Use Git tags for versioning
- Explore advanced Git commands
- Understand Git workflows in teams

## 📋 Prerequisites
- Completed Exercises 1-3
- Basic understanding of Git workflows
- GitHub account with repository access

## 🚀 Let's Get Started!

### Step 1: Git Tags for Versioning

Tags are useful for marking important points in your project history (like releases):

```bash
# Create a lightweight tag
git tag v1.0.0

# Create an annotated tag with a message
git tag -a v1.0.0 -m "Release version 1.0.0"

# List all tags
git tag

# Push tags to remote
git push origin --tags
```

### Step 2: Git Hooks (Local Automation)

Git hooks are scripts that run automatically at certain points in the Git workflow:

```bash
# Navigate to the hooks directory
cd .git/hooks

# List available hooks
ls -la
```

Let's create a simple pre-commit hook:

```bash
# Create a pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
echo "Running pre-commit checks..."
echo "✅ All checks passed!"
EOF

# Make it executable
chmod +x .git/hooks/pre-commit
```

### Step 3: GitHub Actions for CI/CD

Create a simple GitHub Actions workflow:

```bash
# Create the workflows directory
mkdir -p .github/workflows
```

Create a basic CI workflow:

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest
    
    - name: Run tests
      run: |
        echo "Running tests..."
        # Add your test commands here
        echo "✅ All tests passed!"
    
    - name: Check file formatting
      run: |
        echo "Checking file formatting..."
        # Add formatting checks here
        echo "✅ Formatting looks good!"
```

### Step 4: Advanced Git Commands

#### Stashing Changes
```bash
# Save your current work without committing
git stash

# List stashes
git stash list

# Apply the most recent stash
git stash pop

# Apply a specific stash
git stash apply stash@{1}
```

#### Rebasing
```bash
# Rebase your branch on top of main
git checkout feature-branch
git rebase main

# Interactive rebase to clean up commits
git rebase -i HEAD~3
```

#### Cherry-picking
```bash
# Apply a specific commit to your current branch
git cherry-pick <commit-hash>
```

## 🎯 Practice Exercises

### Exercise 4.1: Version Management
1. Create multiple commits with different features
2. Tag important milestones (v0.1.0, v0.2.0, v1.0.0)
3. Create a release on GitHub with release notes
4. Practice checking out specific tags

### Exercise 4.2: Git Hooks
1. Create a pre-commit hook that checks for TODO comments
2. Create a post-commit hook that sends a notification
3. Test your hooks by making commits
4. Share your hooks with the class

### Exercise 4.3: GitHub Actions
1. Set up a workflow that runs tests on every push
2. Add a workflow that deploys to GitHub Pages
3. Create a workflow that checks code formatting
4. Monitor the Actions tab on GitHub

### Exercise 4.4: Advanced Workflows
1. Practice rebasing vs merging
2. Use cherry-picking to apply specific commits
3. Experiment with interactive rebase
4. Learn about Git bisect for finding bugs

## 🔍 Key Concepts to Understand

- **Tags**: Markers for important points in history (releases)
- **Hooks**: Automated scripts that run at Git events
- **GitHub Actions**: CI/CD automation in the cloud
- **Rebasing**: Replaying commits on top of another branch
- **Cherry-picking**: Applying specific commits to other branches

## 💡 Pro Tips

### Version Management
- Use semantic versioning (MAJOR.MINOR.PATCH)
- Tag releases consistently
- Write good release notes
- Use GitHub releases for distribution

### Automation
- Use hooks for local quality checks
- Set up CI/CD for automated testing
- Automate repetitive tasks
- Keep automation simple and reliable

### Advanced Git
- Use rebase to keep history clean
- Use cherry-pick for selective commits
- Learn interactive rebase for commit cleanup
- Use Git bisect for debugging

## 🚨 Common Pitfalls

### Rebasing
- Never rebase shared branches
- Be careful with force pushing
- Always backup before major operations

### Hooks
- Keep hooks lightweight
- Don't block commits unnecessarily
- Test hooks thoroughly

### Actions
- Start simple and add complexity gradually
- Monitor action execution times
- Use caching for dependencies

## ✅ Check Your Understanding

After completing this exercise, you should be able to:
- [ ] Create and manage Git tags
- [ ] Set up basic Git hooks
- [ ] Create GitHub Actions workflows
- [ ] Use advanced Git commands (stash, rebase, cherry-pick)
- [ ] Understand when to use different Git workflows
- [ ] Automate common development tasks

## 🆘 Need Help?

If you get stuck:
1. Check the [Git documentation](https://git-scm.com/doc)
2. Review [GitHub Actions documentation](https://docs.github.com/en/actions)
3. Ask your instructor or peers for help
4. Use `git help <command>` for command-specific help

## 🎉 Congratulations!

You've completed the advanced Git and GitHub tutorial! You now have a solid foundation for:
- Professional Git workflows
- Team collaboration
- Open source contribution
- Automated development processes

## 🚀 Next Steps

- Contribute to open source projects
- Set up Git workflows for your own projects
- Explore more advanced Git features
- Learn about Git hosting platforms (GitLab, Bitbucket)
- Practice with real-world scenarios

---

**You've completed all exercises!** 🎉

Consider this your graduation from Git basics to Git mastery! 