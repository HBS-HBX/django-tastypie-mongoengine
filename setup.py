#!/usr/bin/env python

import os

from setuptools import setup, find_packages

try:
    # Workaround for http://bugs.python.org/issue15881
    import multiprocessing
except ImportError:
    pass

VERSION = '0.4.8'

if __name__ == '__main__':
    setup(
        name = 'django-tastypie-mongoengine',
        version = VERSION,
        description="MongoEngine support for django-tastypie.",
        long_description = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
        author = 'wlan slovenija',
        author_email = 'open@wlan-si.net',
        url = 'https://github.com/wlanslovenija/django-tastypie-mongoengine',
        keywords = "REST RESTful tastypie mongo mongodb mongoengine django",
        license = 'AGPLv3',
        packages = find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
        classifiers = (
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU Affero General Public License v3',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Framework :: Django',
        ),
        zip_safe = False,
        install_requires = (
            'Django>=1.10.5,<=2.3',
            'django-tastypie>=0.13.3',
            'mongoengine>=0.13.0',
            'python-dateutil>=2.5.0',
            'lxml',
            'defusedxml',
            'PyYAML',
            'biplist',
            'python-mimeparse>=1.5.0',
        ),
        test_suite = 'tests.runtests.runtests',
        tests_require = (
            'nose',
        ),
    )
