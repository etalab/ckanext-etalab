from setuptools import setup, find_packages
import sys, os

version = ''

setup(
    name = 'ckanext-etalab',
    version = version,
    description = "CKAN extension for data.gouv.fr site",
    long_description = """\
    """,
    classifiers = [], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords = '',
    author = 'Emmanuel Raviart',
    author_email = 'emmanuel@raviart.com',
    url = '',
    license = 'AGPL',
    packages = find_packages(exclude = ['ez_setup', 'examples', 'tests']),
    namespace_packages = ['ckanext', 'ckanext.etalab'],
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        # -*- Extra requirements: -*-
    ],
    entry_points = """
        [ckan.plugins]
        etalab_theme = ckanext.etalab.theme:EtalabThemePlugin
        """,
    )
