import re

from setuptools import setup

import cleverwrap

install_requires = [
    'requests',
]

req_re = re.compile(r'([^=\s]+)==([^\s]+)')
reqs_file = open('requirements.txt').read().splitlines()


def parse_contstraints():
    d = {}
    for line in reqs_file:
        # Ignore options and comments
        if line.startswith(('#', '-')):
            continue

        if '#' in line:
            line = line.split('#')[0]

        match = req_re.match(line)

        name, ver = match.groups()
        d[name] = ver

    return d


constraints = parse_contstraints()


def get_constraints(reqs):
    for name in reqs:
        yield '{}=={}'.format(name, constraints[name])


setup(
    name='cleverwrap',
    packages=['cleverwrap'],
    license='MIT',
    install_requires=get_constraints(install_requires),
    version='.'.join(cleverwrap.__version__),
    description='A wrapper for the official cleverbot.com API',
    author='Andrew Edwards',
    author_email='andrewthomasedwards@gmail.com',
    url='https://github.com/snoonetIRC/cleverwrap.py',
    keywords=['cleverbot', 'wrapper', 'clever'],
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
    ],
)
