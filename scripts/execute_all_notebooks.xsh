#! /bin/env xonsh
from tqdm import tqdm

ipynb_files = g`./notebooks/**/*_instructor.ipynb`
failed_files = []
for ifile in tqdm(ipynb_files):
    a = !(jupyter nbconvert --inplace --to notebook --allow-errors --execute @(ifile))
    if a.returncode != 0:
        failed_files.append(ifile)

print('Failing files:')
for ifile in failed_files:
    print(ifile)
