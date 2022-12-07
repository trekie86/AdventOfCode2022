from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from queue import Queue
from utils.fileutil import read_file_to_string_list

def part1():
    input = read_file_to_string_list("adventofcode/day7/input.txt")
    tree: File = assembleTree(input)
    calculateFolderSizes(tree)
    result = add_folder_at_most_size(tree, 100000)
    print(result)

def part2():
    input = read_file_to_string_list("adventofcode/day7/input.txt")
    tree: File = assembleTree(input)
    calculateFolderSizes(tree)
    max_space = 70000000
    min_free = 30000000
    in_use = max_space - tree.size
    print(f"We must free up {min_free-in_use}")
    result = find_min_to_free(tree, min_free - in_use)
    print(f"Deleting {result.name} with {result.size} space")
    pass

@dataclass
class File:
    isDir: bool
    name: str
    children: Optional[list[File]]
    parent: Optional[File]
    size: int = 0


def assembleTree(input: list[str]) -> File:
    root: File
    currentFile: File
    for step in input:
        if step.startswith("$ cd "):
            #This is a special case
            if step == "$ cd /":
                root = File(True, "/", [], None)
                currentFile = root
            elif step == "$ cd ..":
                currentFile = currentFile.parent
                continue
            else:
                name = step.replace("$ cd ", "")
                for x in currentFile.children:
                    if x.name == name:
                        currentFile = x
                        break
        elif step == "$ ls":
            continue
        elif step.startswith("dir"):
            name = step.replace("dir ", "")
            currentFile.children.append(File(True, name, [], currentFile))
        else:
            size, name = step.split(" ")
            size = int(size)
            currentFile.children.append(File(False, name, None, currentFile, size))

    return root

def calculateFolderSizes(tree: File) -> int:
    subTotal = 0
    if tree.isDir:
        for child in tree.children:
            subTotal += calculateFolderSizes(child)
        tree.size += subTotal
        return tree.size
    else:
        return tree.size

def add_folder_at_most_size(tree: File, max_size: int) -> int:
    if tree.isDir:
        if tree.size <= max_size:
            return tree.size + sum([add_folder_at_most_size(x, max_size) for x in tree.children])
        else:
            return sum([add_folder_at_most_size(x, max_size) for x in tree.children])
    else:
        return 0

def find_min_to_free(tree: File, to_free: int) -> File:
    max_to_clear = tree.size
    current_min = tree
    queue: Queue[File] = Queue()
    queue.put(tree)

    while not queue.empty():
        current = queue.get_nowait()
        if current.size < max_to_clear and current.size > to_free:
            current_min = current
        for x in current.children:
            if x.isDir and x.size >= to_free:
                queue.put(x)
    return current_min

if __name__ == "__main__":
    part1()
    part2()
