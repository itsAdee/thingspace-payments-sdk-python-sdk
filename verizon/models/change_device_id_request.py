# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.device_id import DeviceId


class ChangeDeviceIdRequest(object):

    """Implementation of the 'ChangeDeviceIdRequest' model.

    Changes the identifier of a 3G or 4G device to match hardware changes made
    for a line of service. Use this request to transfer the line of service
    and the MDN to new hardware, or to change the MDN.

    Attributes:
        assign_non_geo_mdn (bool): Set to true to assign a non-Geo MDN and
            MSISDN, or false to assign an MDN and MSISDN from a specific
            NPA-NXX.
        change_4_g_option (str): The type of change that you want to make for
            a 4G device.
        device_ids (List[DeviceId]): The device that you want to change,
            specified by a device identifier.
        device_ids_to (List[DeviceId]): The new identifier for the device.
            Required for all change4GOptions except ChangeMSISDN.
        npa_nxx (str): The NPA NXX (area code and prefix) from which the MDN
            and MSISDN will be derived when assignNonGeoMDN is false. Specify
            the 6-digit NPA NXX of the location where the line of service will
            primarily be used. This API checks to see if a number starting
            with the NPA NXX is available. If not, this API uses the zipCode
            parameter, if specified, to assign a number in the area of the
            line of service. This parameter is required when you change an
            MDN/MSISDN for a B2B carrier, such as Verizon Wireless.
        service_plan (str): The code for a different service plan, if you want
            to change the service plan while changing the device identifier.
            Set this parameter to one of the Code values returned by GET
            /plans.
        zip_code (str): The ZIP code from which the MDN and MSISDN will be
            derived when assignNonGeoMDN is true. Specify the zip code of the
            location where the line of service will primarily be used.
        smsr_oid (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_ids": 'deviceIds',
        "assign_non_geo_mdn": 'assignNonGeoMdn',
        "change_4_g_option": 'change4gOption',
        "device_ids_to": 'deviceIdsTo',
        "npa_nxx": 'npaNxx',
        "service_plan": 'servicePlan',
        "zip_code": 'zipCode',
        "smsr_oid": 'smsrOid'
    }

    _optionals = [
        'assign_non_geo_mdn',
        'change_4_g_option',
        'device_ids_to',
        'npa_nxx',
        'service_plan',
        'zip_code',
        'smsr_oid',
    ]

    def __init__(self,
                 device_ids=None,
                 assign_non_geo_mdn=APIHelper.SKIP,
                 change_4_g_option=APIHelper.SKIP,
                 device_ids_to=APIHelper.SKIP,
                 npa_nxx=APIHelper.SKIP,
                 service_plan=APIHelper.SKIP,
                 zip_code=APIHelper.SKIP,
                 smsr_oid=APIHelper.SKIP):
        """Constructor for the ChangeDeviceIdRequest class"""

        # Initialize members of the class
        if assign_non_geo_mdn is not APIHelper.SKIP:
            self.assign_non_geo_mdn = assign_non_geo_mdn 
        if change_4_g_option is not APIHelper.SKIP:
            self.change_4_g_option = change_4_g_option 
        self.device_ids = device_ids 
        if device_ids_to is not APIHelper.SKIP:
            self.device_ids_to = device_ids_to 
        if npa_nxx is not APIHelper.SKIP:
            self.npa_nxx = npa_nxx 
        if service_plan is not APIHelper.SKIP:
            self.service_plan = service_plan 
        if zip_code is not APIHelper.SKIP:
            self.zip_code = zip_code 
        if smsr_oid is not APIHelper.SKIP:
            self.smsr_oid = smsr_oid 

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
            device_ids = [DeviceId.from_dictionary(x) for x in dictionary.get('deviceIds')]
        assign_non_geo_mdn = dictionary.get("assignNonGeoMdn") if "assignNonGeoMdn" in dictionary.keys() else APIHelper.SKIP
        change_4_g_option = dictionary.get("change4gOption") if dictionary.get("change4gOption") else APIHelper.SKIP
        device_ids_to = None
        if dictionary.get('deviceIdsTo') is not None:
            device_ids_to = [DeviceId.from_dictionary(x) for x in dictionary.get('deviceIdsTo')]
        else:
            device_ids_to = APIHelper.SKIP
        npa_nxx = dictionary.get("npaNxx") if dictionary.get("npaNxx") else APIHelper.SKIP
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else APIHelper.SKIP
        zip_code = dictionary.get("zipCode") if dictionary.get("zipCode") else APIHelper.SKIP
        smsr_oid = dictionary.get("smsrOid") if dictionary.get("smsrOid") else APIHelper.SKIP
        # Return an object of this model
        return cls(device_ids,
                   assign_non_geo_mdn,
                   change_4_g_option,
                   device_ids_to,
                   npa_nxx,
                   service_plan,
                   zip_code,
                   smsr_oid)