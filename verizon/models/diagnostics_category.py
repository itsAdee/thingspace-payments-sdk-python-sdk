# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.custom_fields import CustomFields


class DiagnosticsCategory(object):

    """Implementation of the 'DiagnosticsCategory' model.

    Various types of information about the device, grouped into categories.
    Each category object contains the category name and a list of Extended
    Attribute objects as key-value pairs.

    Attributes:
        category_name (str): The name of the category.
        extended_attributes (List[CustomFields]): A list of Extended Attribute
            objects as key-value pairs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "category_name": 'categoryName',
        "extended_attributes": 'extendedAttributes'
    }

    _optionals = [
        'category_name',
        'extended_attributes',
    ]

    def __init__(self,
                 category_name=APIHelper.SKIP,
                 extended_attributes=APIHelper.SKIP):
        """Constructor for the DiagnosticsCategory class"""

        # Initialize members of the class
        if category_name is not APIHelper.SKIP:
            self.category_name = category_name 
        if extended_attributes is not APIHelper.SKIP:
            self.extended_attributes = extended_attributes 

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
        category_name = dictionary.get("categoryName") if dictionary.get("categoryName") else APIHelper.SKIP
        extended_attributes = None
        if dictionary.get('extendedAttributes') is not None:
            extended_attributes = [CustomFields.from_dictionary(x) for x in dictionary.get('extendedAttributes')]
        else:
            extended_attributes = APIHelper.SKIP
        # Return an object of this model
        return cls(category_name,
                   extended_attributes)
