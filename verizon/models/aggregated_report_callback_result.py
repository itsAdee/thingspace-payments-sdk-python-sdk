# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class AggregatedReportCallbackResult(object):

    """Implementation of the 'AggregatedReportCallbackResult' model.

    Aggregated usage report (Asynchronous).

    Attributes:
        txid (str): A unique string that associates the request with the
            location report information that is sent in asynchronous callback
            message.ThingSpace will send a separate callback message for each
            device that was in the request. All of the callback messages will
            have the same txid.
        status (AggregatedReportCallbackStatusEnum): QUEUED or COMPLETED.
            Requests for IoT devices with cacheMode=0 (cached) have
            status=COMPLETED; all other requests are QUEUED.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "txid": 'txid',
        "status": 'status'
    }

    _optionals = [
        'status',
    ]

    def __init__(self,
                 txid=None,
                 status=APIHelper.SKIP):
        """Constructor for the AggregatedReportCallbackResult class"""

        # Initialize members of the class
        self.txid = txid 
        if status is not APIHelper.SKIP:
            self.status = status 

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
        txid = dictionary.get("txid") if dictionary.get("txid") else None
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        # Return an object of this model
        return cls(txid,
                   status)