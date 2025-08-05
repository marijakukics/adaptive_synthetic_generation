# Adaptive Synthetic Population Generation using One-step Gibbs Sampler

This repository provides a reproducible implementation of the adaptive synthetic population generation framework described in the paper *"Adaptive synthetic generation using one-step Gibbs Sampler"* (under review).

The method combines:
- Initial population generation using a one-step Gibbs Sampler
- Annual demographic projection through dynamic projection
- Adaptive resampling using Gibbs-based correction based on newly available data

---

## Repository Overview

This repository includes three Jupyter notebooks:

- `01_generation.ipynb`: Generates an initial synthetic population based on disaggregated data using a Gibbs sampler.
- `02_projection.ipynb`: Simulates year-by-year demographic evolution using event-driven microsimulation.
- `03_resampling.ipynb`: Applies a resampling step to align synthetic data with newly available marginal distributions using Gibbs resampling.

---


Note: The original Swiss MTMC datasets used in the paper are not included due to data sharing agreements. A dummy dataset is provided for demonstration purposes.

---

### 1. Install dependencies
You can install required Python packages using: pip install -r requirements.txt


### 2. Run the Notebooks

Use **Jupyter Notebook** to execute each notebook in order:

1. `01_generation.ipynb`
2. `02_projection.ipynb`
3. `03_resampling.ipynb`

Each notebook is self-contained and includes documentation to help reproduce the steps from the paper.

---

### Demo Data

We include a small dummy dataset: `synthetic_sample.csv` to illustrate the workflow.  
This dataset mimics the structure of the real MTMC data and supports full execution of the code.

### Attributes used

**Individual level:**
- Age (grouped)
- Sex
- Employment status
- Marital status
- Driving license

**Household level:**
- Household size
- Household type
- Number of cars

You may replace the dummy data with your own disaggregated dataset, as long as the structure and attributes are preserved.

---

### Citation

**Paper:** *Adaptive synthetic generation using one-step Gibbs Sampler*  
**Authors:** Marija Kukic, Michel Bierlaire  
**Status:** Under review at *Transportation Research Interdisciplinary Perspectives*  
**Link:** TBA

> If you use this code for academic work, please cite the paper once it becomes publicly available.

---

## Contact
For any additional questions, you can email me! 
**Marija Kukic**  
[marija.kukic@epfl.ch](mailto:marija.kukic@epfl.ch)


