from setuptools import setup, find_packages

setup(
    name='django-ajax-validation',
    version='0.1.4',
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
    ],
    # Make setuptools include all data files under version control,
    # svn and CVS by default
    include_package_data=True,
    # Tells setuptools to download setuptools_git before running setup.py so
    # it can find the data files under Git version control.
    setup_requires=['setuptools_git'],
    zip_safe=False,
)
