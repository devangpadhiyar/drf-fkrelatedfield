import os
import setuptools
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setuptools.setup(
    name='drf-fkrelatedfield',
    version='0.1',
    # packages=['myapp'],
    description='DRF fk related field to solve foreign key related problems',
    long_description=README,
    author='Devang Padhiyar',
    author_email='devangpadhiyar700@gmail.com',
    url='https://github.com/yourname/django-myapp/',
    license='MIT',
    install_requires=[
        'Django>=1.11',
        'djangorestframework>=3.8.0',
    ]
)