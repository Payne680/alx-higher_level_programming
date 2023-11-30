#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Print sorted names from the directory
    for name in sorted(dir(hidden_4)):
        # Print only names that do not start with __
        if not name.startswith('__'):
            print("{}".format(name))
