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

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=unittest.mock.PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test that the list of repos is what you expect from the chosen payload
        Args:
            mock_public_repos_url : mock version of public_repos_url
            mock_get_json: mock version of get_json method
        """
        json_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        mock_get_json.return_value = json_payload

        client = GithubOrgClient("test")

        repos = client.public_repos()

        self.assertEqual(repos, ["repo1", "repo2", "repo3"])

        mock_public_repos_url.assert_called_once()

        mock_get_json.assert_called_once_with(mock_public_repos_url.return_value)
