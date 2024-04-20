import glob
import os
import sys
from functools import reduce
from operator import add

extensions: list[str] = [
    "bat",
    "c",
    "cpp",
    "h",
    "hpp",
    "py",
    "txt"
]

def count_file_lines(file_path: str) -> int:
    with open(file_path, encoding="utf-8") as f:
        return len([1 for line in f])

# ディレクトリを再帰的に検索し全ファイルの行数を数える。
def count_dir_lines(dir_path: str) -> list[(str, int)]:
    file_paths: list[str] = []
    for extension in extensions:
        file_paths += [p for p in
            glob.glob("**/*." + extension, root_dir=dir_path, recursive=True)]

    results = []
    for file_path in file_paths:
        result = tuple([file_path,
            count_file_lines(os.path.join(dir_path, file_path))])
        results.append(result)
    return results

def count_lines(path: str) -> list[(str, int)]:
    if os.path.isfile(path):
        return tuple([path, count_flie_lines(path)])
    elif os.path.isdir(path):
        return count_dir_lines(path)

def main() -> None:
    if len(sys.argv) != 2:
        return
    path: str = sys.argv[1]

    results = count_lines(path)
    
    for file_path, count in results:
        print(file_path, count)
    total = reduce(add, [count for _, count in results])
    print("\ntotal: ", total)

if __name__ == "__main__":
    main()
