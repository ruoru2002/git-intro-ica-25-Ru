# Instructor Guide: Interactive Git Demo

## 🎯 Overview

This guide will help you run an interactive Git and GitHub tutorial with your students. The demo is designed to be hands-on, collaborative, and progressive - building from basic concepts to advanced workflows.

## 📋 Prerequisites for Students

Before the session, students should have:
- Git installed on their machines
- GitHub accounts created
- Basic command line familiarity
- Access to the internet

## 🚀 Session Setup (30 minutes)

### 1. Repository Setup
- Ensure this repository is public on GitHub
- Students will fork this repository during the session
- Have the presentation ready (`presentation.ipynb`)

### 2. Student Preparation
- Ask students to create GitHub accounts if they don't have one
- Have them install Git if needed
- Provide the repository URL for forking

### 3. Environment Check
Run these commands to verify everything is working:
```bash
git --version
git config --list
```

## 📚 Session Flow (2-3 hours)

### Part 1: Introduction (30 minutes)
1. **Present the slides** (`presentation.ipynb`)
2. **Explain the learning objectives**
3. **Set expectations** for hands-on participation
4. **Answer questions** about Git concepts

### Part 2: Basic Git Operations (45 minutes)
1. **Guide students through Exercise 1**
2. **Monitor progress** and help with issues
3. **Demonstrate key commands** on screen
4. **Encourage questions** and discussion

**Key Commands to Demonstrate:**
```bash
git status
git add
git commit
git log --oneline
```

### Part 3: Branching and Merging (45 minutes)
1. **Walk through Exercise 2**
2. **Show branch visualization** using `git log --graph`
3. **Demonstrate merge conflicts** intentionally
4. **Help students resolve conflicts**

**Key Commands to Demonstrate:**
```bash
git branch
git checkout
git merge
git log --oneline --graph
```

### Part 4: Collaborative Workflows (45 minutes)
1. **Guide forking process**
2. **Help with pull request creation**
3. **Facilitate code reviews** between students
4. **Demonstrate GitHub features**

**Key Concepts to Emphasize:**
- Fork vs Clone
- Pull Request workflow
- Code review process
- Issue management

### Part 5: Advanced Features (30 minutes)
1. **Introduce GitHub Actions**
2. **Show Git hooks** (if time permits)
3. **Demonstrate tagging**
4. **Discuss real-world applications**

## 🎯 Interactive Elements

### Student Pairing
- Pair students for collaborative exercises
- Have them review each other's pull requests
- Encourage discussion about merge conflicts

### Real-time Demonstrations
- Use screen sharing to show Git commands
- Demonstrate GitHub interface features
- Show the Actions tab in real-time

### Q&A Sessions
- Pause between exercises for questions
- Use student questions to guide discussion
- Encourage peer-to-peer help

## 🚨 Common Issues and Solutions

### Git Configuration Issues
```bash
# If students haven't configured Git
git config --global user.name "Student Name"
git config --global user.email "student@email.com"
```

### Permission Issues
- Help students set up SSH keys or use HTTPS
- Guide them through GitHub authentication
- Troubleshoot push/pull permission errors

### Merge Conflicts
- Use the `conflict-example.txt` file for practice
- Show students how to identify conflict markers
- Guide them through resolution process

### Network Issues
- Have offline alternatives ready
- Use local Git repositories for practice
- Provide screenshots of GitHub interface

## 📊 Assessment and Feedback

### Progress Tracking
- Use the `student-checklist.md` file
- Monitor completion of exercises
- Check pull request submissions

### Student Feedback
- Ask for questions throughout
- Use quick polls to gauge understanding
- Collect feedback at the end

### Success Metrics
- All students create at least one commit
- Most students complete a pull request
- Students can explain basic Git concepts
- Students feel confident using Git

## 🎉 Wrap-up Activities

### 1. Student Showcase
- Have students share their contributions
- Show interesting pull requests
- Highlight good commit messages

### 2. Real-world Applications
- Discuss how Git is used in industry
- Show examples of open source projects
- Talk about career benefits

### 3. Next Steps
- Provide resources for continued learning
- Suggest projects to practice with
- Encourage open source contributions

## 📚 Additional Resources

### For Students
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

### For Instructors
- [GitHub Education](https://education.github.com/)
- [GitHub Classroom](https://classroom.github.com/)
- [GitHub Skills](https://skills.github.com/)

## 🛠️ Customization Options

### Time Constraints
- **Short session (1 hour)**: Focus on Exercises 1-2
- **Medium session (2 hours)**: Include Exercise 3
- **Full session (3 hours)**: Complete all exercises

### Skill Levels
- **Beginners**: Focus on basic commands and concepts
- **Intermediate**: Emphasize branching and collaboration
- **Advanced**: Cover advanced features and automation

### Class Size
- **Small groups (5-10)**: Individual attention, detailed guidance
- **Medium groups (10-25)**: Pair programming, peer support
- **Large groups (25+)**: More structured approach, TAs helpful

## 🎯 Learning Outcomes

By the end of this session, students should be able to:
- Use basic Git commands confidently
- Understand branching and merging workflows
- Collaborate using GitHub pull requests
- Apply Git concepts to real projects
- Continue learning independently

---

**Remember**: The goal is to make students comfortable with Git and excited about version control. Focus on practical skills they can use immediately in their projects! 