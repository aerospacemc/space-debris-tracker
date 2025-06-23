# Branch: Phase 4: Refinement and Expansion - Advanced Conjunction Analysis

Purpose: This repository serves as the home for code developed and tested specifically for Phase 4 of the project.

Development Workflow:
*   Developers fork the main repository to contribute.
*   They create feature branches within their forks for specific tasks (e.g., feature/automated-tle-download).
*   Developers implement and rigorously test their code within these feature branches.
*   Once a feature is ready, they submit a pull request (PR) to merge their changes into the designated phase branch (e.g., phase-4).
*   The pull request undergoes code review and discussion.
*   After approval, the PR is merged into the phase branch, integrating the new code into the project.

## Requirements

Phase 4: Refinement and Expansion - Advanced Conjunction Analysis

Overall Goal: To improve the accuracy, scope, and usability of the space debris tracking system by refining the orbit prediction models, enhancing the conjunction analysis algorithms, integrating additional data sources, improving the feasibility assessment, and adding new visualization capabilities.


4.2 Advanced Conjunction Analysis:

Problem: The basic conjunction analysis algorithm only considers the proximity between debris objects and target satellites, but it doesn't account for the uncertainties in the orbit predictions.

Solution: Implement more advanced conjunction analysis techniques that estimate the probability of collision (POC) based on position uncertainties.

Implementation Steps:
*   Estimate Position Uncertainties: Develop methods for estimating the uncertainties in the orbit predictions, based on factors such as the age of the TLE data and the accuracy of the orbit propagation model.
*   Calculate Probability of Collision (POC): Implement a POC algorithm that takes into account the position uncertainties of the debris object and target satellite.
*   Refine Conjunction Reporting: Report the POC for each potential conjunction, in addition to the time of closest approach and distance at closest approach.


## Related Issues/Tasks

*   <links to related issues in your issue tracker>

## Status

* "In Development"

## Owner

<name of the developer responsible for the branch>
