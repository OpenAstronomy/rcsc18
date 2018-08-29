from glob import glob
from subprocess import check_call
from tqdm import tqdm

ipynb_files = glob('./notebooks/**/*_instructor.ipynb', recursive=True)
failed_files = []
for ifile in tqdm(ipynb_files):
    call = 'jupyter nbconvert --inplace --to notebook --allow-errors --execute {}'.format(ifile)
    try:
        out = check_call(call.split())
    except Exception:
        failed_files.append(ifile)

print('Failing files:')
for ifile in failed_files:
    print(ifile)
