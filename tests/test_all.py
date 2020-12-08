def test_containers_running(host):
    assert host.docker("django")


def test_pings_django(host):
    result = host.run("curl localhost:8000")
    assert "Get started with Django" in result.stdout
