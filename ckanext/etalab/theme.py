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


import ckan.plugins as plugins


class EtalabThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def get_helpers(self):
        # Tell CKAN what custom template helper functions this plugin provides,
        # see the ITemplateHelpers plugin interface.
        return dict(
            smart_viewers = smart_viewers,
            )

    def update_config(self, config):
        # Update CKAN's config settings, see the IConfigurer plugin interface.
        plugins.toolkit.add_public_directory(config, 'public')
        plugins.toolkit.add_template_directory(config, 'templates')


def smart_viewers(package):
    """Helper function to extract smart viewers from the related of a package."""
    return [
        related
        for related in package.related
        if related.type == 'smart_viewer'
        ]
