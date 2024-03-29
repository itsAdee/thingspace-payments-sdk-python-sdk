# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class GetTriggerResponse(object):

    """Implementation of the 'GetTriggerResponse' model.

    TODO: type model description here.

    Attributes:
        account_name (str): TODO: type description here.
        comparator (str): TODO: type description here.
        created_at (datetime): TODO: type description here.
        group_name (str): TODO: type description here.
        modified_at (datetime): TODO: type description here.
        notification_group_name (str): TODO: type description here.
        organization_name (str): TODO: type description here.
        sms_type (str): TODO: type description here.
        threshold (str): TODO: type description here.
        threshold_unit (str): TODO: type description here.
        trigger_category (str): TODO: type description here.
        trigger_cycle (str): TODO: type description here.
        trigger_id (str): TODO: type description here.
        trigger_name (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "comparator": 'comparator',
        "created_at": 'createdAt',
        "group_name": 'groupName',
        "modified_at": 'modifiedAt',
        "notification_group_name": 'notificationGroupName',
        "organization_name": 'organizationName',
        "sms_type": 'smsType',
        "threshold": 'threshold',
        "threshold_unit": 'thresholdUnit',
        "trigger_category": 'triggerCategory',
        "trigger_cycle": 'triggerCycle',
        "trigger_id": 'triggerId',
        "trigger_name": 'triggerName'
    }

    _optionals = [
        'account_name',
        'comparator',
        'created_at',
        'group_name',
        'modified_at',
        'notification_group_name',
        'organization_name',
        'sms_type',
        'threshold',
        'threshold_unit',
        'trigger_category',
        'trigger_cycle',
        'trigger_id',
        'trigger_name',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 comparator=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 group_name=APIHelper.SKIP,
                 modified_at=APIHelper.SKIP,
                 notification_group_name=APIHelper.SKIP,
                 organization_name=APIHelper.SKIP,
                 sms_type=APIHelper.SKIP,
                 threshold=APIHelper.SKIP,
                 threshold_unit=APIHelper.SKIP,
                 trigger_category=APIHelper.SKIP,
                 trigger_cycle=APIHelper.SKIP,
                 trigger_id=APIHelper.SKIP,
                 trigger_name=APIHelper.SKIP):
        """Constructor for the GetTriggerResponse class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if comparator is not APIHelper.SKIP:
            self.comparator = comparator 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if group_name is not APIHelper.SKIP:
            self.group_name = group_name 
        if modified_at is not APIHelper.SKIP:
            self.modified_at = APIHelper.apply_datetime_converter(modified_at, APIHelper.RFC3339DateTime) if modified_at else None 
        if notification_group_name is not APIHelper.SKIP:
            self.notification_group_name = notification_group_name 
        if organization_name is not APIHelper.SKIP:
            self.organization_name = organization_name 
        if sms_type is not APIHelper.SKIP:
            self.sms_type = sms_type 
        if threshold is not APIHelper.SKIP:
            self.threshold = threshold 
        if threshold_unit is not APIHelper.SKIP:
            self.threshold_unit = threshold_unit 
        if trigger_category is not APIHelper.SKIP:
            self.trigger_category = trigger_category 
        if trigger_cycle is not APIHelper.SKIP:
            self.trigger_cycle = trigger_cycle 
        if trigger_id is not APIHelper.SKIP:
            self.trigger_id = trigger_id 
        if trigger_name is not APIHelper.SKIP:
            self.trigger_name = trigger_name 

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
        comparator = dictionary.get("comparator") if dictionary.get("comparator") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("createdAt")).datetime if dictionary.get("createdAt") else APIHelper.SKIP
        group_name = dictionary.get("groupName") if dictionary.get("groupName") else APIHelper.SKIP
        modified_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("modifiedAt")).datetime if dictionary.get("modifiedAt") else APIHelper.SKIP
        notification_group_name = dictionary.get("notificationGroupName") if dictionary.get("notificationGroupName") else APIHelper.SKIP
        organization_name = dictionary.get("organizationName") if dictionary.get("organizationName") else APIHelper.SKIP
        sms_type = dictionary.get("smsType") if dictionary.get("smsType") else APIHelper.SKIP
        threshold = dictionary.get("threshold") if dictionary.get("threshold") else APIHelper.SKIP
        threshold_unit = dictionary.get("thresholdUnit") if dictionary.get("thresholdUnit") else APIHelper.SKIP
        trigger_category = dictionary.get("triggerCategory") if dictionary.get("triggerCategory") else APIHelper.SKIP
        trigger_cycle = dictionary.get("triggerCycle") if dictionary.get("triggerCycle") else APIHelper.SKIP
        trigger_id = dictionary.get("triggerId") if dictionary.get("triggerId") else APIHelper.SKIP
        trigger_name = dictionary.get("triggerName") if dictionary.get("triggerName") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   comparator,
                   created_at,
                   group_name,
                   modified_at,
                   notification_group_name,
                   organization_name,
                   sms_type,
                   threshold,
                   threshold_unit,
                   trigger_category,
                   trigger_cycle,
                   trigger_id,
                   trigger_name)
