# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import warnings
from enum import Enum
from apimatic_core.http.configurations.http_client_configuration import HttpClientConfiguration
from apimatic_requests_client_adapter.requests_client import RequestsClient


class Environment(Enum):
    """An enum for SDK environments"""
    PRODUCTION = 0


class Server(Enum):
    """An enum for API servers"""
    EDGE_DISCOVERY = 0
    THINGSPACE = 1
    OAUTH_SERVER = 2
    M2M = 3
    DEVICE_LOCATION = 4
    SUBSCRIPTION_SERVER = 5
    SOFTWARE_MANAGEMENT_V1 = 6
    SOFTWARE_MANAGEMENT_V2 = 7
    SOFTWARE_MANAGEMENT_V3 = 8
    PERFORMANCE = 9
    DEVICE_DIAGNOSTICS = 10
    CLOUD_CONNECTOR = 11
    HYPER_PRECISE_LOCATION = 12
    SERVICES = 13
    QUALITY_OF_SERVICE = 14


class Configuration(HttpClientConfiguration):
    """A class used for configuring the SDK by a user.
    """

    @property
    def environment(self):
        return self._environment

    @property
    def oauth_client_id(self):
        return self._client_credentials_auth_credentials.oauth_client_id

    @property
    def oauth_client_secret(self):
        return self._client_credentials_auth_credentials.oauth_client_secret

    @property
    def oauth_scopes(self):
        return self._client_credentials_auth_credentials.oauth_scopes

    @property
    def vz_m2m_token(self):
        return self._vz_m2m_token

    @property
    def oauth_token(self):
        return self._client_credentials_auth_credentials.oauth_token

    @property
    def client_credentials_auth_credentials(self):
        return self._client_credentials_auth_credentials

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment=Environment.PRODUCTION, oauth_client_id=None,
                 oauth_client_secret=None, oauth_token=None, oauth_scopes=None,
                 client_credentials_auth_credentials=None,
                 vz_m2m_token='TODO: Replace'):
        if retry_methods is None:
            retry_methods = ['GET', 'PUT']

        if retry_statuses is None:
            retry_statuses = [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]

        super().__init__(http_client_instance, override_http_client_configuration, http_call_back, timeout, max_retries,
                         backoff_factor, retry_statuses, retry_methods)

        # Current API environment
        self._environment = environment

        # M2M Session Token ([How to generate an M2M session token?](page:getting-started/5g-edge-developer-creds-token#obtaining-a-vz-m2m-session-token-programmatically))
        self._vz_m2m_token = vz_m2m_token

        self._client_credentials_auth_credentials = self.create_auth_credentials_object(
            oauth_client_id, oauth_client_secret, oauth_token, oauth_scopes,
            client_credentials_auth_credentials)

        # The Http Client to use for making requests.
        self.set_http_client(self.create_http_client())

    def clone_with(self, http_client_instance=None,
                   override_http_client_configuration=None, http_call_back=None,
                   timeout=None, max_retries=None, backoff_factor=None,
                   retry_statuses=None, retry_methods=None, environment=None,
                   oauth_client_id=None, oauth_client_secret=None,
                   oauth_token=None, oauth_scopes=None,
                   client_credentials_auth_credentials=None, vz_m2m_token=None):
        http_client_instance = http_client_instance or self.http_client_instance
        override_http_client_configuration = override_http_client_configuration or self.override_http_client_configuration
        http_call_back = http_call_back or self.http_callback
        timeout = timeout or self.timeout
        max_retries = max_retries or self.max_retries
        backoff_factor = backoff_factor or self.backoff_factor
        retry_statuses = retry_statuses or self.retry_statuses
        retry_methods = retry_methods or self.retry_methods
        environment = environment or self.environment
        vz_m2m_token = vz_m2m_token or self.vz_m2m_token
        client_credentials_auth_credentials = self.create_auth_credentials_object(
            oauth_client_id, oauth_client_secret, oauth_token, oauth_scopes,
            client_credentials_auth_credentials or self.client_credentials_auth_credentials,
            stack_level=3)
        return Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout, max_retries=max_retries,
            backoff_factor=backoff_factor, retry_statuses=retry_statuses,
            retry_methods=retry_methods, environment=environment,
            vz_m2m_token=vz_m2m_token,
            client_credentials_auth_credentials=client_credentials_auth_credentials
        )

    def create_http_client(self):
        return RequestsClient(
            timeout=self.timeout, max_retries=self.max_retries,
            backoff_factor=self.backoff_factor, retry_statuses=self.retry_statuses,
            retry_methods=self.retry_methods,
            http_client_instance=self.http_client_instance,
            override_http_client_configuration=self.override_http_client_configuration,
            response_factory=self.http_response_factory
        )

    # All the environments the SDK can run in
    environments = {
        Environment.PRODUCTION: {
            Server.EDGE_DISCOVERY: 'https://5gedge.verizon.com/api/mec/eds',
            Server.THINGSPACE: 'https://thingspace.verizon.com/api',
            Server.OAUTH_SERVER: 'https://thingspace.verizon.com/api/ts/v1',
            Server.M2M: 'https://thingspace.verizon.com/api/m2m',
            Server.DEVICE_LOCATION: 'https://thingspace.verizon.com/api/loc/v1',
            Server.SUBSCRIPTION_SERVER: 'https://thingspace.verizon.com/api/subsc/v1',
            Server.SOFTWARE_MANAGEMENT_V1: 'https://thingspace.verizon.com/api/fota/v1',
            Server.SOFTWARE_MANAGEMENT_V2: 'https://thingspace.verizon.com/api/fota/v2',
            Server.SOFTWARE_MANAGEMENT_V3: 'https://thingspace.verizon.com/api/fota/v3',
            Server.PERFORMANCE: 'https://5gedge.verizon.com/api/mec',
            Server.DEVICE_DIAGNOSTICS: 'https://thingspace.verizon.com/api/diagnostics/v1',
            Server.CLOUD_CONNECTOR: 'https://thingspace.verizon.com/api/cc/v1',
            Server.HYPER_PRECISE_LOCATION: 'https://thingspace.verizon.com/api/hyper-precise/v1',
            Server.SERVICES: 'https://5gedge.verizon.com/api/mec/services',
            Server.QUALITY_OF_SERVICE: 'https://thingspace.verizon.com/api/m2m/v1/devices'
        }
    }

    def get_base_uri(self, server=Server.EDGE_DISCOVERY):
        """Generates the appropriate base URI for the environment and the
        server.

        Args:
            server (Configuration.Server): The server enum for which the base
            URI is required.

        Returns:
            String: The base URI.

        """
        return self.environments[self.environment][server]

    @staticmethod
    def create_auth_credentials_object(oauth_client_id, oauth_client_secret,
                                       oauth_token, oauth_scopes,
                                       client_credentials_auth_credentials,
                                       stack_level=4):
        if oauth_client_id is None \
                and oauth_client_secret is None \
                and oauth_token is None \
                and oauth_scopes is None:
            return client_credentials_auth_credentials

        warnings.warn(message=('The \'oauth_client_id\', \'oauth_client_secret'
                               '\', \'oauth_token\', \'oauth_scopes\' params ar'
                               'e deprecated. Use \'client_credentials_auth_cre'
                               'dentials\' param instead.'),
                      category=DeprecationWarning,
                      stacklevel=stack_level)

        if client_credentials_auth_credentials is not None:
            return client_credentials_auth_credentials.clone_with(
                oauth_client_id, oauth_client_secret, oauth_token, oauth_scopes)

        from verizon.http.auth.oauth_2 import ClientCredentialsAuthCredentials
        return ClientCredentialsAuthCredentials(oauth_client_id,
                                                oauth_client_secret,
                                                oauth_token, oauth_scopes)
