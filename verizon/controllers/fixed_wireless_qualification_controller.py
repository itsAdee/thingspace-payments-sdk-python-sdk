# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from verizon.api_helper import APIHelper
from verizon.configuration import Server
from verizon.http.api_response import ApiResponse
from verizon.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from verizon.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from verizon.models.wnp_request_response import WNPRequestResponse
from verizon.exceptions.wnp_rest_error_response_exception import WNPRestErrorResponseException


class FixedWirelessQualificationController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(FixedWirelessQualificationController, self).__init__(config)

    def domestic_4_g_and_5g_fixed_wireless_qualification(self,
                                                         body):
        """Does a POST request to /m2m/intelligence/wireless-coverage.

        Use this query for Fixed Wireless Qualification of an address. Network
        types include: LTE, C-BAND and MMWAVE.

        Args:
            body (GetWirelessCoverageRequestFWA): Request for network coverage
                details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/intelligence/wireless-coverage')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(WNPRequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response', WNPRestErrorResponseException)
        ).execute()
