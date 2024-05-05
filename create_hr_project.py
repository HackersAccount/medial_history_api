import os
import subprocess

def generate_project_structure(project_name):
    # Create project directory
    os.makedirs(project_name)
    os.chdir(project_name)

    # Create app directory structure
    os.makedirs("app/models")
    os.makedirs("app/routes")
    os.makedirs("app/security")
    os.makedirs("app/utils")

    # Create tests directory structure
    os.makedirs("tests/test_routes")
    os.makedirs("tests/test_security")
    os.makedirs("tests/test_utils")

    # Create __init__.py files
    open("app/__init__.py", "a").close()
    open("app/models/__init__.py", "a").close()
    open("app/routes/__init__.py", "a").close()
    open("app/security/__init__.py", "a").close()
    open("app/utils/__init__.py", "a").close()
    open("tests/__init__.py", "a").close()
    open("tests/test_routes/__init__.py", "a").close()
    open("tests/test_security/__init__.py", "a").close()
    open("tests/test_utils/__init__.py", "a").close()

    # Create main.py and requirements.txt
    open("app/main.py", "a").close()
    with open("requirements.txt", "w") as req_file:
        req_file.write("fastapi\nuvicorn")

    # Create README.md
    with open("README.md", "w") as readme_file:
        readme_file.write("# " + project_name + "\n\nThis is a FastAPI project for managing electronic health records.")

def initialize_git_repo(project_name):
    # Initialize git repository
    subprocess.run(["git", "init"])
    # Stage all files
    subprocess.run(["git", "add", "."])
    # Commit with initial message
    subprocess.run(["git", "commit", "-m", "Initial commit: Project setup"])
    # Create GitHub repository
    subprocess.run(["gh", "repo", "create", project_name, "--confirm"])

def main():
    project_name = input("Enter the project name: ")
    generate_project_structure(project_name)
    initialize_git_repo(project_name)
    print("Project setup completed successfully!")

if __name__ == "__main__":
    main()

