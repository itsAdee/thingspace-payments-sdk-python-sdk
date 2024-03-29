# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_device_list import AccountDeviceList


class DeviceGroupDevicesData(object):

    """Implementation of the 'DeviceGroupDevicesData' model.

    Returns the name, description, and list of devices in a device group.

    Attributes:
        description (str): The description of the device group.
        devices (List[AccountDeviceList]): The devices in the device group.
        has_more_data (bool): False for a status 200 response.True for a
            status 202 response, indicating that there is more data to be
            retrieved.
        name (str): The name of the device group.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "devices": 'devices',
        "has_more_data": 'hasMoreData',
        "name": 'name'
    }

    _optionals = [
        'description',
        'devices',
        'has_more_data',
        'name',
    ]

    def __init__(self,
                 description=APIHelper.SKIP,
                 devices=APIHelper.SKIP,
                 has_more_data=APIHelper.SKIP,
                 name=APIHelper.SKIP):
        """Constructor for the DeviceGroupDevicesData class"""

        # Initialize members of the class
        if description is not APIHelper.SKIP:
            self.description = description 
        if devices is not APIHelper.SKIP:
            self.devices = devices 
        if has_more_data is not APIHelper.SKIP:
            self.has_more_data = has_more_data 
        if name is not APIHelper.SKIP:
            self.name = name 

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
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        devices = None
        if dictionary.get('devices') is not None:
            devices = [AccountDeviceList.from_dictionary(x) for x in dictionary.get('devices')]
        else:
            devices = APIHelper.SKIP
        has_more_data = dictionary.get("hasMoreData") if "hasMoreData" in dictionary.keys() else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        # Return an object of this model
        return cls(description,
                   devices,
                   has_more_data,
                   name)
