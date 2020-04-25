def true_trivial():
    import yaml
    data = input()
    loaded = yaml.load(data)
    print(loaded)


def true_import_from():
    from yaml import load
    data = input()
    loaded = load(data)
    print(loaded)


def false_relative_import():
    from .yaml import load
    data = input()
    loaded = load(data)
    print(loaded)


def true_import_as():
    import yaml as y
    data = input()
    loaded = y.load(data)
    print(loaded)


def false_custom_f_not_used():
    import yaml
    def load(x):
        return x + "load"

    data = input()
    loaded = load(data)
    print(loaded)


def true_import_from_as_rename():
    from yaml import load as ld
    data = input()
    loaded = ld(data)
    print(loaded)
