#!/usr/bin/env python3
"""Module to test the GithubOrgClient class."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org method"""
        test_data = {'name': 'test_org'}
        mock_get_json.return_value = test_data

        client = GithubOrgClient(org_name)
        org_info = client.org()

        self.assertEqual(org_info, test_data)

        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
        )


if __name__ == '__main__':
    unittest.main()
