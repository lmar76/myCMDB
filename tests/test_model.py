"""Test the `mycmdb.model` mudule"""
from typing import Any, Dict

import pytest

from mycmdb.hosts import models


class TestOS:

    @pytest.mark.parametrize(
        "parameters",
        [
            {"id": 1, "name": "Linux", "distribution": "RedHat", "version": "8.5"},
            {"id": None, "name": "Linux", "distribution": "RedHat", "version": "8.5"},
            {"id": None, "name": "Linux", "distribution": "RedHat", "version": "8.5"},
        ]
    )
    def test_creation(self, parameters: Dict[str, Any]) -> None:
        obj = models.OS(**parameters)
        assert isinstance(obj, models.OS)
        assert isinstance(obj.hosts, list)
        assert obj.hosts == []
        assert repr(obj) == (
            f"OS(id={parameters['id']}, name={parameters['name']},"
            f" distribution={parameters['distribution']}, version={parameters['version']})"
        )


class TestHost:

    @pytest.mark.parametrize(
        "parameters",
        [
            {
                "id": 1,
                "name": "pi2",
                "alias": "pi2",
                "os_id": 1,
                "os": models.OS(id=1, name="Linux", distribution="Raspbian", version="11"),
                "processor_cores": 4,
                "ram": 1,
                "disk_size": 5
            },
            {
                "id": 1,
                "name": "a1gy05-03",
                "alias": "pi2",
                "os": models.OS(id=1, name="Linux", distribution="Raspbian", version="11"),
                "processor_cores": 4,
                "ram": 1,
                "disk_size": 5
            },
            {
                "name": "a1gy05-03",
                "alias": "pi2",
            },
        ]
    )
    def test_creation(self, parameters: Dict[str, Any]) -> None:
        obj = models.Host(**parameters)
        assert isinstance(obj, models.Host)
        assert repr(obj) == (
            f"Host(id={parameters.get('id')}, name={parameters.get('name')},"
            f" alias={parameters.get('alias')})"
        )


class TestInterface:

    @pytest.mark.parametrize(
        "parameters",
        [
            {
                "id": 1,
                "name": "eth0",
                "mac_address": "ae:65:42:f4:2c:ab",
                "ipv4_address": "192.168.0.1",
                "ipv4_mask": "255.255.255.0",
                "ipv6_address": "2001:db8::8a2e:370:7334",
                "host_id": 1,
                "host": models.Host(id=1, name="7627dgh", alias="fdy")
            }
        ]
    )
    def test_creation(self, parameters: Dict[str, Any]) -> None:
        obj = models.Interface(**parameters)
        assert isinstance(obj, models.Interface)
        assert repr(obj) == f"Interface(name={parameters.get('name')})"
