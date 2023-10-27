"""
This script is responsible for creating a dependency tree for a given JSON file.
If not specified otherwise, the script will use the default JSON file path, "example1.json".
"""
import argparse
import json
import os

# The default path to the JSON file, in case the user doesn't provide one as an argument
DEFAULT_JSON_FILE_PATH = "example1.json"

class DependencyTree:
    """
    A class that represents a dependency tree structure.
    Rather than holing it as a single string, I hold it as a list of strings,
    where each string represents a single line in the tree.
    """
    def __init__(self):
        self.structure = []

    def __str__(self):
        return "\n".join(self.structure)

def _is_valid_path(parser, arg):
    """
    Checks if the file exists.
    """
    if not os.path.exists(arg):
        parser.error(f"The specified file '{arg}' does not exist.\n")
        os.makedirs(arg)
    else:
        return arg

def arg_parser() -> argparse.Namespace:
    """
    Creates an argument parser for the script.
    """
    parser = argparse.ArgumentParser(description="Create a dependency tree for a given JSON file.")
    parser.add_argument("-f",
                         "--json-file", 
                        type=lambda x: _is_valid_path(parser, x), 
                        required=False, 
                        help="The path to the JSON file.", 
                        default=DEFAULT_JSON_FILE_PATH)
    
    return parser.parse_args()

def _traverse_tree(pkg, data: dict, structure_output: DependencyTree, indent = "- ") -> None:
    """
    Traverses the dependency tree.
    """
    # print(f"{indent}{pkg}")
    structure_output.structure.append(f"{indent}{pkg}")
    if pkg in data:
        for dependency in data[pkg]:
            _traverse_tree(pkg=dependency, data=data, structure_output=structure_output, indent="  " + indent)
    

def create_dependency_tree(json_file_path: str) -> DependencyTree:
    """
    Creates a dependency tree object for a given JSON file.
    """
    with open(json_file_path, "r") as json_file:
        json_data = json.load(json_file)
        # print(json_data)
    
    # create a dependency tree object
    dep_tree = DependencyTree()

    for package in json_data:
        _traverse_tree(package, data=json_data, structure_output=dep_tree)

    return dep_tree

def main():
    """
    The main function of the script.
    """
    # Parse the argument
    args = arg_parser()

    # Create the dependency tree
    result = create_dependency_tree(args.json_file)

    print("Dependency tree structure:")
    print(result)

if __name__ == "__main__":
    main()
