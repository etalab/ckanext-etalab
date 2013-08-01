#! /usr/bin/env python
# -*- coding: utf-8 -*-


# CKANExt-Etalab -- CKAN extension for Etalab
# By: Emmanuel Raviart <emmanuel@raviart.com>
#
# Copyright (C) 2013 Emmanuel Raviart
# http://gitorious.org/etalab/ckanext-etalab
#
# This file is part of CKANExt-Etalab.
#
# CKANExt-Etalab is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# CKANExt-Etalab is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


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
        etalab_theme = ckanext.etalab.plugin:EtalabPlugin
        """,
    )
