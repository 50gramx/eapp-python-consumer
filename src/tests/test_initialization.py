# Initialization Tests
def test_package_initialization():
    """Test that the eapp_python_consumer package initializes without errors."""
    try:
        import eapp_python_consumer
        assert True
    except ImportError as e:
        assert False, f"Failed to initialize eapp_python_consumer: {e}"
