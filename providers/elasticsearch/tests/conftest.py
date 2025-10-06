# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

import pytest
from filelock import FileLock
from testcontainers.elasticsearch import ElasticSearchContainer

LOCK_PATH = "/tmp/airflow_es_testcontainers.lock"


@pytest.fixture(scope="session")
def es_8_container_url():
    with FileLock(LOCK_PATH, timeout=1200):
        with ElasticSearchContainer("docker.elastic.co/elasticsearch/elasticsearch:8.19.0") as es:
            yield es.get_url()


pytest_plugins = "tests_common.pytest_plugin"
