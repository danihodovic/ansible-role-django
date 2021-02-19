# pylint: disable=redefined-outer-name,invalid-name
import time

import pytest
from testinfra.host import Host


@pytest.fixture(scope="session")
def target_host(request):
    def fn(host, sudo=True):
        return Host.get_host(
            f"ansible://{host}?ansible_inventory={request.config.option.ansible_inventory}",
            sudo=sudo,
        )

    return fn


def test_django_running(target_host):
    host = target_host("web")
    assert host.docker("django").is_running


def test_pings_django(target_host):
    host = target_host("web")
    result = host.run("curl http://localhost")
    assert "404" in result.stdout


def test_celery_worker_running(target_host):
    host = target_host("worker")
    assert host.docker("celery-worker").is_running


def test_celery_completes_task(target_host):
    web_facts = target_host("web").ansible("setup")["ansible_facts"]
    web_ip = web_facts["ansible_default_ipv4"]["address"]
    worker = target_host("worker")
    worker.ansible("uri", f"url=http://{web_ip}/task", check=False)
    time.sleep(5)
    output = worker.check_output(
        f"echo 'keys *' | docker run -i redis redis-cli -h {web_ip}"
    )
    assert "celery-task-meta-" in output
