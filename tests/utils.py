from contextlib import contextmanager


@contextmanager
def null_context():
    """
    Optional context manager to remove boilerplate code when creating unit tests
    that have cases which raise Exceptions and cases which do not.
    """
    yield
