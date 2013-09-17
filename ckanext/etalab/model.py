# -*- coding: utf-8 -*-


# CKANExt-Etalab -- CKAN extension for Etalab
# By: Emmanuel Raviart <emmanuel@raviart.com>
#
# Copyright (C) 2013 Emmanuel Raviart
# http://github.com/etalab/ckanext-etalab
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


import logging

from ckan import model
from ckan.model import meta
from ckan.model.types import make_uuid
import sqlalchemy as sa
from sqlalchemy import orm, types


certified_public_service_table = None
log = logging.getLogger(__name__)


class CertifiedPublicService(object):
    pass


def define_tables():
    global certified_public_service_table
    certified_public_service_table = sa.Table('certified_public_service', meta.metadata,
        sa.Column('organization_id', types.UnicodeText, sa.ForeignKey('group.id'), primary_key = True),
        )

    meta.mapper(
        CertifiedPublicService,
        certified_public_service_table,
        properties = dict(
            organization = orm.relation(
                model.Group,  # Organization only
                backref = orm.backref(u'certified_public_service', uselist = False),
                lazy = True,
                ),
            ),
        )


def setup():
    if certified_public_service_table is None:
        define_tables()

    if model.package_table.exists():
        if not certified_public_service_table.exists():
            certified_public_service_table.create()
            log.debug(u'Etalab tables created')
