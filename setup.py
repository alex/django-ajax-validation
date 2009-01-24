from setuptools import setup, find_packages

setup(
    name='django-ajax-validation',
    version='.5a',
    description='Provides support for doing validation using Ajax(currently with jQuery) using your existing Django forms.',
    long_description=open('docs/index.txt').read(),
    author='Alex Gaynor',
    author_email='alex.gaynor@gmail.com',
    url='http://github.com/alex/django-ajax-validation/tree/master',
    packages=find_pacakges(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
