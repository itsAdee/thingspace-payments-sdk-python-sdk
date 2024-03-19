# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.esim_device_id import ESIMDeviceId


class DeviceList2(object):

    """Implementation of the 'DeviceList2' model.

    TODO: type model description here.

    Attributes:
        ids (List[ESIMDeviceId]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ids": 'ids'
    }

    _optionals = [
        'ids',
    ]

    def __init__(self,
                 ids=APIHelper.SKIP):
        """Constructor for the DeviceList2 class"""

        # Initialize members of the class
        if ids is not APIHelper.SKIP:
            self.ids = ids 

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
        ids = None
        if dictionary.get('ids') is not None:
            ids = [ESIMDeviceId.from_dictionary(x) for x in dictionary.get('ids')]
        else:
            ids = APIHelper.SKIP
        # Return an object of this model
        return cls(ids)
