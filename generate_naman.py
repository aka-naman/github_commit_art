import os
import subprocess
import datetime

# Define the letter matrices (7 rows, 5 columns)
# 1 represents a commit pixel, 0 represents empty
N = [
    [1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1]
]

A = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1]
]

M = [
    [1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1]
]

# Initialize a 7x53 grid (Sunday to Saturday, 53 weeks)
grid = [[0 for _ in range(53)] for _ in range(7)]

# Letter placements (column offsets)
# Total width = 5 + 1 + 5 + 1 + 5 + 1 + 5 + 1 + 5 = 29 columns
# Symmetric centering: (53 - 29) / 2 = 12 columns margin on each side
letter_offsets = [12, 18, 24, 30, 36]
letters = [N, A, M, A, N]

for offset, letter in zip(letter_offsets, letters):
    for r in range(7):
        for c in range(5):
            grid[r][offset + c] = letter[r][c]

def print_preview():
    print("\n--- GitHub Contribution Graph Preview (NAMAN) ---")
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    for r in range(7):
        row_str = "".join("#" if grid[r][c] == 1 else "." for c in range(53))
        print(f"{days[r]} {row_str}")
    print("-" * 60)

def main():
    print_preview()
    
    # Target directory for the new git repository
    target_dir = os.path.join(os.getcwd(), "naman-2019")
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created directory: {target_dir}")
        
    os.chdir(target_dir)
    
    # Initialize git repo
    subprocess.run(["git", "init", "-b", "main"], check=True)
    print("Initialized empty Git repository in naman-2019.")
    
    # Configure local git repository if user hasn't set name/email globally, to avoid commit errors
    # We will use dummy info but it is better to preserve theirs if it exists.
    # Let's check if git user.name and user.email are set.
    name_check = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True)
    email_check = subprocess.run(["git", "config", "user.email"], capture_output=True, text=True)
    
    if not name_check.stdout.strip():
        subprocess.run(["git", "config", "user.name", "Naman"], check=True)
        print("Configured local git user.name to 'Naman'")
    if not email_check.stdout.strip():
        subprocess.run(["git", "config", "user.email", "naman@example.com"], check=True)
        print("Configured local git user.email to 'naman@example.com'")

    # Create an initial file to track
    readme_path = "README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# NAMAN 2019 Contribution Art\n\nGenerated automatically to display 'NAMAN' on the GitHub contribution map for the year 2019.\n")
    
    subprocess.run(["git", "add", "README.md"], check=True)
    
    # Calculate dates
    # Jan 1, 2019 was a Tuesday. The Sunday of that week was Dec 30, 2018.
    base_sunday = datetime.date(2018, 12, 30)
    
    # Commits configuration
    commits_per_pixel = 12
    total_commits = 0
    
    print("Generating commits. Please wait...")
    
    for c in range(53):
        for r in range(7):
            if grid[r][c] == 1:
                # Calculate the date for this column/row
                target_date = base_sunday + datetime.timedelta(days = c * 7 + r)
                
                # Format date for Git environment variables
                # Git dates are in ISO 8601 format: YYYY-MM-DDTHH:MM:SS
                date_str = target_date.strftime("%Y-%m-%dT12:00:00")
                
                # Make multiple commits for the target date to ensure maximum color depth
                for i in range(commits_per_pixel):
                    # We slightly alter the file content or make empty commits.
                    # Empty commits are fast, clean, and count on GitHub.
                    env = os.environ.copy()
                    env["GIT_AUTHOR_DATE"] = date_str
                    env["GIT_COMMITTER_DATE"] = date_str
                    
                    subprocess.run(
                        ["git", "commit", "--allow-empty", "-m", f"Contribution Art - Pixel ({c},{r}) commit {i+1}"],
                        env=env,
                        capture_output=True,
                        check=True
                    )
                    total_commits += 1

    print(f"\nSuccessfully generated {total_commits} backdated commits in 2019!")
    print("\nHow to display this on GitHub:")
    print("1. Go to https://github.com and create a new repository named 'naman-2019'.")
    print("2. Link your local repository to GitHub by running:")
    print("   git remote add origin https://github.com/YOUR_USERNAME/naman-2019.git")
    print("3. Push the main branch to GitHub:")
    print("   git push -u origin main")
    print("\nNote: Make sure your GitHub account is configured with the same email used in these commits.")
    print("If you pushed to a private repository, ensure 'Contribution settings -> Private contributions' is enabled in your GitHub profile settings.")

if __name__ == "__main__":
    main()
