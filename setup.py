from setuptools import setup, find_packages

setup(
    name='django-ajax-validation',
    version='0.1.3',
    description='Provides support for doing validation using Ajax(currently with jQuery) using your existing Django forms.',
    author='Alex Gaynor',
    author_email='alex.gaynor@gmail.com',
    url='http://github.com/alex/django-ajax-validation/tree/master',
    packages=find_packages(),
    data_files=[
        ('ajax_validation/media/ajax_validation/js', ['ajax_validation/media/ajax_validation/js/jquery-ajax-validation.js']),
    ],
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
