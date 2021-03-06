"""
Simple Python Script that looks for changes in the files and commits them
to github
"""
import subprocess
import os
import datetime
import time


def git_add_and_commit():
    os.system(f'(git add . && git commit -m "{datetime.datetime.now()}" && git push) &')


if __name__ == "__main__":
    while True:
        output = subprocess.run(['git', 'status'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        if "nothing to commit, working tree clean" in output:
            pass
        else:
            git_add_and_commit()
        time.sleep(3600)