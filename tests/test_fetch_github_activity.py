import unittest
import json
from unittest.mock import patch, MagicMock
from main import fetch_github_activity


class TestFetchGitHubActivity(unittest.TestCase):
    @patch("http.client.HTTPSConnection")
    def test_fetch_github_activity_success(self, mock_https_connection):
        # Mock response data
        mock_response_data = json.dumps([
            {
                "type": "PushEvent",
                "repo": {"name": "example/repo"},
                "payload": {
                    "commits": [{"message": "Initial commit"}]
                }
            },
            {
                "type": "IssuesEvent",
                "repo": {"name": "example/repo"},
                "payload": {
                    "action": "opened",
                    "issue": {"title": "Example issue"}
                }
            },
            {
                "type": "WatchEvent",
                "repo": {"name": "example/repo"}
            }
        ]).encode("utf-8")

        # Mock the HTTPSConnection object and its methods
        mock_conn = MagicMock()
        mock_https_connection.return_value = mock_conn
        mock_conn.getresponse.return_value.status = 200
        mock_conn.getresponse.return_value.read.return_value = \
            mock_response_data

        # Patch `sys.stdout` to capture print outputs
        with patch("sys.stdout.write") as mock_stdout_write:
            fetch_github_activity("example_user")

        # Combine output into complete lines
        actual_output = "".join(
            call.args[0] for call in mock_stdout_write.call_args_list
        ).splitlines()

        # Define expected output
        expected_output = [
            "Pushed 1 commits to example/repo",
            "Opened an issue titled 'Example issue' in example/repo",
            "Starred example/repo"
        ]

        # Assert that each expected line is in the actual output
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
