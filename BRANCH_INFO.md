# Branch: Phase 1: Data Acquisition 

Purpose: This repository serves as the home for code developed and tested specifically for Phase 1 of the project.

Development Workflow:
*   Developers fork the main repository to contribute.
*   They create feature branches within their forks for specific tasks (e.g., feature/automated-tle-download).
*   Developers implement and rigorously test their code within these feature branches.
*   Once a feature is ready, they submit a pull request (PR) to merge their changes into the designated phase branch (e.g., phase-1).
*   The pull request undergoes code review and discussion.
*   After approval, the PR is merged into the phase branch, integrating the new code into the project.

## Requirements

**1. Continuous Data Acquisition:**

*   **Problem:** The current code loads TLE data from a file only once. Needed: a mechanism to periodically update this data.
*   **Solution:**
    *   **Download TLEs Automatically:** Implement a function to download TLE data from a reliable online source (e.g., Celestrak).  Use the `requests` library in Python.
    *   **Schedule Updates:** Use a scheduler (e.g., `schedule` library or `threading.Timer`) to run the download function at regular intervals (e.g., every hour, every day).
    *   **Error Handling:** Add robust error handling to the download function to catch network issues or changes in the data source format.
    *   **Data Storage:** Consider storing TLE data in a database (e.g., SQLite, PostgreSQL) for easier management and retrieval.


## Related Issues/Tasks

*   <links to related issues in your issue tracker>

## Status

* "In Development"

## Owner

<name of the developer responsible for the branch>
