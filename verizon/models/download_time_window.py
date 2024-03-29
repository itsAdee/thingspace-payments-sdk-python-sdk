# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class DownloadTimeWindow(object):

    """Implementation of the 'downloadTimeWindow' model.

    TODO: type model description here.

    Attributes:
        start_time (str): Device IMEI list.
        end_time (str): Device IMEI list.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_time": 'startTime',
        "end_time": 'endTime'
    }

    _optionals = [
        'start_time',
        'end_time',
    ]

    def __init__(self,
                 start_time=APIHelper.SKIP,
                 end_time=APIHelper.SKIP):
        """Constructor for the DownloadTimeWindow class"""

        # Initialize members of the class
        if start_time is not APIHelper.SKIP:
            self.start_time = start_time 
        if end_time is not APIHelper.SKIP:
            self.end_time = end_time 

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
        start_time = dictionary.get("startTime") if dictionary.get("startTime") else APIHelper.SKIP
        end_time = dictionary.get("endTime") if dictionary.get("endTime") else APIHelper.SKIP
        # Return an object of this model
        return cls(start_time,
                   end_time)
