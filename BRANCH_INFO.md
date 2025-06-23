# Branch: Phase 1: Foundation - Basic Prediction

Purpose: This repository serves as the home for code developed and tested specifically for Phase 1 of the project.

Development Workflow:
*   Developers fork the main repository to contribute.
*   They create feature branches within their forks for specific tasks (e.g., feature/automated-tle-download).
*   Developers implement and rigorously test their code within these feature branches.
*   Once a feature is ready, they submit a pull request (PR) to merge their changes into the designated phase branch (e.g., phase-1).
*   The pull request undergoes code review and discussion.
*   After approval, the PR is merged into the phase branch, integrating the new code into the project.

## Requirements

**1. Short-Term Prediction:**

*   **Problem:** The current code uses a single snapshot in time. Needed: propagate the orbits to predict future positions.
*   **Solution:**
    *   **Orbit Propagation:** Use Skyfield's `at()` method with different times to predict satellite positions at future epochs.
    *   **Time Deltas:** Create an array of time deltas to define the prediction horizon (e.g., predict positions every 10 minutes for the next 24 hours).
    *   **Store Predictions:** Store the predicted positions (and other orbital parameters) for each satellite at each time step.  Consider using NumPy arrays or Pandas DataFrames for efficient storage and manipulation.

## Related Issues/Tasks

*   <links to related issues in your issue tracker>

## Status

* "In Development"

## Owner

<name of the developer responsible for the branch>
