#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This file is part of cpe package.

This module allows to create a component of CPE name that represents any value.

Copyright (C) 2013  Alejandro Galindo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

For any problems using the cpe package, or general questions and
feedback about it, please contact: galindo.garcia.alejandro@gmail.com.
'''

from cpecomp_logical import CPEComponentLogical


class CPEComponentAnyValue(CPEComponentLogical):
    """
    Represents a component of CPE name without a particular value,
    compatible with the components of all versions of CPE specification.

    For example, in version 2.3 of CPE specification, an component "any value"
    is other attribute in CPE name
    cpe:2.3:a:microsft:windows:xp:*:*:*:*:*:*:*.
    """

    ####################
    #  OBJECT METHODS  #
    ####################

    def __contains__(self, item):
        """
        Returns True if item is included in set of values of self.

        INPUT:
            - item: component to find in self
        OUTPUT:
            - True if item is included in set of self
        """

        return super(CPEComponentAnyValue, self).__contains__(item)

    def __eq__(self, other):
        """
        Returns True if other (first element of operation) and
        self (second element of operation) are equal components,
        false otherwise.

        INPUT:
            - other: component to compare
        OUTPUT:
            True if other == self, False otherwise
        """

        from cpecomp_empty import CPEComponentEmpty
        from cpecomp_undefined import CPEComponentUndefined

        return (isinstance(other, CPEComponentUndefined) or
                isinstance(other, CPEComponentEmpty) or
                isinstance(other, CPEComponentAnyValue))

    def __init__(self):
        """
        Initializes the component.

        INPUT:
            - None
        OUPUT:
            - None
        """

        super(CPEComponentAnyValue, self).__init__(
            CPEComponentLogical._VALUE_INT_ANY)

    def __repr__(self):
        """
        Returns a unambiguous representation of CPE component.

        INPUT:
            - None
        OUTPUT:
            - Representation of CPE component as string
        """

        return "CPEComponentAnyValue()"

    def __str__(self):
        """
        Returns a human-readable representation of CPE component.

        INPUT:
            - None
        OUTPUT:
            - Representation of CPE component as string
        """

        return "<ANY>"
