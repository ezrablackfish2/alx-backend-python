#!/usr/bin/env python3
"""
A test for the access_nested_map method
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
)
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test for the access_nested_map method
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """ Test that the method returns what it is supposed to. """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence) -> None:
        """Test that exception raises for KeyError"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test get json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, payload: dict):
        """
        Test that the method returns as excepcted
        """
        with patch('utils.requests') as mock_requests:
            mock_response = Mock()
            mock_response.json.return_value = payload
            mock_requests.get.return_value = mock_response

            result = get_json(url)

            mock_requests.get.assert_called_once_with(url)
            self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """
    Test memoize method
    """
    def test_memoize(self):
        """
        Test the memoize method
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            mock_response = 100
            mock_method.return_value = mock_response

            tc = TestClass()
            self.assertEqual(tc.a_property, mock_response)
            self.assertEqual(tc.a_property, mock_response)

            mock_method.assert_called_once()
