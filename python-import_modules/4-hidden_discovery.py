#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    sorted_names = sorted(filter(lambda x: not x.startswith('__'), names))

    for name in sorted_names:
        print(name)
