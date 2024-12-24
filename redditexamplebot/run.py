# /usr/bin/env python3

"""
Example basic Reddit bot 
Created 2024-12-24
Updated 2024-12-24
"""
# Import third-party PyPI libraries
import praw

# Import local files
from constants import USERNAME


def main():
    r = praw.Reddit("bot1")
    user = r.redditor(USERNAME)

    for saved_content in user.saved(limit=5):
        print(saved_content)


if __name__ == "__main__":
    main()
