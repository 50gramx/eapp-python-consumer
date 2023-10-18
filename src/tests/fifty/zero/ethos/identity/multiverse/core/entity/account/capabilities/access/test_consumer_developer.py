import pytest
from ethos.elint.services.product.identity.account.access_account_pb2 import ValidateAccountRequest

from fifty.zero.ethos.identity.multiverse.core.entity.account.capabilities.access.consumer import AccessAccountConsumer


# Test Initialization
@pytest.mark.developer
def test_initialization_developer():
    assert AccessAccountConsumer is not None


# Test Discovery
@pytest.mark.developer
def test_discover_valid_account_developer():
    consumer = AccessAccountConsumer()
    request = ValidateAccountRequest(
        account_mobile_number="0987654321"
    )
    response = consumer.validate_account(request=request)
    assert response.validate_account_done is True
    assert response.validate_account_message == "OTP Sent to the Mobile Number"


@pytest.mark.developer
def test_discover_non_existent_account_developer():
    consumer = AccessAccountConsumer()
    request = ValidateAccountRequest(
        account_mobile_number="1234567890"
    )
    response = consumer.validate_account(request=request)
    assert response.validate_account_done is False
    assert response.validate_account_message == "Account doesn't exists. Please Create your Account."

# ... Add other tests following the same pattern ...
