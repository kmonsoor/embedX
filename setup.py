from setuptools import setup, find_packages

README = open('README.md')

setup(
        name='embedX',
        version='0.0.3',
        packages=find_packages(),
        url='https://github.com/kmonsoor/embedX',
        license='MIT',
        author='Khaled Monsoor',
        author_email='k@kmonsoor.com',
        description='Generate embeddable HTML or JavaScript code for a online content from its URL in single step',
        long_description=README,
        platforms='any',
        install_requires=[],
        classifiers=[
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
