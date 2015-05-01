# coding: utf-8
from setuptools import setup
from setuptools.command.test import test as TestCommand
import io
import os
import sys

import hip2slack_emoji

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='hip2slack-emoji',
    version=hip2slack_emoji.__version__,
    url='http://github.com/ivancrneto/hip2slack-emoji/',
    license='MIT License',
    author='Ivan Rocha',
    tests_require=['pytest'],
    install_requires=read('requirements.txt'),
    cmdclass={'test': PyTest},
    author_email='ivan.cr.neto@gmail.com',
    description='Importer of Hipchat emojis to Slack',
    long_description=long_description,
    packages=['hip2slack_emoji'],
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    extras_require={
        'testing': ['pytest'],
    }
)
