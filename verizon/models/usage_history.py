# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class UsageHistory(object):

    """Implementation of the 'usage history' model.

    TODO: type model description here.

    Attributes:
        bytes_used (int): TODO: type description here.
        serviceplan (str): TODO: type description here.
        sms_used (int): TODO: type description here.
        mo_sms (int): TODO: type description here.
        mt_sms (int): TODO: type description here.
        source (str): TODO: type description here.
        event_date_time (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bytes_used": 'bytesUsed',
        "serviceplan": 'serviceplan',
        "sms_used": 'smsUsed',
        "mo_sms": 'moSMS',
        "mt_sms": 'mtSMS',
        "source": 'source',
        "event_date_time": 'eventDateTime'
    }

    _optionals = [
        'bytes_used',
        'serviceplan',
        'sms_used',
        'mo_sms',
        'mt_sms',
        'source',
        'event_date_time',
    ]

    def __init__(self,
                 bytes_used=APIHelper.SKIP,
                 serviceplan=APIHelper.SKIP,
                 sms_used=APIHelper.SKIP,
                 mo_sms=APIHelper.SKIP,
                 mt_sms=APIHelper.SKIP,
                 source=APIHelper.SKIP,
                 event_date_time=APIHelper.SKIP):
        """Constructor for the UsageHistory class"""

        # Initialize members of the class
        if bytes_used is not APIHelper.SKIP:
            self.bytes_used = bytes_used 
        if serviceplan is not APIHelper.SKIP:
            self.serviceplan = serviceplan 
        if sms_used is not APIHelper.SKIP:
            self.sms_used = sms_used 
        if mo_sms is not APIHelper.SKIP:
            self.mo_sms = mo_sms 
        if mt_sms is not APIHelper.SKIP:
            self.mt_sms = mt_sms 
        if source is not APIHelper.SKIP:
            self.source = source 
        if event_date_time is not APIHelper.SKIP:
            self.event_date_time = APIHelper.apply_datetime_converter(event_date_time, APIHelper.RFC3339DateTime) if event_date_time else None 

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
        bytes_used = dictionary.get("bytesUsed") if dictionary.get("bytesUsed") else APIHelper.SKIP
        serviceplan = dictionary.get("serviceplan") if dictionary.get("serviceplan") else APIHelper.SKIP
        sms_used = dictionary.get("smsUsed") if dictionary.get("smsUsed") else APIHelper.SKIP
        mo_sms = dictionary.get("moSMS") if dictionary.get("moSMS") else APIHelper.SKIP
        mt_sms = dictionary.get("mtSMS") if dictionary.get("mtSMS") else APIHelper.SKIP
        source = dictionary.get("source") if dictionary.get("source") else APIHelper.SKIP
        event_date_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("eventDateTime")).datetime if dictionary.get("eventDateTime") else APIHelper.SKIP
        # Return an object of this model
        return cls(bytes_used,
                   serviceplan,
                   sms_used,
                   mo_sms,
                   mt_sms,
                   source,
                   event_date_time)
