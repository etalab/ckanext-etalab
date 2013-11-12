# -*- coding: utf-8 -*-


# CKANExt-Etalab -- CKAN extension for Etalab
# By: Emmanuel Raviart <emmanuel@raviart.com>
#
# Copyright (C) 2013 Etalab
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


import math


def compute_territorial_granularity_weight(pkg_dict):
    territorial_coverage_granularity = pkg_dict.get('territorial_coverage_granularity')
    if territorial_coverage_granularity:
        territorial_coverage_granularity = {
            'poi': 'CommuneOfFrance',
            'iris': 'CommuneOfFrance',
            'commune': 'CommuneOfFrance',
            'canton': 'CantonOfFrance',
            'epci': 'IntercommunalityOfFrance',
            'department': 'DepartmentOfFrance',
            'region': 'RegionOfFrance',
            'pays': 'Country',
            }.get(territorial_coverage_granularity, territorial_coverage_granularity)
        territorial_granularity_weight = dict(
            ArrondissementOfCommuneOfFrance = 36700.0,
            ArrondissementOfFrance = 342.0,
            AssociatedCommuneOfFrance = 36700.0,
            CantonalFractionOfCommuneOfFrance = 36700.0,
            CantonCityOfFrance = 3785.0,
            CantonOfFrance = 4055.0,
            CatchmentAreaOfFrance = 1666.0,
            CommuneOfFrance = 36700.0,
            Country = 1.0,
            DepartmentOfFrance = 101.0,
            EmploymentAreaOfFrance = 322.0,
            IntercommunalityOfFrance = 2582.0,
            InternationalOrganization = 1.0,
            JusticeAreaOfFrance = 316.0,  # TODO: Justice areas have not the same size.
            MetropoleOfCountry = 27.0,
            Mountain = (36700.0 * 7.0) / 8857.0,
            OverseasCollectivityOfFrance = 109.0,
            OverseasOfCountry = 27.0 / 5.0,
            PaysOfFrance = (36700.0 * 358.0) / 28849.0,
            RegionalNatureParkOfFrance = (36700.0 * 47.0) / 4126.0,
            RegionOfFrance = 27.0,
            UrbanAreaOfFrance = 796.0,
            UrbanTransportsPerimeterOfFrance = (36700.0 * 297.0) / 4077.0,
            UrbanUnitOfFrance = 2390.0,
            ).get(territorial_coverage_granularity, 0.0)
    else:
        territorial_granularity_weight = 0.0
    # Ensure that territorial_granularity is beween 0.5 and 2.0.
    territorial_granularity_weight *= 1.5 / 36700.0
    territorial_granularity_weight += 0.5
    return territorial_granularity_weight


def compute_territorial_weight(pkg_dict, *local_kinds):
    territorial_coverage = pkg_dict.get('territorial_coverage')
    if territorial_coverage:
        # When local_kinds is empty, compute a territorial_weight between 0 and 1, except when kind belongs to
        # local_kinds where it equals 2.
        # When local_kinds is not empty, compute a territorial_weight between 0 and 2.
        territorial_weight = 0
        for covered_kind in (
                covered_territory.split('/', 1)[0]
                for covered_territory in territorial_coverage.split(',')
                if covered_territory
                ):
            if covered_kind in local_kinds:
                return 2.0
            territorial_weight += dict(
                ArrondissementOfCommuneOfFrance = 1.0 / 36700.0,
                ArrondissementOfFrance = 1.0 / 342.0,
                AssociatedCommuneOfFrance = 1.0 / 36700.0,
                CantonalFractionOfCommuneOfFrance = 1.0 / 36700.0,
                CantonCityOfFrance = 1.0 / 3785.0,
                CantonOfFrance = 1.0 / 4055.0,
                CatchmentAreaOfFrance = 1.0 / 1666.0,
                CommuneOfFrance = 1.0 / 36700.0,
                Country = 1.0,
                DepartmentOfFrance = 1.0 / 101.0,
                EmploymentAreaOfFrance = 1.0 / 322.0,
                IntercommunalityOfFrance = 1.0 / 2582.0,
                InternationalOrganization = 1.0,
                JusticeAreaOfFrance = 1.0 / 316.0,  # TODO: Justice areas have not the same size.
                MetropoleOfCountry = 22.0 / 27.0,
                Mountain = 8857.0 / (36700.0 * 7.0),
                OverseasCollectivityOfFrance = 1.0 / 109.0,
                OverseasOfCountry = 5.0 / 27.0,
                PaysOfFrance = 28849.0 / (36700.0 * 358.0),
                RegionalNatureParkOfFrance = 4126.0 / (36700.0 * 47.0),
                RegionOfFrance = 1.0 / 27.0,
                UrbanAreaOfFrance = 1.0 / 796.0,
                UrbanTransportsPerimeterOfFrance = 4077.0 / (36700.0 * 297.0),
                UrbanUnitOfFrance = 1.0 / 2390.0,
                ).get(covered_kind, 1.0 / 40000.0)
            if territorial_weight >= 1.0:
                territorial_weight = 1.0
                break
    else:
        # When no territorial coverage is given, consider that it is less than a commune.
        territorial_weight = 1.0 / 40000.0
    # Note: territorial_weight is between 0 and 1.
    if local_kinds:
        # Ensure that territorial_weight is between 0.5 and 1.
        territorial_weight /= 2.0
        territorial_weight += 0.5
    else:
        # Ensure that territorial_weight is between 0.5 and 2.
        territorial_weight *= 1.5
        territorial_weight += 0.5
    return territorial_weight


def normalize_bonus_weight(weight):
    # Convert a weight between 0 and infinite to a number between 1 and 2.
    # cf http://en.wikipedia.org/wiki/Inverse_trigonometric_functions
    return math.atan(weight) * 2 / math.pi + 1.0


def normalize_weight(weight):
    # Convert a weight between 0 and infinite to a number between 0.5 and 2.
    # cf http://en.wikipedia.org/wiki/Inverse_trigonometric_functions
    return math.atan(weight) * 3 / math.pi + 0.5
