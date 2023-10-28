from .dependency_tree_creator import arg_parser, create_dependency_tree


def main():
    """
    The main function of the module.
    """
    # Parse the argument
    args = arg_parser()

    # Create the dependency tree
    result = create_dependency_tree(args.json_file)

    print(result)

if __name__ == "__main__":
    main()
