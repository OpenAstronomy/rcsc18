#!/bin/env xonsh
"""
Run a complete build of the stfc summer school webpage.
"""
pwd
cd notebooks
git clean -fxd
rm -rf 02-git/rcsc18_lessons
rm -rf 07-collaborating-with-git/rcsc18_lessons
git pull
cd ../
git add notebooks/
git commit -m "update notebooks before build"
rm -r _chapters/*
python scripts/generate_summary_from_folders.py notebooks/ --filename_split_char=- --overwrite
if "--no-run" not in $ARGS:
    python scripts/execute_all_notebooks.py
    rm -rf notebooks/02-git/rcsc18_lessons
    rm -rf notebooks/07-collaborating-with-git/rcsc18_lessons
python scripts/generate_textbook.py
# Reset the notebooks directory back now we have finished executing everything
cd notebooks
git reset --hard origin/master
git clean -fxd

if "--web" in $ARGS:
    git push web master
