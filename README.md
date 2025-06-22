# space-debris-tracker

A Python-based tool for tracking space debris, assessing collision risk, and determining removal feasibility

# Space Debris Tracker

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub Issues](https://img.shields.io/github/issues/aerospacemc/space-debris-tracker)](https://github.com/aerospacemc/space-debris-tracker/issues)

## Overview

The Space Debris Tracker is a Python-based tool designed to monitor and analyze the growing problem of space debris. It will provide functionalities for:

*   **PHASE-1 Data Acquisition:** Automatically downloading Two-Line Element (TLE) data from online sources.
*   **PHASE-1 Short Term Orbit Prediction:** Propagating orbits of debris objects to predict future positions.
*   **PHASE-2 Filtering and Initial Assessment:** Debris Filtering, Conjunction Analysis
*   **PHASE-3 Risk Scoring and Feasibility:** Risk Scoring, Initial Feasibility Assessment
*   **PHASE-4 Refinement and Expansion:** Refine Orbit Prediction, Advanced Conjunction Analysis, Data Integration, Refine Feasibility Assessment, Visualization
*   **PHASE-5 Optimization and Deployment:** Optimization, Testing and Validation, Deployment

This project aims to contribute to a better understanding of the space debris environment and support efforts to ensure the long-term sustainability of space activities.

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

0.  **Get Git:**
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
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables** (if needed):
    - Create a `.env` file in the root directory.
    - Add API keys or configuration variables as required.

## Usage

1.  **Run the main script:**

    ```bash
    python3 debris_clustering10.py
    ```

2.  **Follow the on-screen instructions** to load data, perform orbit analysis, and run risk assessments.

---

## Contribution Guidelines

We welcome contributions! To contribute:

1. Fork the repo.
2. Create a feature or bugfix branch: `git checkout -b feature/my-feature`.
3. Develop your changes and add tests.
4. Follow PEP 8 coding standards.
5. Submit a pull request for review.

### Reporting bugs:
Please open an issue with:
- A clear description
- Steps to reproduce
- Expected vs. actual behavior
- Any relevant error messages

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Contact
