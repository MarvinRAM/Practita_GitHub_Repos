import os
import subprocess
import time
import webbrowser
import winger

git_dir = r"C:\Users\Admin\Desktop\Marvin"

repos = [name for name in os.listdir(git_dir)
         if os.path.isdir(os.path.join(git_dir, name)) and
         os.path.exists(os.path.join(git_dir, name, ".git"))]

