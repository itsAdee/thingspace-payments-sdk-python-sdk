# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class TargetAuthenticationBodyHost(object):

    """Implementation of the 'TargetAuthenticationBodyHost' model.

    Host information.

    Attributes:
        hostandpath (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hostandpath": 'hostandpath'
    }

    _optionals = [
        'hostandpath',
    ]

    def __init__(self,
                 hostandpath=APIHelper.SKIP):
        """Constructor for the TargetAuthenticationBodyHost class"""

        # Initialize members of the class
        if hostandpath is not APIHelper.SKIP:
            self.hostandpath = hostandpath 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        hostandpath = dictionary.get("hostandpath") if dictionary.get("hostandpath") else APIHelper.SKIP
        # Return an object of this model
        return cls(hostandpath)
