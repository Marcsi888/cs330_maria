import requests
import unittest
from unittest import TestCase, mock

pylint = "pip install pylint"
pycodestyle = "pip install pycodestyle"

class TestGitHubAPIMocking(TestCase):
    
    @mock.patch('my_github_module.requests.get')
    def test_mocked_api_response(self, mock_get):
        # Mock the API response
        mock_response = mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'full_name': 'octocat/Hello-World',
            'stargazers_count': 1710,
            'forks_count': 1425
        }
        mock_get.return_value = mock_response
        
        result = get_repo_info('octocat', 'Hello-World')
        self.assertEqual(result['full_name'], 'octocat/Hello-World')
        self.assertEqual(result['stargazers_count'], 1710)

if __name__ == '__main__':
    unittest.main()


API_URL = "https://api.github.com/repos"
Bearer_token = "h" 
def get_repo_info(owner, repo_name):
    url = f"{API_URL}/{owner}/{repo_name}" 
    
    try:
        response = requests.get(url)    # Send a GET request to the URL
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json() # Parse the JSON data
        
        print(f"\nRepository Information for '{repo_name}' by '{owner}':")
        print(f"  - Name: {data['name']}")
        print(f"  - Full Name: {data['full_name']}")
        print(f"  - Description: {data['description']}")
        print(f"  - Stars: {data['stargazers_count']}")
        print(f"  - Forks: {data['forks_count']}")
        print(f"  - Open Issues: {data['open_issues_count']}")
        print(f"  - Created at: {data['created_at']}")
        print(f"  - Updated at: {data['updated_at']}")
        print(f"  - Clone URL: {data['clone_url']}")
        print(f"  - Default Branch: {data['default_branch']}")
        print(f"  - Language: {data['language']}")
        
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Error: The repository '{owner}/{repo_name}' was not found.") # Repository not found
        else:
            print(f"HTTP error occurred: {http_err}")   # Other HTTP errors
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    print("GitHub Repository Info Fetcher")
    owner = input("Enter the GitHub owner (username or organization): ")    # Get the owner name
    repo_name = input("Enter the repository name: ")    
    get_repo_info(owner, repo_name) # Call the function to get the repository information
