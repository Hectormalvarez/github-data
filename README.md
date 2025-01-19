# GitHub Data Fetcher

A Python tool to fetch data from public GitHub repositories. Currently supports fetching issues, but designed to be extensible for other repository data (e.g., pull requests, commits, releases).

---

## Features

- **Fetch Data**: Retrieve data (e.g., issues) from any public GitHub repository.
- **Pagination Support**: Handles pagination to fetch all results, even for large datasets.
- **Secure Credentials**: Uses a `.env` file for secure GitHub credentials (optional for public repos).
- **JSON Output**: Outputs data as JSON for easy processing and integration.

---

## Future Plans

Planned enhancements will be tracked as GitHub issues and resolved with commits:

1. **Expand Data Types**: Add support for pull requests, commits, releases, etc.
2. **Filtering**: Filter data by specific criteria (e.g., state, date, labels).
3. **Sorting**: Sort data by creation date, update date, or other fields.
4. **Export Formats**: Export data to CSV, Markdown, or other formats.
5. **CLI Options**: Add command-line arguments for flexibility.
6. **Error Handling**: Improve error handling for API requests.
7. **Tests**: Add unit tests for reliability.
8. **Refactor**: Refactor into a reusable Python package.

---

## Setup

### Prerequisites

- Python 3.x
- `python-dotenv` package (install via `pip install python-dotenv`)
- A GitHub Personal Access Token (PAT) for authentication (optional but recommended for higher rate limits)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Create a `.env` file (optional for public repos):

   ```plaintext
   GITHUB_USERNAME=your_username
   GITHUB_REPOSITORY=your_repo
   GITHUB_TOKEN=your_personal_access_token
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the script to fetch data from the specified GitHub repository:

```bash
python main.py
```

The script will output the fetched data as a JSON object. You can redirect the output to a file if needed:

```bash
python main.py > output.json
```

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, descriptive messages.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
