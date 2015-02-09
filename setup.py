"""
Piano. Beginner friendly Plone development.
"""
from setuptools import find_packages, setup

dependencies = ['click','plock','requests','setuptools>=12.0.5']

setup(
    name='for-beginner-piano',
    version='0.3.0',
    url='https://github.com/for-beginner-piano/for-beginner-piano',
    license='BSD',
    author='David Bain',
    author_email='david@alteroo.com',
    description='Piano. Beginner friendly Plone development.',
    # long_description=__doc__,
    long_description=(
        open('README.rst').read() + '\n' +
        open('CHANGES.rst').read()
    ),
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='Linux, Mac',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'piano = piano.cli:cli',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        # 'Operating System :: Windows',
        'Framework :: Plone :: 4.3',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
