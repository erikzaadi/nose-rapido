from setuptools import setup, find_packages
from os.path import realpath, join, dirname
from noserapido import NoseRapidoNotifier, get_version


BASE = dirname(realpath(__file__))

with open(join(BASE, 'README.rst')) as readme:
    long_description = readme.read()
with open(join(BASE, 'requirements.txt')) as reqs:
    requirements = [line.replace("\n", "") for line in reqs.readlines()]
with open(join(BASE, 'requirements-dev.txt')) as dev_reqs:
    dev_requirements = [line.replace(
        "\n", "") for line in dev_reqs.readlines()]

version_str = get_version()

dev_requirements = requirements + dev_requirements[1:]

setup(
    name='nose-rapido',
    version=version_str,
    author='Erik Zaadi',
    description=NoseRapidoNotifier.__doc__,
    url='https://github.com/erikzaadi/nose-rapido',
    download_url="https://github.com/erikzaadi/nose-rapido/tarball/" +
    version_str,
    packages=find_packages(),
    long_description=long_description,
    license="apache2",
    setup_requires=requirements,
    tests_require=dev_requirements,
    keywords=['testing', 'nose', 'nose plugin', 'tdd'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing',
    ],
    entry_points={
        'nose.plugins': [
            'rapido = noserapido:NoseRapidoNotifier'
        ]
    }
)
