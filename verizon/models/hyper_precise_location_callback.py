# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class HyperPreciseLocationCallback(object):

    """Implementation of the 'HyperPreciseLocationCallback' model.

    Callback registration request.

    Attributes:
        name (str): The name of the callback service that you want to
            subscribe to.
        url (str): The address on your server where you have enabled a
            listening service for the specific type of callback messages.
            Specify a URL that is reachable from the Verizon data centers. If
            your service is running on HTTPS, you should use a one-way
            authentication certificate with a white-listed IP address.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "url": 'url'
    }

    def __init__(self,
                 name=None,
                 url=None):
        """Constructor for the HyperPreciseLocationCallback class"""

        # Initialize members of the class
        self.name = name 
        self.url = url 

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
        name = dictionary.get("name") if dictionary.get("name") else None
        url = dictionary.get("url") if dictionary.get("url") else None
        # Return an object of this model
        return cls(name,
                   url)
