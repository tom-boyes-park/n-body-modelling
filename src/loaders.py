import json


class Body:

    def __init__(self, x, vx, y, vy, mass, name):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.name = name


def load_config(config_path):
    with open(config_path, "r") as f:
        return json.load(f)


def load_body(b):
    """

    :param b: dict representation of body from config
    :return: Body with values set from b
    """
    required_keys = ["x", "y", "vx", "vy", "mass", "name"]
    for key in required_keys:
        if key not in b:
            raise Exception("'{}' value missing, unable to load body".format(key))

    x, y = b["x"], b["y"]
    vx, vy = b["vx"], b["vy"]
    name = b["name"]
    mass = b["mass"]

    print("Loaded Body: {}".format(name))

    return Body(x, y, vx, vy, mass, name)


def load_bodies(config_path):
    """

    :param config_path: path to config containing body parameters
    :return: list of Body classes with values set from config
    """

    config = load_config(config_path)

    bodies = []
    for b in config:
        body = load_body(b)
        bodies.append(body)

    return bodies
