#!/usr/bin/env python3
"""
Module to test the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test the GithubOrgClient class methods
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_org):
        """
        Test TestGithubOrgClient's org method
        Args:
            org (str): organisation's name
        """
        org_test = GithubOrgClient(org)
        test_response = org_test.org
        self.assertEqual(test_response, mock_org.return_value)
        mock_org.assert_called_once()

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """ Tests repos_url and compares them to mock_org """
        org_payload = {"repos_url": "https://api.github.com/orgs/test/repos"}

        mock_org.return_value = org_payload

        client = GithubOrgClient("test")

        public_repos_url = client._public_repos_url

        self.assertEqual(public_repos_url, org_payload["repos_url"])

