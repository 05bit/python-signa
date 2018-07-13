"""One lib to sign them all.
"""
from setuptools import setup, find_packages

__version__ = None

with open('signa/__init__.py') as module_fp:
    for line in module_fp:
        if line.startswith('__version__'):
            __version__ = line.split('=')[1].strip().strip("'").strip('"')
            break

setup(
    name='signa',
    version=__version__,
    author="Alexey Kinëv",
    author_email='rudy@05bit.com',
    url='https://github.com/05bit/python-signa',
    description=__doc__,
    # long_description=__doc__,
    license='MIT',
    # zip_safe=False,
    packages=find_packages(),
    # include_package_data=True,
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
    test_loader='unittest:TestLoader',
)
