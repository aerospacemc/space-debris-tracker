# Branch: Phase 3: Risk Scoring and Feasibility

Purpose: This repository serves as the home for code developed and tested specifically for Phase 3 of the project.

Development Workflow:
*   Developers fork the main repository to contribute.
*   They create feature branches within their forks for specific tasks (e.g., feature/automated-tle-download).
*   Developers implement and rigorously test their code within these feature branches.
*   Once a feature is ready, they submit a pull request (PR) to merge their changes into the designated phase branch (e.g., phase-1).
*   The pull request undergoes code review and discussion.
*   After approval, the PR is merged into the phase branch, integrating the new code into the project.

## Requirements

Phase 3: Risk Scoring and Feasibility Assessment

Overall Goal: To prioritize the debris objects that pose the greatest risk and to assess the feasibility of removing or mitigating those objects. This involves developing a risk scoring system and evaluating the technical and economic feasibility of different mitigation strategies.

1 Risk Scoring:

Problem: Not all potential conjunctions are equally risky. Some debris objects are larger, faster, or more likely to collide with a valuable asset.

Solution: Develop a risk scoring system that considers factors such as the probability of collision, the size/mass of the debris object, the kinetic energy of the debris object, and the value of the asset at risk.

Implementation Steps:
*   Define Risk Factors: Determine the specific factors to include in the risk score and assign weights to each factor based on their relative importance.
*   Calculate Risk Scores: Implement the risk scoring algorithm to calculate a risk score for each debris object.
*   Rank Debris Objects: Rank the debris objects based on their risk scores.
*   Visualization: Create visualizations to display the risk scores of the debris objects. *5. Document all of these processes within the BRANCH.md

**Risk Scoring:**
    *   Develop a basic risk scoring system that considers the probability of collision (based on proximity), debris size, and the value of the asset at risk.
    *   Assign weights to each factor to reflect their relative importance.
    *   Calculate the risk score for each debris object and rank them accordingly.

2 Feasibility Assessment (Initial):

Problem: Removing or mitigating all high-risk debris objects is not feasible due to technical and economic constraints.

Solution: Develop a basic feasibility assessment that considers factors such as the delta-V required to reach the debris object, the size and shape of the debris object, the tumbling rate of the debris object, and the technology readiness level of the removal/mitigation technology.

Implementation Steps:
*   Define Feasibility Factors: Determine the specific factors to include in the feasibility assessment and assign weights to each factor based on their relative importance.
*   Assess Feasibility: Implement the feasibility assessment algorithm to calculate a feasibility score for each debris object.
*   Combine Risk and Feasibility: Combine the risk score and feasibility score to prioritize debris objects for removal/mitigation.
*   Document all of these processes within the BRANCH.md
*   Test and Validate Output: Create functions to simulate various cases to see that high risk targets are shown, and which are feasible to meet with success

**Feasibility Assessment (Initial):**
    *   Implement the `assess_target_feasibility` function.
    *   Start with a simplified feasibility assessment that considers the delta-V to reach the debris object (using a placeholder `calculate_delta_v` function), size, and tumbling rate.
    *   Combine these factors into a feasibility score.

## Related Issues/Tasks

*   <links to related issues in your issue tracker>

## Status

* "In Development"

## Owner

<name of the developer responsible for the branch>
