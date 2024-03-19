# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class ReadySimDeviceId(object):

    """Implementation of the 'ReadySimDeviceId' model.

    TODO: type model description here.

    Attributes:
        kind (str): TODO: type description here.
        id (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "kind": 'kind',
        "id": 'id'
    }

    _optionals = [
        'kind',
        'id',
    ]

    def __init__(self,
                 kind=APIHelper.SKIP,
                 id=APIHelper.SKIP):
        """Constructor for the ReadySimDeviceId class"""

        # Initialize members of the class
        if kind is not APIHelper.SKIP:
            self.kind = kind 
        if id is not APIHelper.SKIP:
            self.id = id 

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
        kind = dictionary.get("kind") if dictionary.get("kind") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        # Return an object of this model
        return cls(kind,
                   id)
