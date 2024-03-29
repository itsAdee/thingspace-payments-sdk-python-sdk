# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.v1_device_list_item import V1DeviceListItem


class V1LicensesAssignedRemovedResult(object):

    """Implementation of the 'V1LicensesAssignedRemovedResult' model.

    License assignment or removal confirmation.

    Attributes:
        account_name (str): Account identifier in "##########-#####".
        lic_count (int): Total number of monthly licenses in an MRC
            subscription.
        lic_used_count (int): Number of licenses assigned to devices after the
            request completed.
        device_list (List[V1DeviceListItem]): A JSON object for each device
            that was in the request.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "lic_count": 'licCount',
        "lic_used_count": 'licUsedCount',
        "device_list": 'deviceList'
    }

    _optionals = [
        'account_name',
        'lic_count',
        'lic_used_count',
        'device_list',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 lic_count=APIHelper.SKIP,
                 lic_used_count=APIHelper.SKIP,
                 device_list=APIHelper.SKIP):
        """Constructor for the V1LicensesAssignedRemovedResult class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if lic_count is not APIHelper.SKIP:
            self.lic_count = lic_count 
        if lic_used_count is not APIHelper.SKIP:
            self.lic_used_count = lic_used_count 
        if device_list is not APIHelper.SKIP:
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
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        lic_count = dictionary.get("licCount") if dictionary.get("licCount") else APIHelper.SKIP
        lic_used_count = dictionary.get("licUsedCount") if dictionary.get("licUsedCount") else APIHelper.SKIP
        device_list = None
        if dictionary.get('deviceList') is not None:
            device_list = [V1DeviceListItem.from_dictionary(x) for x in dictionary.get('deviceList')]
        else:
            device_list = APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   lic_count,
                   lic_used_count,
                   device_list)
