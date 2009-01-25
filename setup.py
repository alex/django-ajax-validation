from setuptools import setup, find_packages

setup(
    name='django-ajax-validation',
    version='0.1.1',
    description='Provides support for doing validation using Ajax(currently with jQuery) using your existing Django forms.',
    author='Alex Gaynor',
    author_email='alex.gaynor@gmail.com',
    url='http://github.com/alex/django-ajax-validation/tree/master',
    packages=find_packages(),
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
