import pytest
from ethos.elint.services.product.identity.account.access_account_pb2 import ValidateAccountRequest, \
    ValidateAccountResponse

from fifty.zero.ethos.identity.multiverse.core.entity.account.capabilities.access.consumer import AccessAccountConsumer


# Mocks for ValidateAccount RPC responses based on different scenarios


def mock_validate_account_rpc(request: ValidateAccountRequest):
    mobile_number = request.account_mobile_number

    if not mobile_number:
        return ValidateAccountResponse(
            validate_account_done=False,
            validate_account_message="Account doesn't exists. Please Create your Account."
        )

    # Define logic based on mock mobile numbers for tests
    if mobile_number == "1234567890":
        return ValidateAccountResponse(
            validate_account_done=False,
            validate_account_message="Account doesn't exists. Please Create your Account."
        )
    elif mobile_number == "0987654321":
        return ValidateAccountResponse(
            validate_account_done=True,
            validate_account_message="OTP Sent to the Mobile Number"
        )
    else:
        return ValidateAccountResponse(
            validate_account_done=False,
            validate_account_message="Account doesn't exists. Please Create your Account."
        )


# Test Initialization
@pytest.mark.mock
def test_initialization_mock():
    assert AccessAccountConsumer is not None


# Test Discovery
@pytest.mark.mock
def test_discover_valid_account_mock(monkeypatch):
    mock_validate_account_attr = "fifty.zero.ethos.identity.multiverse.core.entity." \
                                 "account.capabilities.access.consumer." \
                                 "AccessAccountService.validate_account"
    monkeypatch.setattr(mock_validate_account_attr, mock_validate_account_rpc)

    request = ValidateAccountRequest(
        account_mobile_number="0987654321"
    )
    response = AccessAccountConsumer.validate_account(request)
    assert response.validate_account_done == True
    assert response.validate_account_message == "OTP Sent to the Mobile Number"


@pytest.mark.mock
def test_discover_non_existent_account_mock(monkeypatch):
    mock_validate_account_attr = "fifty.zero.ethos.identity.multiverse.core.entity." \
                                 "account.capabilities.access.consumer." \
                                 "AccessAccountService.validate_account"
    monkeypatch.setattr(mock_validate_account_attr, mock_validate_account_rpc)

    request = ValidateAccountRequest(
        account_mobile_number="1234567890"
    )
    response = AccessAccountConsumer.validate_account(request)
    assert response.validate_account_done == False
    assert response.validate_account_message == "Account doesn't exists. Please Create your Account."

# ... Add other tests following the same pattern ...
