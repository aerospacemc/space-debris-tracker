# space-debris-tracker
A Python-based tool for tracking space debris, assessing collision risk, and determining removal feasibility

# Space Debris Tracker

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub Issues](https://img.shields.io/github/issues/your-username/space-debris-tracker)](https://github.com/your-username/space-debris-tracker/issues)

## Overview

The Space Debris Tracker is a Python-based tool designed to monitor and analyze the growing problem of space debris. It will provide functionalities for:

*   **PHASE-1 Data Acquisition:** Automatically downloading Two-Line Element (TLE) data from online sources.
*   **PHASE-1 Short Term Orbit Prediction:** Propagating orbits of debris objects to predict future positions.
*   **PHASE-2 Filtering and Initial Assessment:** Debris Filtering, Conjunction Analysis
*   **PHASE-3 Risk Scoring and Fessibility:** Risk Scoring, Initial Feasabilty Assessment
*   **PHASE-4 Refinement and Expansion:** Refine Orbit Prediction, Advanced Conjunction Analysis, Data Integration, Refine Feasibility Assessment, Visualization
*   **PHASE-5 Optimization and Deployment:** Optimization, Testing and Validation, Deployment

This project aims to contribute to a better understanding of the space debris environment and to support efforts to ensure the long-term sustainability of space activities.

## Goals

*   Develop a robust and accurate system for tracking space debris.
*   Provide tools for assessing the risk of collisions between debris and operational satellites.
*   Evaluate the feasibility of different debris removal and mitigation strategies.
*   Foster community collaboration and contribute to the open-source space community.

## Key Features

*   **Automated TLE Data Acquisition:** Downloads TLE data from Celestrak (or other sources) on a regular basis.
*   **Orbit Propagation:** Uses Skyfield (or other astrodynamics libraries) to predict future positions of debris objects.
*   **Collision Risk Assessment:** Calculates proximity and estimates the probability of collision between debris and satellites.
*   **Feasibility Scoring:** Evaluates the feasibility of removing debris based on delta-V requirements, size, tumbling rate, and mission constraints.
*   **Data Visualization:** Provides interactive visualizations of debris orbits, potential conjunctions, and risk levels.
*   **Open-Source and Extensible:** Designed for community contributions and easy integration with other tools and data sources.

## Dependencies

*   Python 3.7+
*   NumPy
*   Skyfield
*   Matplotlib/Plotly (for visualization)
*   Requests
*   Schedule
*   (Other dependencies listed in `requirements.txt`)

## Setup

0.  **get Git:**
    ```bash
    sudo apt update
    sudo apt install git
    ```

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/aerospacemc/space-debris-tracker.git
    cd space-debris-tracker
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    sudo apt update
    sudo apt install python3-pip
    pip3 --version
    sudo apt install python3.11-venv
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

4.  **Install dependencies:**

    ```bash
    sudo apt-get install python3-brlapi
    pip install -r requirements.txt
    ```

5.  **Configure environment variables (if needed):**

    *   Create a `.env` file in the project root directory.
    *   Set any necessary environment variables (e.g., API keys, data directories).

## Usage

1.  **Run the main script:**

    ```bash
    python src/main.py
    ```

2.  **Follow the instructions in the console to interact with the program.**

    *   The program will load TLE data, propagate orbits, and perform risk assessments.  (Future enhancement)
    *   You can configure the program's behavior through command-line arguments or configuration files.

## Contribution Guidelines

We welcome contributions from the community! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix: `git checkout -b phase/my-new-phase-feature`
3.  Develop your code and write tests.
4.  Follow the code style guidelines (PEP 8).
5.  Create a pull request to the appropriate phase branch (e.g., `phase-1`, `phase-2`).
6.  Your pull request will be reviewed by the project maintainers.

### Code Style

*   Follow PEP 8 guidelines.
*   Write clear and concise code with comments.
*   Write unit tests for all new features.

### Reporting Bugs

If you find a bug, please report it by creating a new issue in the issue tracker.  Be sure to include:

*   A clear description of the bug
*   Steps to reproduce the bug
*   The expected behavior
*   The actual behavior
*   Any relevant error messages

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

*   aerospacemc
*  info@aerospacemc.com
*   [GitHub Profile](https://github.com/aerospacemc)

## Acknowledgements

*   [Celestrak](https://celestrak.org/) for providing TLE data.
*   The Skyfield developers for creating a powerful astrodynamics library.
*   The open-source community for contributing to the advancement of space research.

---


