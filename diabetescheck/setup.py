from setuptools import setup, find_packages

name = 'diabetescheck'
version = '0.0.1'


setup(
    name=name,
    version=version,
    packages=find_packages(exclude=['tests', 'tests.*']),
    description="A self management system for pre-diabetic" +
    " and diabetic patients",
    long_description=open('README.md').read(),
    author="@fey101",
    author_email='feyitza@diabetescheck.com',
    license="MIT",
    classifiers=[
        'Development Status ::',
        'Intended Audience :: pre-diabetic and diabetic patients',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
        'django==1.9.1',
        'django-oauth-toolkit==0.10.0',
        'psycopg2==2.6.1',
        'djangorestframework==3.3.2',
        'django-cors-headers==1.1.0',
        'gunicorn==19.4.5',
        'oauthlib==1.0.3',
        'click==6.2',
        'dj-database-url==0.3.0',
        'sarge==0.1.4',
    ],
    scripts=[
        'bin/diabetescheck_manage',
        'bin/run'
    ],
    include_package_data=True
)