"""cs330_04_3.py:10:0: C0303: Trailing whitespace (trailing-whitespace)
cs330_04_3.py:22:0: C0303: Trailing whitespace (trailing-whitespace)
cs330_04_3.py:32:18: C0303: Trailing whitespace (trailing-whitespace)
cs330_04_3.py:34:42: C0303: Trailing whitespace (trailing-whitespace)
cs330_04_3.py:35:0: C0303: Trailing whitespace (trailing-whitespace)
cs330_04_3.py:40:0: C0303: Trailing whitespace (trailing-whitespace)
cs330_04_3.py:53:0: C0303: Trailing whitespace (trailing-whitespace)
cs330_04_3.py:56:0: C0301: Line too long (103/100) (line-too-long)
cs330_04_3.py:65:52: C0303: Trailing whitespace (trailing-whitespace)
cs330_04_3.py:1:0: C0114: Missing module docstring (missing-module-docstring)
cs330_04_3.py:3:0: C0103: Constant name "pylint" doesn't conform to UPPER_CASE naming style (invalid-name)
cs330_04_3.py:4:0: C0103: Constant name "requests" doesn't conform to UPPER_CASE naming style (invalid-name)
cs330_04_3.py:5:0: C0103: Constant name "pycodestyle" doesn't conform to UPPER_CASE naming style (invalid-name)
cs330_04_3.py:6:0: C0413: Import "from unittest import TestCase, mock" should be placed at the top of the module (wrong-import-position)
cs330_04_3.py:7:0: C0413: Import "from __main__ import get_repo_info" should be placed at the top of the module (wrong-import-position)
cs330_04_3.py:7:0: E0611: No name 'get_repo_info' in module '__main__' (no-name-in-module)
cs330_04_3.py:9:0: C0115: Missing class docstring (missing-class-docstring)
cs330_04_3.py:12:4: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_3.py:23:8: E1111: Assigning result of a function call, where the function has no return (assignment-from-no-return)
cs330_04_3.py:24:25: E1136: Value 'result' is unsubscriptable (unsubscriptable-object)
cs330_04_3.py:25:25: E1136: Value 'result' is unsubscriptable (unsubscriptable-object)
cs330_04_3.py:32:0: C0103: Constant name "Bearer_token" doesn't conform to UPPER_CASE naming style (invalid-name)
cs330_04_3.py:33:0: C0116: Missing function or method docstring (missing-function-docstring)
cs330_04_3.py:33:0: E0102: function already defined line 7 (function-redefined)
cs330_04_3.py:33:18: W0621: Redefining name 'owner' from outer scope (line 64) (redefined-outer-name)
cs330_04_3.py:33:25: W0621: Redefining name 'repo_name' from outer scope (line 65) (redefined-outer-name)
cs330_04_3.py:59:11: W0718: Catching too general exception Exception (broad-exception-caught)
cs330_04_3.py:37:19: E1101: Instance of 'str' has no 'get' member (no-member)
cs330_04_3.py:54:11: E1101: Instance of 'str' has no 'exceptions' member (no-member)
cs330_04_3.py:2:0: C0411: standard import "unittest" should be placed before third party import "requests" (wrong-import-order)
cs330_04_3.py:6:0: C0411: standard import "unittest.TestCase" should be placed before third party import "requests" (wrong-import-order)

"""
#pycodestyle
"""cs330_04_3.py:6:1: E402 module level import not at top of file
cs330_04_3.py:7:1: E402 module level import not at top of file
cs330_04_3.py:9:1: E302 expected 2 blank lines, found 1
cs330_04_3.py:10:1: W293 blank line contains whitespace
cs330_04_3.py:22:1: W293 blank line contains whitespace
cs330_04_3.py:27:1: E305 expected 2 blank lines after class or function definition, found 1
cs330_04_3.py:32:19: W291 trailing whitespace
cs330_04_3.py:33:1: E302 expected 2 blank lines, found 0
cs330_04_3.py:34:43: W291 trailing whitespace
cs330_04_3.py:35:1: W293 blank line contains whitespace
cs330_04_3.py:39:31: E261 at least two spaces before inline comment
cs330_04_3.py:40:1: W293 blank line contains whitespace
cs330_04_3.py:53:1: W293 blank line contains whitespace
cs330_04_3.py:56:80: E501 line too long (103 > 79 characters)
cs330_04_3.py:56:81: E261 at least two spaces before inline comment
cs330_04_3.py:62:1: E305 expected 2 blank lines after class or function definition, found 1
cs330_04_3.py:64:80: E501 line too long (96 > 79 characters)
cs330_04_3.py:65:53: W291 trailing whitespace
cs330_04_3.py:66:36: E261 at least two spaces before inline comment
cs330_04_3.py:66:80: E501 line too long (89 > 79 characters)
"""
#pep8
"""pep8 has been renamed to pycodestyle (GitHub issue #466)
Use of the pep8 tool will be removed in a future release.
Please install and use `pycodestyle` instead.

$ pip install pycodestyle
$ pycodestyle ...  

warnings.warn(
cs330_04_3.py:6:1: E402 module level import not at top of file
cs330_04_3.py:7:1: E402 module level import not at top of file
cs330_04_3.py:9:1: E302 expected 2 blank lines, found 1
cs330_04_3.py:10:1: W293 blank line contains whitespace
cs330_04_3.py:22:1: W293 blank line contains whitespace
cs330_04_3.py:32:19: W291 trailing whitespace
cs330_04_3.py:33:1: E302 expected 2 blank lines, found 0
cs330_04_3.py:34:43: W291 trailing whitespace
cs330_04_3.py:35:1: W293 blank line contains whitespace
cs330_04_3.py:39:31: E261 at least two spaces before inline comment
cs330_04_3.py:40:1: W293 blank line contains whitespace
cs330_04_3.py:53:1: W293 blank line contains whitespace
cs330_04_3.py:56:80: E501 line too long (103 > 79 characters)
cs330_04_3.py:56:81: E261 at least two spaces before inline comment
cs330_04_3.py:64:80: E501 line too long (96 > 79 characters)
cs330_04_3.py:65:53: W291 trailing whitespace
cs330_04_3.py:66:36: E261 at least two spaces before inline comment
cs330_04_3.py:66:80: E501 line too long (89 > 79 characters)
"""