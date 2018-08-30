from glob import glob
from subprocess import check_call
from tqdm import tqdm
import nbformat

ipynb_files = glob('./notebooks/**/*_instructor.ipynb', recursive=True)
failed_files = []
for ifile in tqdm(ipynb_files):
    call = 'jupyter nbconvert --inplace --to notebook --allow-errors --execute {}'.format(ifile)
    try:
        out = check_call(call.split())
    except Exception:
        failed_files.append(ifile)

if failed_files:
    print('Failing files:')
for ifile in failed_files:
    print(ifile)


# for ifile in tqdm(ipynb_files):
#     nb = nbformat.read(ifile, as_version=4)
#     for ind, cell in enumerate(nb['cells']):
#         if "notebook_only" in cell.metadata:
#             nb['cells'].pop(ind)
#     nbformat.validate(nb)
#     nbformat.write(nb, ifile)
