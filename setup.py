from setuptools import setup

NAME = 'username-generator'
VERSION = '0.1'
DESCRIPTION = 'A package for generating usernames based on categories.'
LONG_DESCRIPTION = 'This package provides a simple interface for generating usernames based on a chosen category.'
AUTHOR = 'pn_radhakrishna'
AUTHOR_EMAIL = 'soupornochakraborty40@gmail.com'
LICENSE = 'MIT'
URL = 'https://github.com/yourusername/username-generator'
DOWNLOAD_URL = 'https://github.com/yourusername/username-generator/archive/v_01.tar.gz'
KEYWORDS = ['username', 'generator', 'categories']
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
]
PACKAGES = ['username_generator']
REQUIRES = ['pydantic']

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    url=URL,
    download_url=DOWNLOAD_URL,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=PACKAGES,
    requires=REQUIRES
)