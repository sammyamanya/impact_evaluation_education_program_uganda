# impact_evaluation_education_program_uganda
To estimate the impact of an education support program on pupil learning outcomes among Primary 5 and Primary 6 students in a government primary school in rural Uganda.

The project demonstrates the application of causal inference methods commonly used in education, development, and social policy evaluations.

# Education Impact Evaluation in rural Uganda

## Project Overview

This project uses synthetic data to evaluates the effect of a hypothetical education support program on test scores among Primary 5 and Primary 6 pupils in a government primary school in Northern Uganda.

The project demonstrates the application of causal inference methods commonly used in education research, monitoring and evaluation (M&E), and impact evaluation.

## Evaluation Question

What is the effect of an education support program on pupil learning outcomes?

## Intervention

The hypothetical education support program includes:

- Remedial reading sessions
- Mathematics tutoring
- Teacher coaching
- Learning materials
- Attendance monitoring

## Methods

The analysis will be conducted using:

- Exploratory Data Analysis (EDA)
- Difference-in-Differences (DiD)
- Propensity Score Matching (PSM)
- Propensity Score Matching with Difference-in-Differences (PSM + DiD)

## Covariate Balance Assessment

### Purpose

Propensity Score Matching (PSM) was used to improve comparability between treatment and comparison pupils before estimating the impact of the education support program.

Matching was based on observed pupil characteristics, including:

- Attendance rate
- Study hours per week
- Class level (P5/P6)
- Gender

### Matched Sample Balance

| Covariate | Comparison Group | Treatment Group |
|------------|----------------:|----------------:|
| Attendance Rate (%) | 84.41 | 84.98 |
| Study Hours per Week | 6.09 | 6.09 |
| Average Test Score | 72.83 | 72.60 |

### Interpretation

The balance assessment indicates that the matching procedure successfully improved comparability between treatment and comparison pupils.

After matching, attendance rates were highly similar across groups, differing by less than one percentage point. Average study hours were identical between groups, while mean test scores differed by only 0.23 points. These small differences suggest that the matched sample achieved a high degree of balance on key observed characteristics.

In addition, the propensity score distributions exhibited substantial overlap between treatment and comparison pupils, indicating adequate common support for matching.

### Implications for Impact Estimation

Because treatment and comparison pupils are more similar after matching, the subsequent Propensity Score Matching plus Difference-in-Differences (PSM + DiD) analysis is expected to provide a more credible estimate of program impact than a simple Difference-in-Differences approach alone.

### Key Takeaway

> The matching procedure successfully constructed a comparison group that closely resembles program participants on observed characteristics, strengthening the foundation for causal impact estimation.

## Repository Structure

```text
education-impact-evaluation-northern-uganda
│
├── README.md
├── policy_brief.md
├── requirements.txt
│
├── data/
├── notebooks/
├── src/
│
└── outputs/
    ├── figures/
    └── tables/
```

## Disclaimer

All data used in this repository are synthetic and were generated for educational and portfolio purposes only.

The project demonstrates impact evaluation methods and does not represent findings from a real school, program, or intervention.

## Author

Samuel Amanya
