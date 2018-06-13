import json
import random
import string
from string import Template

import pkg_resources


def __get_random_id():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))


def __check_size(root):
    if root.get('children'):
        if root.get('size'):
            raise Exception("Non-leaf nodes can't have size attribute\n size will be calculated using children nodes")
        for child in root['children']:
            __check_size(child)
    elif not root.get('size'):
        raise Exception("Leaf nodes should have size attribute")


def visualize(root, size=960):
    __check_size(root)
    resource_package = __name__
    template = pkg_resources.resource_filename(resource_package, 'template.html')
    tmpl = Template(open(template).read())
    return tmpl.safe_substitute(json_root=json.dumps(root), size=size, svg_id=__get_random_id())


def visualize_notebook(*args, **kwargs):
    html = visualize(*args, **kwargs)
    from IPython.core.display import display, HTML
    display(HTML(html))
