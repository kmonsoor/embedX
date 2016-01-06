from setuptools import setup, find_packages

README = open('README.md')

setup(
        name='extract-video-id',
        version='0.0.3',
        packages=find_packages(),
        package_dir={'online_video'},
        url='https://github.com/kmonsoor/extract-video-id',
        license='MIT',
        author='Khaled Monsoor',
        author_email='k@kmonsoor.com',
        description='Library to extract video id from link and embedding',
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
