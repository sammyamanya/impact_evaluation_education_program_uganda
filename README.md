# Education Impact Evaluation of an Education Support Program in Rural Uganda

## Project Overview

This project evaluates the impact of a hypothetical education support program on learning outcomes among Primary 5 and Primary 6 pupils in a government primary school in rural Uganda.

Using synthetic data, the project demonstrates the application of causal inference methods commonly used in Monitoring and Evaluation (M&E), education research, social policy evaluation, and development economics.

The analysis follows a structured impact evaluation workflow, beginning with exploratory analysis and progressing through increasingly rigorous estimation approaches.

---

## Evaluation Question

**What is the effect of an education support program on pupil learning outcomes?**

Specifically, the project estimates the impact of program participation on pupil test scores using quasi-experimental methods.

---

## Intervention

The hypothetical education support program includes:

- Remedial reading sessions
- Mathematics tutoring
- Teacher coaching
- Learning materials
- Attendance monitoring

The program targets Primary 5 and Primary 6 pupils and aims to improve learning outcomes through enhanced instructional support and pupil engagement.

---

## Theory of Change

```text
Education Support Program
            ↓
Improved Learning Environment
            ↓
Higher Attendance and Study Effort
            ↓
Improved Academic Performance
            ↓
Higher Test Scores
```

---

## Data

The dataset was synthetically generated for educational and portfolio purposes.

### Dataset Characteristics

- 240 pupils
- Primary 5 and Primary 6 learners
- Treatment and comparison groups
- Baseline and endline observations
- Total observations: 480

### Variables

- Student ID
- Class Level
- Gender
- Treatment Status
- Attendance Rate
- Weekly Study Hours
- Test Score
- Survey Round (Baseline/Endline)

---

## Methods

The project applies four analytical approaches:

### 1. Exploratory Data Analysis (EDA)

- Descriptive statistics
- Distribution analysis
- Baseline comparisons
- Visual exploration of key variables

### 2. Difference-in-Differences (DiD)

A Difference-in-Differences framework was used to estimate the program effect by comparing changes in test scores over time between treatment and comparison pupils.

### 3. Propensity Score Matching (PSM)

Propensity scores were estimated using:

- Gender
- Class level
- Attendance rate
- Study hours

Nearest-neighbor matching was then used to improve comparability between treatment and comparison pupils.

### 4. Propensity Score Matching + Difference-in-Differences (PSM + DiD)

The matched sample was subsequently used in a Difference-in-Differences framework to produce a more robust estimate of program impact.

---

## Covariate Balance Assessment

### Purpose

Propensity Score Matching (PSM) was used to improve comparability between treatment and comparison pupils prior to impact estimation.

### Matched Sample Balance

| Covariate | Comparison Group | Treatment Group |
|------------|----------------:|----------------:|
| Attendance Rate (%) | 84.41 | 84.98 |
| Study Hours per Week | 6.09 | 6.09 |
| Average Test Score | 72.83 | 72.60 |

### Interpretation

The balance assessment indicates that the matching procedure successfully improved comparability between treatment and comparison pupils.

Post-matching attendance rates were highly similar across groups, differing by less than one percentage point. Average study hours were identical between groups, while average test scores differed by only 0.23 points.

The substantial overlap observed in propensity score distributions further supports the validity of the matching procedure.

### Key Takeaway

> The matching procedure successfully constructed a comparison group that closely resembles program participants on observed characteristics, strengthening the foundation for causal impact estimation.

---

## Results

### Impact Estimates

| Method | Estimated Impact (Points) |
|----------|-------------------------:|
| Difference-in-Differences (DiD) | 7.22 |
| Propensity Score Matching + DiD | 7.52 |

### Difference-in-Differences Results

The Difference-in-Differences analysis estimated that participation in the education support program increased pupil test scores by approximately **7.22 points** relative to the comparison group.

### PSM + DiD Results

After improving baseline comparability through Propensity Score Matching, the estimated program impact was **7.52 points**.

The close similarity between the two estimates suggests that the findings are robust to observable baseline differences between treatment and comparison pupils.

### Main Finding

The education support program was associated with an improvement of approximately **7 to 8 test-score points** across multiple evaluation approaches.

The consistency of estimates across methods increases confidence in the credibility of the findings.

---

## Repository Structure

```text
impact_evaluation_education_program_uganda
│
├── README.md
├── policy_brief.md
├── requirements.txt
│
├── data/
│   └── synthetic_education_data.csv
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_difference_in_differences.ipynb
│   ├── 03_propensity_score_matching.ipynb
│   └── 04_psm_did.ipynb
│
├── src/
│   └── generate_data.py
│
└── outputs/
    ├── figures/
    └── tables/
```

---

## Reproducing the Analysis

### Clone the Repository

```bash
git clone https://github.com/sammyamanya/impact_evaluation_education_program_uganda.git
```

### Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Generate the Dataset

```bash
python src/generate_data.py
```

### Run the Analysis

Open and execute the notebooks in sequence:

1. `01_data_exploration.ipynb`
2. `02_difference_in_differences.ipynb`
3. `03_propensity_score_matching.ipynb`
4. `04_psm_did.ipynb`

---

## Disclaimer

All data used in this repository are synthetic and were generated for educational and portfolio purposes only.

This project demonstrates impact evaluation methodologies and does not represent findings from an actual education intervention, school, or program.

---

## Author

**Samuel Amanya**