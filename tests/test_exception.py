from pyflight.api import APIException


def test_exception():
    exception = APIException(404, "Unknown Endpoint", "NotFound")

    assert exception.code == 404
    assert exception.message == "Unknown Endpoint"
    assert exception.reason == "NotFound"

    assert str(exception) == "404: Unknown Endpoint (NotFound)"
