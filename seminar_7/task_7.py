__all__ = ['sort_files']


from pathlib import Path
import os
import shutil
from task_6 import create_file,generate_file


def sort_files(path: str | Path, groups: dict[str:list[str]] = None) -> None:
    if not groups:
        groups = {
            Path('video'): ['avi', 'mov', 'mk4', 'mkv'],
            Path('images'): ['bmp', 'jpeg', 'jpg', 'png']
        }
    os.chdir(path)
    reverse_groups = {}
    for target_dir, ext_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
        for ext in ext_list:
            reverse_groups[f'.{ext}'] = target_dir
    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups:
           file.replace(reverse_groups[file.suffix] / file.name)


if __name__ == '__main__':
    generate_file(r"C:\Users\mariy\PycharmProjects\pythonProject\seminar_7\new", png=2, mkv=2, avi=1, jpg=1)
    sort_files(Path(r"C:\Users\mariy\PycharmProjects\pythonProject\seminar_7\new"))


