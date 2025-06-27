import os

sandbox_dir = "./sandbox"
os.makedirs(sandbox_dir, exist_ok=True)

# All file operations restricted to this directory
with open(os.path.join(sandbox_dir, "file.txt"), "w") as f:
    f.write("Javed Store.\n")
    f.write("Hello Muhammad Javed.\n")
