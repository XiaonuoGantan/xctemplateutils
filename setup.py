import os
from distutils.core import setup

dirname = os.path.dirname(__file__)

setup(
    name='xctemplateutils',
    version='0.0.2',
    author='Xiaonuo Gantan',
    author_email='xiaonuo.gantan@gmail.com',
    scripts=['bin/generate_xctemplate.py'],
    license='LICENSE.txt',
    description='Xcode Template File Helpers',
    long_description=open('README.txt').read(),
    install_requires=[],
)
