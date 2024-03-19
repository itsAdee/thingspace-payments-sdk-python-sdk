# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class UsageTriggerAddRequest(object):

    """Implementation of the 'UsageTriggerAddRequest' model.

    TODO: type model description here.

    Attributes:
        trigger_name (str): Usage trigger name
        account_name (str): Account name
        service_name (ServiceNameEnum): Service name
        threshold_value (str): The percent of subscribed usage required to
            activate the trigger, such as 90 or 100.
        allow_excess (bool): Allow additional requests after thresholdValue is
            reached. (currently not functional)
        send_sms_notification (bool): Send SMS (text) alerts when the
            thresholdValue is reached.
        sms_phone_numbers (str): Comma-separated list of phone numbers to send
            SMS alerts to. Digits only; no dashes or parentheses, etc.
        send_email_notification (bool): Send email alerts when the
            thresholdValue is reached.
        email_addresses (str): Comma-separated list of email addresses to send
            alerts to.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "service_name": 'serviceName',
        "threshold_value": 'thresholdValue',
        "trigger_name": 'triggerName',
        "allow_excess": 'allowExcess',
        "send_sms_notification": 'sendSmsNotification',
        "sms_phone_numbers": 'smsPhoneNumbers',
        "send_email_notification": 'sendEmailNotification',
        "email_addresses": 'emailAddresses'
    }

    _optionals = [
        'trigger_name',
        'allow_excess',
        'send_sms_notification',
        'sms_phone_numbers',
        'send_email_notification',
        'email_addresses',
    ]

    def __init__(self,
                 account_name=None,
                 service_name='Location',
                 threshold_value=None,
                 trigger_name=APIHelper.SKIP,
                 allow_excess=APIHelper.SKIP,
                 send_sms_notification=APIHelper.SKIP,
                 sms_phone_numbers=APIHelper.SKIP,
                 send_email_notification=APIHelper.SKIP,
                 email_addresses=APIHelper.SKIP):
        """Constructor for the UsageTriggerAddRequest class"""

        # Initialize members of the class
        if trigger_name is not APIHelper.SKIP:
            self.trigger_name = trigger_name 
        self.account_name = account_name 
        self.service_name = service_name 
        self.threshold_value = threshold_value 
        if allow_excess is not APIHelper.SKIP:
            self.allow_excess = allow_excess 
        if send_sms_notification is not APIHelper.SKIP:
            self.send_sms_notification = send_sms_notification 
        if sms_phone_numbers is not APIHelper.SKIP:
            self.sms_phone_numbers = sms_phone_numbers 
        if send_email_notification is not APIHelper.SKIP:
            self.send_email_notification = send_email_notification 
        if email_addresses is not APIHelper.SKIP:
            self.email_addresses = email_addresses 

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
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else None
        service_name = dictionary.get("serviceName") if dictionary.get("serviceName") else 'Location'
        threshold_value = dictionary.get("thresholdValue") if dictionary.get("thresholdValue") else None
        trigger_name = dictionary.get("triggerName") if dictionary.get("triggerName") else APIHelper.SKIP
        allow_excess = dictionary.get("allowExcess") if "allowExcess" in dictionary.keys() else APIHelper.SKIP
        send_sms_notification = dictionary.get("sendSmsNotification") if "sendSmsNotification" in dictionary.keys() else APIHelper.SKIP
        sms_phone_numbers = dictionary.get("smsPhoneNumbers") if dictionary.get("smsPhoneNumbers") else APIHelper.SKIP
        send_email_notification = dictionary.get("sendEmailNotification") if "sendEmailNotification" in dictionary.keys() else APIHelper.SKIP
        email_addresses = dictionary.get("emailAddresses") if dictionary.get("emailAddresses") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   service_name,
                   threshold_value,
                   trigger_name,
                   allow_excess,
                   send_sms_notification,
                   sms_phone_numbers,
                   send_email_notification,
                   email_addresses)
