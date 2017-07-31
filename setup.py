#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


def get_version(*file_paths):
    """Retrieves the version from instagram_app_client/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("instagram_app_client", "__init__.py")

if sys.argv[-1] == 'publish':
    try:
        import wheel

        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()

setup(
    name='instagram-app-client',
    version=version,
    description="""A sample Django package""",
    long_description=readme + '\n\n',
    author='Dmytro Litvinov, Anton Linevych, Igor Margitych',
    author_email='dmytro.litvinov@softformance.com, anton.linevich@softformance.com',
    url='https://github.com/softformance/instagram-app-client',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.html', '*.js', '*.css', ],
    },
    install_requires=[
        'requests==2.18.2',
        'requests-cache==0.4.13',
    ],
    license="",
    zip_safe=False,
    keywords='instagram-app-client',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
