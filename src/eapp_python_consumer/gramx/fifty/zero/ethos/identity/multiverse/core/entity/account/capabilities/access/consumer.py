from ethos.elint.services.product.identity.account.access_account_pb2 import ValidateAccountRequest

from fifty.zero.ethos.identity.multiverse.core.entity.account.capabilities.access.service import AccessAccountService


class AccessAccountConsumer:
    def __init__(self):
        self.service = AccessAccountService()

    def validate_account(self, request: ValidateAccountRequest):
        return self.service.validate_account(
            request=request
        )
