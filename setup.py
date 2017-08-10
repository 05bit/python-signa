"""One lib to sign them all.
"""
import sys
from setuptools import setup, find_packages

__version__ = '0.2'

install_requires = []

if ('develop' in sys.argv) or ('test' in sys.argv):
    try:
        import dotenv
    except ImportError:
        print('python-dotenv is not installed: \n'
              'pip install python-dotenv')
        sys.exit(1)

setup(
    name="signa",
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
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
    test_loader='unittest:TestLoader',
)
