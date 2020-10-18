"""One lib to sign them all.
"""
from setuptools import setup, find_packages

__version__ = None

__description__ = None

with open('signa/__init__.py') as module_fp:
    for line in module_fp:
        if line.startswith('__version__'):
            __version__ = line.split('=')[1].strip().strip("'").strip('"')
            break

with open('README.md', 'r') as readme_fp:
    __description__ = readme_fp.read()

# NOTE: Steps for publishing
# - pip install twine wheel
# - python setup.py sdist bdist_wheel
# - twine check dist/*
# - twine upload dist/*

setup(
    name='signa',
    version=__version__,
    author="Alexey Kinëv",
    author_email='rudy@05bit.com',
    url='https://github.com/05bit/python-signa',
    description=__doc__.strip(),
    long_description=__description__,
    long_description_content_type='text/markdown',
    license='MIT License',
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
