from setuptools import setup, find_packages

setup(
        name='flocx', 
        version='0.1.0',
        maintainer='Sahil Tikale',
        url='https://github.com/CCI-MOC/flocx',
        description='A marketplace that enables sharing and trading '
        'of bare-metal servers among non-trusting stake-holders.',
        license='Apache 2.0',
        classifiers=[
            'Development Status :: Beta',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: Apache Software License, version 2.0',
            'Topic :: System :: Cloud :: Installation/Setup',
            'Environment :: Web Environment',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            ],
        packages=find_packages(),
        keywords='cloud cloud-economics bare-metal setuptools data-center',
        install_requires=[],
        extras_require={'tests': ['pytest>=4.0',]}
)




