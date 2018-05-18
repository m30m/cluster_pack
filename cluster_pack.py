import json
import random
import string
from string import Template

import pkg_resources


def __get_random_id():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))


def visualize(root, size=960):
    resource_package = __name__
    template = pkg_resources.resource_filename(resource_package, 'template.html')
    tmpl = Template(open(template).read())
    return tmpl.safe_substitute(json_root=json.dumps(root), size=size, svg_id=__get_random_id())


def visualize_notebook(*args, **kwargs):
    html = visualize(*args, **kwargs)
    from IPython.core.display import display, HTML
    display(HTML(html))
