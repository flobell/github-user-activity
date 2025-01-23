import sys
import http.client
import json


def fetch_github_activity(username):
    try:
        conn = http.client.HTTPSConnection("api.github.com")
        headers = {"User-Agent": "github-activity-cli"}
        url = f"/users/{username}/events"

        conn.request("GET", url, headers=headers)
        response = conn.getresponse()

        if response.status != 200:
            print(f"Error: Received "
                  f"status code {response.status} from GitHub API.")
            return

        data = response.read()
        events = json.loads(data)

        if not events:
            print(f"No recent activity found for user: {username}")
            return

        for event in events[:10]:  # Limit to the 10 most recent events
            event_type = event['type']
            repo_name = event['repo']['name']

            if event_type == "PushEvent":
                commit_count = len(event['payload']['commits'])
                print(f"Pushed {commit_count} commits to {repo_name}")
            elif event_type == "IssuesEvent":
                action = event['payload']['action']
                issue_title = event['payload']['issue']['title']
                print(f"{action.capitalize()} an issue "
                      f"titled '{issue_title}' in {repo_name}")
            elif event_type == "WatchEvent":
                print(f"Starred {repo_name}")
            elif event_type == "CreateEvent":
                ref_type = event['payload']['ref_type']
                print(f"Created a new {ref_type} in {repo_name}")
            else:
                print(f"Performed {event_type} in {repo_name}")

    except Exception as e:
        print(f"Error fetching data from GitHub: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: github-activity <username>")
        sys.exit(1)

    username = sys.argv[1]
    fetch_github_activity(username)


if __name__ == "__main__":
    main()
