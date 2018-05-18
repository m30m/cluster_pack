import json
from string import Template


def visualize(root, path, size=960):
    tmpl = Template(open('template.html').read())
    output_result = open(path, 'w')
    output_result.write(tmpl.safe_substitute(json_root=json.dumps(root), size=size))
    output_result.close()


def visualize_inline(root, size=960):
    tmpl = Template(open('template.html').read())
    return tmpl.safe_substitute(json_root=json.dumps(root), size=size)


def visualize_notebook(*args, **kwargs):
    html = visualize_inline(*args, **kwargs)
    from IPython.core.display import display, HTML
    display(HTML(html))


if __name__ == '__main__':
    root = {}
    visualize(root, 'index.html', size=1200)
