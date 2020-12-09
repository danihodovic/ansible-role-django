def test_containers_running(host):
    assert host.docker("django")


def test_pings_django(host):
    result = host.run("curl http://localhost")
    assert "Get started with Django" in result.stdout
