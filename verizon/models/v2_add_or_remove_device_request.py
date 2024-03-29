# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class V2AddOrRemoveDeviceRequest(object):

    """Implementation of the 'V2AddOrRemoveDeviceRequest' model.

    Add or remove device to existing software upgrade information.

    Attributes:
        mtype (str): Operation either 'append' or 'remove'.
        device_list (List[str]): Device IMEI list.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'Type',
        "device_list": 'deviceList'
    }

    def __init__(self,
                 mtype=None,
                 device_list=None):
        """Constructor for the V2AddOrRemoveDeviceRequest class"""

        # Initialize members of the class
        self.mtype = mtype 
        self.device_list = device_list 

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
        mtype = dictionary.get("Type") if dictionary.get("Type") else None
        device_list = dictionary.get("deviceList") if dictionary.get("deviceList") else None
        # Return an object of this model
        return cls(mtype,
                   device_list)
