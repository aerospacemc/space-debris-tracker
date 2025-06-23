# Branch: Phase 2: Filtering 

Purpose: This repository serves as the home for code developed and tested specifically for Phase 1 of the project.

Development Workflow:
*   Developers fork the main repository to contribute.
*   They create feature branches within their forks for specific tasks (e.g., feature/automated-tle-download).
*   Developers implement and rigorously test their code within these feature branches.
*   Once a feature is ready, they submit a pull request (PR) to merge their changes into the designated phase branch (e.g., phase-1).
*   The pull request undergoes code review and discussion.
*   After approval, the PR is merged into the phase branch, integrating the new code into the project.

## Requirements

**1. Filtering by Debris Size, Shape, Orbit:**

*   **Problem:** Need to incorporate additional debris characteristics into the analysis.  This often involves external data sources or estimations.
*   **Solution:**
    *   **Data Integration:**
        *   **Size and Shape:** These are difficult to obtain directly.  Consider correlating radar cross-section (RCS) data with size estimates.  Sources like Space-Track.org may provide RCS data.  Need to create or find a mapping between RCS and approximate size.
        *   **Orbit:** The Code is already using orbital parameters.  Need to define filters based on inclination, altitude (derived from semi-major axis), eccentricity, etc.
    *   **Filtering Logic:** Add conditional statements to filter the `satellites` list based on these criteria *before* clustering.


## Related Issues/Tasks

*   <links to related issues in your issue tracker>

## Status

* "In Development"

## Owner

<name of the developer responsible for the branch>
