from ethos.elint.services.product.identity.account.access_account_pb2 import ValidateAccountRequest
from ethos.elint.services.product.identity.account.access_account_pb2_grpc import AccessAccountServiceStub

from gramx.fifty.zero.ethos.identity.multiverse.core.entity.account.capabilities.access import channel


class AccessAccountService:
    def __init__(self):
        self.channel = channel.create_developer_channel("AccessAccountService")
        self.stub = AccessAccountServiceStub(self.channel)

    def validate_account(self, request: ValidateAccountRequest):
        return self.stub.ValidateAccount(request)
