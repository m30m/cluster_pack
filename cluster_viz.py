import json
import random
import string
from string import Template


def __get_random_id():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))


def visualize(root, path, size=960):
    tmpl = Template(open('template.html').read())
    output_result = open(path, 'w')
    output_result.write(tmpl.safe_substitute(json_root=json.dumps(root), size=size, svg_id=__get_random_id()))
    output_result.close()


def visualize_inline(root, size=960):
    tmpl = Template(open('template.html').read())
    return tmpl.safe_substitute(json_root=json.dumps(root), size=size, svg_id=__get_random_id())


def visualize_notebook(*args, **kwargs):
    html = visualize_inline(*args, **kwargs)
    from IPython.core.display import display, HTML
    display(HTML(html))


if __name__ == '__main__':
    root = {}
    visualize(root, 'index.html', size=1200)
