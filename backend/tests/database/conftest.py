import os

import pytest

from database.database import Database


@pytest.fixture
def db():
    Database.namespace = os.environ["DATASTORE_NAMESPACE"]
    Database.clear()
