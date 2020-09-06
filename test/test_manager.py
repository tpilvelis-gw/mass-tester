import pytest
from manager import main


def test_main():
    event = {}
    context = {}

    main(event, context)


