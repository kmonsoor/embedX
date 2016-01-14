from setuptools import setup, find_packages

from embedx import __version__, __author__, __author_email__, __license__, __short_desc__, __source_url__

try:
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
        name='embedX',
        version=__version__,
        packages=find_packages(),
        url=__source_url__,
        license=__license__,
        author=__author__,
        author_email=__author_email__,
        description=__short_desc__,
        long_description=long_description,
        keywords=['embed', 'html', 'javascript', 'embeddable', 'code generation', 'from url'],
        platforms='any',
        install_requires=[],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python',
            'Environment :: Console',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'License :: OSI Approved :: MIT License',
            'Topic :: Utilities'
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
