from fabric.api import local
from jinja2 import Environment, FileSystemLoader
from ConfigParser import SafeConfigParser
from os import path
from datetime import datetime as date

template_env = Environment(loader=FileSystemLoader('.'))

src_index = path.join('src', 'index.html')

parser = SafeConfigParser()
parser.read('settings.cfg')
reveal_dir = parser.get('Reveal', 'Dir')
reveal_index = path.join(reveal_dir, 'index.html')

def build():
    template = template_env.get_template(src_index)
    rendered_template = template.render()
    with open(reveal_index, 'wb') as fh:
        fh.write(rendered_template.encode('utf-8'))
    print (date.now().strftime('%H:%M:%S')),