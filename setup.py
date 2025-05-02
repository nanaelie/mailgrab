from setuptools import setup, find_packages
from mailgrab.__version__ import __version__

setup(
    name='mailgrab',
    version=__version__,
    author='nae.devp',
    author_email='nae.devp@gmail.com',
    description='Un outil Python pour extraire des adresses email depuis des pages web ou des fichiers texte.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nanaelie/mailgrab',
    packages=find_packages(),
    py_modules=['mailgrab'],
    install_requires=[
        'playwright>=1.44.0',
    ],
    entry_points={
        'console_scripts': [
            'mailgrab=mailgrab.mailgrab:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
    ],
    python_requires='>=3.7',
    include_package_data=True,
)
