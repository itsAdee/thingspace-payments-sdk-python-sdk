# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class AddressItem(object):

    """Implementation of the 'AddressItem' model.

    Address details.

    Attributes:
        address_line_1 (str): Street Address.
        address_line_2 (str): Optional address information.
        city (str): Name of the city.
        state (str): State code.
        country (str): Country.
        zip (str): Five digit zipcode.
        zip_4 (str): Four digit zip code.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address_line_1": 'addressLine1',
        "address_line_2": 'addressLine2',
        "city": 'city',
        "state": 'state',
        "country": 'country',
        "zip": 'zip',
        "zip_4": 'zip4'
    }

    _optionals = [
        'address_line_1',
        'address_line_2',
        'city',
        'state',
        'country',
        'zip',
        'zip_4',
    ]

    def __init__(self,
                 address_line_1=APIHelper.SKIP,
                 address_line_2=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 country=APIHelper.SKIP,
                 zip=APIHelper.SKIP,
                 zip_4=APIHelper.SKIP):
        """Constructor for the AddressItem class"""

        # Initialize members of the class
        if address_line_1 is not APIHelper.SKIP:
            self.address_line_1 = address_line_1 
        if address_line_2 is not APIHelper.SKIP:
            self.address_line_2 = address_line_2 
        if city is not APIHelper.SKIP:
            self.city = city 
        if state is not APIHelper.SKIP:
            self.state = state 
        if country is not APIHelper.SKIP:
            self.country = country 
        if zip is not APIHelper.SKIP:
            self.zip = zip 
        if zip_4 is not APIHelper.SKIP:
            self.zip_4 = zip_4 

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
        address_line_1 = dictionary.get("addressLine1") if dictionary.get("addressLine1") else APIHelper.SKIP
        address_line_2 = dictionary.get("addressLine2") if dictionary.get("addressLine2") else APIHelper.SKIP
        city = dictionary.get("city") if dictionary.get("city") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        country = dictionary.get("country") if dictionary.get("country") else APIHelper.SKIP
        zip = dictionary.get("zip") if dictionary.get("zip") else APIHelper.SKIP
        zip_4 = dictionary.get("zip4") if dictionary.get("zip4") else APIHelper.SKIP
        # Return an object of this model
        return cls(address_line_1,
                   address_line_2,
                   city,
                   state,
                   country,
                   zip,
                   zip_4)
