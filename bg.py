"""
File  :    bg.py
Author:    ershan
mail  :    ershan_coding@outlook.com
desc  :    Handy background python tools.
"""
import pathlib

import keyboard


curdir = pathlib.Path(__file__).parent


def parse_cfg():
    li = []
    cfg = curdir / "bg_cfg.txt"

    if not cfg.exists():
        with open(cfg, "w") as f:
            pass

    with open(cfg) as f:
        for line in f:
            k, v = line.strip().split("\t")
            li.append((k, v))

    return li


li = [
    # for daily
    ("lht", "localhost"),
    ("lht1", "127.0.0.1"),
    # for django
    ("djp", "django-admin startproject "),
    ("djapp", "python manage.py startapp "),
    ("djr", "python manage.py runserver"),
    ("djmk", "python manage.py makemigrations"),
    ("djmi", "python manage.py migrate"),
    ("djcs", "python manage.py createsuperuser"),
    ("djs", "python manage.py shell"),
    # for conda
    ("cde", "conda deactivate"),
    ("cda", "conda activate "),
    ("cdi", "conda install -y "),
    ("cdc", "conda create -y -n "),
    # for pip
    ("pipi", "pip install "),
    ("pipr", "pip install -r requirements.txt"),
    # for git
    ("ga", "git add "),
    ("gba", "git branch -av"),
    ("gc", "git checkout "),
    ("gcb", "git checkout -b "),
    ("gd", "git diff "),
    ("gm", 'git commit -m""'),
    ("gp", "git push "),
    ("gpl", "git pull "),
    ("gs", "git status"),
    ("gst", "git stash"),
    # for code insiders
    ("cii", "code-insiders --install-extension "),
    ("ci", "code-insiders "),
    # for code 
    ("codei", "code --install-extension "),
]

li.extend(parse_cfg())


def abbr():
    for t in li:
        keyboard.add_abbreviation(*t)


if __name__ == "__main__":
    try:
        abbr()
        keyboard.wait()
    except KeyboardInterrupt:
        pass
