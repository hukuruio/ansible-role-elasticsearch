import os
import requests

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

user_uid = 3999
es_identifier_label = "elasticsearch"
data_directory = "/usr/share/elasticsearch/data"


def test_elasticsearch_user_exists(host):
    user = host.user(es_identifier_label)
    assert es_identifier_label in user.groups
    assert user.uid == user_uid


def test_elasticsearch_container_is_running(host):
    container = host.docker("elasticsearch1")
    assert container.is_running
    assert host.socket("tcp://0.0.0.0:9200").is_listening


def test_elasticsearch_data_directory_exists(host):
    data_dir = host.file(data_directory)
    assert data_dir.is_directory
    assert data_dir.user == es_identifier_label
    assert data_dir.group == es_identifier_label
