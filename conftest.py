
def pytest_addoption(parser):
    parser.addoption(
        "--devices",
        action="store",
        default="iPhone 15",
        help="comma separated list of devices to search on Amazon"
    )


def pytest_generate_tests(metafunc):
    if "device_name" in metafunc.fixturenames:
        raw = metafunc.config.getoption("devices")
        device_list = [d.strip() for d in raw.split(",")]
        metafunc.parametrize("device_name", device_list)