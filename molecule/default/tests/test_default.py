import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_hosts_all(host):
    # Check if Peering Manager is in the right directory
    peering_manager_install_directory = host.file("/opt/peering-manager/")

    assert peering_manager_install_directory.exists
    assert peering_manager_install_directory.user == "peering-manager"
    assert peering_manager_install_directory.group == "peering-manager"
