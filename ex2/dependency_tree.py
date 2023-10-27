"""
This script is responsible for creating a dependency tree for a given JSON file.
If not specified otherwise, the script will use the default JSON file path, "example1.json".
"""
import argparse
import json
import os

# The default path to the JSON file, in case the user doesn't provide one as an argument
DEFAULT_JSON_FILE_PATH = "example1.json"

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

def _traverse_tree(pkg, data: dict, indent = "- ") -> None:
    """
    Traverses the dependency tree.
    """
    print(f"{indent}{pkg}")
    if pkg in data:
        for dependency in data[pkg]:
            _traverse_tree(dependency, data, "  " + indent)

def create_dependency_tree(json_file_path: str) -> None:
    """
    Creates a dependency tree for a given JSON file.
    """
    with open(json_file_path, "r") as json_file:
        data = json.load(json_file)
        print(data)
    
    for pkg in data:
        _traverse_tree(pkg, data)


def main():
    """
    The main function of the script.
    """
    # Parse the arguments
    args = arg_parser()
    print(args.json_file)

    # Create the dependency tree
    create_dependency_tree(args.json_file)


if __name__ == "__main__":
    main()
