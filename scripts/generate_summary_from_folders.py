import os
import argparse

from titlecase import titlecase

DESCRIPTION = ("Automatically generate a SUMMARY.md file from a collection"
               " of Jupyter Notebooks/markdown files that make a textbook."
               " The alpha-numeric name of folders/files will be used to choose the order of chapters.")

parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument("textbook_folder", default=None, help="Path to the folder where the textbook is stored.")
parser.add_argument("--out_path", default=None, help="Path to the folder where the output SUMMARY.md file will be written.")
parser.add_argument("--filename_split_char", default='_', help="The character used to split words in the file name. Used to generate titles from file names. Defaults to '_'")
parser.add_argument("--overwrite", action='store_true', help="Overwrite SUMMARY.md if it already exists.")


def files_to_markdown(files, indentation='  '):
    def key(l):
        return l[-1]
    files = sorted(files, key=key)
    md = []
    for title, link, level, order in files:
        md.append(level*indentation + '* [{}]({})'.format(title, link))
    md = [ii+'\n' for ii in md]
    return md


def titleize_list(segments, suffix=None):
    title = ' '.join(segments)
    if suffix:
        title = title.replace(suffix, "")
    return titlecase(title)


def notebooks_folder_to_files(notebooks_folder):
    last_folder = ''
    all_files = []
    order = 0
    for ii, (dirpath, dirnames, filenames) in enumerate(os.walk(notebooks_folder)):
        if '.ipynb_checkpoints' in dirpath:
            continue
        rel_folder = dirpath.split(notebooks_folder)[-1].strip('/')
        split_subfolders = rel_folder.split('/')
        level = len(split_subfolders) if split_subfolders[0] != '' else 0
        if last_folder != rel_folder:
            subfolder_title = titleize_list(split_subfolders[-1].split(
                args.filename_split_char))
            sf_parts = subfolder_title.split()
            try:
                # If first part of the filename is a number for ordering, remove it
                order = int(sf_parts[0])
                subfolder_title = " ".join(sf_parts[1:])
            except Exception:
                pass
            all_files.append((subfolder_title, '', level-1, order))

        filenames.sort()
        for filename in filenames:
            suffix = os.path.splitext(filename)[-1]
            if suffix not in ['.ipynb', '.md']:
                continue
            if suffix == ".ipynb":
                if "_instructor" not in filename:
                    continue
                else:
                    suffix = "_instructor.ipynb"
            filename_parts = filename.split(args.filename_split_char)
            try:
                # If first part of the filename is a number for ordering, remove it
                int(filename_parts[0])
                filename_parts = filename_parts[1:]
            except Exception:
                pass
            title = titleize_list(filename_parts, suffix)
            url = os.path.join(notebooks_folder, rel_folder, filename)
            last_folder = rel_folder
            all_files.append((title, url, level, order))
    # all_files = [ii for ii in all_files if len(ii[1]) > 0]
    return all_files


if __name__ == '__main__':
    args = parser.parse_args()
    if args.textbook_folder is None:
        args.textbook_folder = os.path.join('.', 'notebooks')
    if args.out_path is None:
        args.out_path = '.'

    files = notebooks_folder_to_files(args.textbook_folder)
    print('Found {} chapters'.format(len(files)))
    md = files_to_markdown(files)


    out_path_file = os.path.join(args.out_path, 'SUMMARY.md')
    if os.path.exists(out_path_file) and bool(args.overwrite) is False:
        raise ValueError('SUMMARY.md file exists, delete the file or set `overwrite=True`')
    with open(out_path_file, 'w') as ff:
        ff.writelines(md)
    print('Done!')
