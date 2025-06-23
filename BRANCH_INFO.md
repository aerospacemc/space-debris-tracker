# Branch: Phase 2: Filtering and Initial Risk Assessment

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

   **Debris Filtering:**
       *   Start with a simple filtering implementation (e.g., based on inclination and a placeholder size attribute, as in the example).
       *   Test the filtering to ensure that it correctly selects debris objects based on the defined criteria.
       *   Later, integrate actual size data (e.g., from RCS values) if available.

**2. Risk Assessment:**

*   **Problem:** Need to determine which debris poses the most risk to operational satellites or other assets.
*   **Solution:**
    *   **Conjunction Analysis(Basic):**
        *   **Target Satellites:** Define a list of operational satellites to be protected.  Get their TLE data as well.
        *   **Proximity Calculation:** For each debris object, calculate its proximity to the target satellites over your prediction horizon.  This involves comparing their predicted positions at each time step.  Use a distance threshold (e.g., 1 km) to identify potential conjunctions.
        *   **Probability of Collision (POC):** More advanced methods estimate the POC based on position uncertainties.  Libraries like Orekit can help with this.
    *   **Risk Scoring:** Develop a risk score that considers:
        *   **Probability of Collision:** Higher POC = higher risk.
        *   **Size/Mass of Debris:** Larger debris = higher risk (more damage).
        *   **Kinetic Energy:**  Related to velocity; higher velocity = higher risk.
        *   **Value of Asset at Risk:** Protecting a critical satellite = higher risk.
    *   **Prioritization:** Rank the debris objects based on their risk scores.
 
       *   **Conjunction Analysis (Basic):**
       *   Define a set of target satellites with their TLE data.  You may need to manually add these initially.
       *   Implement the `assess_collision_risk` function to calculate the proximity between debris and target satellites over the prediction horizon.
       *   Start with a simple distance threshold to identify potential conjunctions.
       *   Verify that the conjunction analysis identifies close approaches between debris and target satellites.

## Related Issues/Tasks

*   <links to related issues in your issue tracker>

## Status

* "In Development"

## Owner

<name of the developer responsible for the branch>
