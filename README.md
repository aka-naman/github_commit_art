# 🎨 NAMAN 2019 Contribution Graph Art

This repository is designed to paint the name **"NAMAN"** onto your GitHub Contribution Graph for the year **2019** using backdated Git commits.

---

## 📅 Preview of the Graph

Once pushed to GitHub, your contribution calendar for 2019 will render the following pixel art:

```text
Sun ............#...#..###..#...#..###..#...#............
Mon ............##..#.#...#.##.##.#...#.##..#............
Tue ............#.#.#.#...#.#.#.#.#...#.#.#.#............
Wed ............#.#.#.#####.#.#.#.#####.#.#.#............
Thu ............#..##.#...#.#...#.#...#.#..##............
Fri ............#...#.#...#.#...#.#...#.#...#............
Sat ............#...#.#...#.#...#.#...#.#...#............
```
*Note: `#` represents a green contribution square and `.` represents an empty square.*

---

## 🚀 How to Apply This to Your Profile

Follow these simple steps to push the contribution art to your GitHub profile:

### 1. Create a Repository on GitHub
Go to GitHub and create a new repository:
* **Repository name**: `naman-2019`
* **Visibility**: You can choose either **Public** or **Private**.
* *Do not initialize the repository with a README, .gitignore, or license.*

### 2. Link This Local Repo to GitHub
Open your terminal or command prompt inside the `naman-2019` directory and link the remote URL:
```bash
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/naman-2019.git
```
*(Be sure to replace `YOUR_GITHUB_USERNAME` with your actual GitHub username).*

### 3. Push to GitHub
Push the commits to the default branch (`main`):
```bash
git push -u origin main
```

---

## ⚙️ Essential Troubleshooting & Setup

* **Email Match**: GitHub attributes commits to your profile based on the email address configured in the commits. Ensure the email registered in this local repository matches one of the verified emails in your [GitHub Emails Settings](https://github.com/settings/emails).
  You can check your local repo email config using:
  ```bash
  git config user.email
  ```
* **Private Repository Setting**: If you pushed to a **Private** repository, the contributions will not be visible to the public (or even to you by default) unless you enable them. 
  To fix this:
  1. Go to your GitHub profile page (`https://github.com/YOUR_USERNAME`).
  2. Click **Contribution settings** (dropdown near the top-right of your contribution graph).
  3. Check the box for **Private contributions**.

---

## 🔍 How It Works
If you want to understand the underlying mechanics, calculations, and git scripts used to build this, check out the detailed guide:
* **[working.md](./working.md)**
