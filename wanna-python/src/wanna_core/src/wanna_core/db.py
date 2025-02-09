import logging
from contextlib import contextmanager
from typing import NamedTuple

from neo4j import GraphDatabase

LOG = logging.getLogger(__name__)


class DBAuth(NamedTuple):
    username: str
    password: str


class Neo4JDatabase:
    def __init__(self, uri: str, auth: DBAuth):
        self._uri = uri
        self._auth = auth

    def create_user(self, username: str, password: str):
        with self.transaction() as tx:
            query = "CREATE (p:User {username: $username, password: $password})"
            params = {"username": username, "password": password}
            tx.run(query, params)

    @contextmanager
    def transaction(self):
        try:
            # Create our driver, session, and a transaction
            driver = GraphDatabase.driver(self._uri, auth=self._auth)
            session = driver.session()
            tx = session.begin_transaction()
            yield tx

        except Exception as e:
            # If our transaction fails, log a warning and rollback the transaction
            LOG.warning("Transaction failed")
            tx.rollback()

        finally:
            # Commit our transactional changes
            tx.commit()

            # Cleanup our driver, session, and transaction
            session.close()
            driver.close()
            tx.close()
