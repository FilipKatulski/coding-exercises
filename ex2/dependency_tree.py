"""
This script is responsible for creating a dependency tree for a given JSON file.

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

def create_dependency_tree(json_file_path: str) -> None:
    ...

def main():

    # Create an argument parser
    parser = argparse.ArgumentParser(description="Create a dependency tree for a given JSON file.")
    parser.add_argument("-f",
                         "--file", 
                        type=lambda x: _is_valid_path(parser, x), 
                        required=False, help="The path to the JSON file.", 
                        default=DEFAULT_JSON_FILE_PATH)
    parser.parse_args()
    
    print(parser)

    print(parser.file)


if __name__ == "__main__":
    main()
