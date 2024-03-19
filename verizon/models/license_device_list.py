# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.license_device_id import LicenseDeviceId


class LicenseDeviceList(object):

    """Implementation of the 'LicenseDeviceList' model.

    List of all devices.

    Attributes:
        device_ids (List[LicenseDeviceId]): For 4G devices, IMEI (decimal, up
            to 15 digits).
        ip_address (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_ids": 'deviceIds',
        "ip_address": 'ipAddress'
    }

    _optionals = [
        'device_ids',
        'ip_address',
    ]

    def __init__(self,
                 device_ids=APIHelper.SKIP,
                 ip_address=APIHelper.SKIP):
        """Constructor for the LicenseDeviceList class"""

        # Initialize members of the class
        if device_ids is not APIHelper.SKIP:
            self.device_ids = device_ids 
        if ip_address is not APIHelper.SKIP:
            self.ip_address = ip_address 

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
        device_ids = None
        if dictionary.get('deviceIds') is not None:
            device_ids = [LicenseDeviceId.from_dictionary(x) for x in dictionary.get('deviceIds')]
        else:
            device_ids = APIHelper.SKIP
        ip_address = dictionary.get("ipAddress") if dictionary.get("ipAddress") else APIHelper.SKIP
        # Return an object of this model
        return cls(device_ids,
                   ip_address)
