__author__ = "730654182"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_all_even() -> None:
    """Test only_evens with all even numbers."""
    assert only_evens([2, 4, 6]) == [2, 4, 6]


def test_only_evens_mixed() -> None:
    """Test only_evens with mixed even and odd numbers."""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_only_evens_all_odd() -> None:
    """Test only_evens with all odd numbers."""
    assert only_evens([1, 3, 5]) == []


def test_sub_within_bounds() -> None:
    """Test sub with valid start and end indices."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_start_negative() -> None:
    """Test sub with negative start index."""
    assert sub([10, 20, 30, 40], -1, 3) == [10, 20, 30]


def test_sub_empty() -> None:
    """Test sub with empty list."""
    assert sub([], 1, 3) == []


def test_add_at_index_middle() -> None:
    """Test add_at_index with a valid middle index."""
    a = [1, 2, 4]
    add_at_index(a, 3, 2)
    assert a == [1, 2, 3, 4]


def test_add_at_index_end() -> None:
    """Test add_at_index at the end of the list."""
    a = [1, 2, 3]
    add_at_index(a, 4, 3)
    assert a == [1, 2, 3, 4]


def test_add_at_index_raises() -> None:
    """Test that add_at_index raises IndexError for invalid index."""
    a = [1, 2]
    with pytest.raises(IndexError):
        add_at_index(a, 3, 5)
