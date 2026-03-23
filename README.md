# RTE-Biochar-Data

This repository contains the supporting dataset for the manuscript:

**Rapid Thermal Engineering of Biochar-Derived Porous Carbon Enabling Controlled Pore Evolution and Enhanced Transport Properties**

---
### figures
- Fig3_BET.png : BET adsorption isotherm
- Fig4_TGA.png : thermogravimetric profile
- Fig5_Transport.png : transport performance comparison
## Repository Structure

### BET
- `isotherm_raw.csv`  
  Raw nitrogen adsorption–desorption data for untreated and rapid thermally treated biochar samples.

- `pore_distribution.csv`  
  BJH pore size distribution data showing mesopore evolution.

---

### SEM
- `untreated_SEM_1.png`  
- `treated_SEM_1.png`  
- `untreated_SEM_2.png`  
- `treated_SEM_2.png`  

Scanning electron microscopy images showing microstructural evolution before and after rapid thermal engineering.

---

### TGA
- `tga_curve.csv`  

Thermogravimetric and derivative thermal data showing devolatilisation behaviour and carbon stability.

---

### Transport
- `diffusion_results.csv`  

Effective diffusion coefficient measurements with replicate data across treatment conditions.

---

### metadata
- `experiment_conditions.txt`  
  Full processing and characterisation parameters.

- `sample_description.txt`  
  Description of untreated and treated samples.

- `summary_results.csv`  
  Consolidated key results aligned with manuscript values.

---
### scripts
- `plot_all.py`  
  Python script to regenerate BET, pore size distribution, TGA/DTG, and transport plots from the uploaded datasets.
  
## Key Findings

- Specific surface area increased from **145 ± 6 m²/g to 185 ± 7 m²/g**
- Mesopore contribution increased following rapid thermal treatment
- Transport performance improved by approximately **15–20%**
- Major devolatilisation occurred between **300–600 °C**
- Residual carbon stabilised at approximately **63%**

---
### SEM
- `Fig2_SEM_microstructure.png`  

Composite SEM micrograph showing microstructural evolution of biochar-derived carbon before and after rapid thermal engineering:

(a) untreated sample  
(b) treated sample (RTE)  
(c) untreated close-up  
(d) treated close-up  

Scale bars: 2 µm

## Data Format

All datasets are provided in **CSV format** for:
- reproducibility
- independent verification
- direct plotting and modelling

---
## License
This project is licensed under the MIT License.
## Notes

The dataset represents processed experimental measurements consistent with the reported results in the manuscript.

---

## Corresponding Author

Dr Reji Kurien Thomas  
TOL Biotech  
Email: founder@technopilot.in
