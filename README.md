# Space Debris Tracker - A Python-based tool for tracking space debris, assessing collision risk, and determining removal feasibility

Hi everyone! We're building an open-source tool for space debris tracking and mitigation, aiming to improve satellite safety and 
reduce clutter in Earth's orbit. If you're passionate about space tech and open-source development, we'd love your help! Check it out and contribute

Vision - Making Orbit Safe: Active Debris Removal as a Service (ODRaaS)

Space-Debris-Tracker Application Objectives:  
* Define operational envelope: debris target types(size/mass),altitudes, inclinations, removal rate goals
* Orbital Scenario Simulation: Identify conjunction-prone targets using historical and projected data
* Conjunction Risk reduction modeling: quantify the net benefit of removing different debris types using a Monte Carlo approach
* AI Path Planning and Dynamic Scheduling: demonstrate a convergent, safe approach to planning for multi-target missions and real-time rerouting

# Space Debris Tracker

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTORS.md)
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
    sudo apt-get update
    sudo apt-get install pkg-config meson cmake libdbus-1-dev
    sudo apt-get install libglib2.0-dev
    sudo apt-get install libcurl4-openssl-dev
    sudo apt-get install libcairo2-dev
    sudo apt-get install libsmbclient-dev
     **Install Python**
    sudo apt-get install python3.10 python3.10-venv python3.10-dev
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
    curl https://pyenv.run | bash
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv virtualenv-init -)"
    Restart your shell or source your profile.
    source ~/.bashrc  # or ~/.zshrc
    pyenv --version
    sudo apt-get update
    sudo apt-get update
    sudo apt-get install libcups2-dev libgirepository1.0-dev gir1.2-gtk-3.0

    pip install -r requirements.txt
    ```

5.  **Configure environment variables (if needed):**

    *   Create a `.env` file in the project root directory.
    *   Set any necessary environment variables (e.g., API keys, data directories).
    python -m venv env
    source env/bin/activate
    pip install --upgrade pip setuptools


## Usage

1.  **Run the main script:**

    ```bash
    python3 debris_clustering10.py
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

This project is licensed under the Apache License. See the `LICENSE` file for details.

## Contact

*   aerospacemc
*  info@aerospacemc.com
*   [GitHub Profile](https://github.com/aerospacemc)

## Acknowledgements

*   [Celestrak](https://celestrak.org/) for providing TLE data.
*   The Skyfield developers for creating a powerful astrodynamics library.
*   The open-source community for contributing to the advancement of space research.

---
