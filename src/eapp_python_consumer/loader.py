import os

import grpc

# ------------------------------------
# IDENTITY STUBS
# ------------------------------------
grpc_host = os.environ['EAPP_SERVICE_IDENTITY_HOST']
grpc_port = os.environ['EAPP_SERVICE_IDENTITY_PORT']
grpc_certificate_file = os.environ['EAPP_SERVICE_IDENTITY_COMMON_GRPC_EXTERNAL_CERTIFICATE_FILE']

host_ip = "{host}:{port}".format(host=grpc_host, port=grpc_port)

ssl_credentials = grpc.ssl_channel_credentials(open(grpc_certificate_file, 'rb').read())
identity_common_channel = grpc.secure_channel(host_ip, ssl_credentials)

# which channel?
# context channels for each entity
# for ex, fifty_zero_ethos_identity
# followed by, multiverse_core_entity_epme_1005
# followed by, capability_discover_channel

# in one line as
# fifty_zero_ethos_identity_multiverse_core_entity_epme_1005_capability_discover_channel

identity_common_channel = grpc.intercept_channel(identity_common_channel)
channels.append(identity_common_channel)

access_account_service_stub = AccessAccountServiceStub(identity_common_channel)
Registry.register_service('access_account_service_stub', access_account_service_stub)
