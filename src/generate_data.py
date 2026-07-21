import numpy as np
import pandas as pd

# Reproducibility
np.random.seed(42)

# Number of pupils
n_students = 240

# Pupil characteristics
student_id = np.arange(1, n_students + 1)

class_level = np.random.choice(
    ["P5", "P6"],
    size=n_students
)

gender = np.random.choice(
    ["Boy", "Girl"],
    size=n_students
)

# Treatment assignment
treatment = np.random.binomial(
    1,
    0.5,
    n_students
)

attendance_rate = np.random.normal(
    85,
    5,
    n_students
).round(1)

study_hours = np.random.normal(
    6,
    2,
    n_students
).round(1)

# Baseline score
baseline_score = (
    50
    + 0.2 * attendance_rate
    + 0.8 * study_hours
    + np.random.normal(0, 5, n_students)
)

# Program effect
program_effect = treatment * 7

# Endline score
endline_score = (
    baseline_score
    + 4
    + program_effect
    + np.random.normal(0, 4, n_students)
)

# Create baseline observations
baseline = pd.DataFrame({
    "student_id": student_id,
    "class_level": class_level,
    "gender": gender,
    "treatment": treatment,
    "attendance_rate": attendance_rate,
    "study_hours": study_hours,
    "post": 0,
    "time": "baseline",
    "test_score": baseline_score.round(1)
})

# Create endline observations
endline = baseline.copy()

endline["post"] = 1
endline["time"] = "endline"
endline["test_score"] = endline_score.round(1)

# Combine
df = pd.concat(
    [baseline, endline],
    ignore_index=True
)

# Save
df.to_csv(
    "data/synthetic_education_data.csv",
    index=False
)

print(df.head())
print()
print(f"Dataset saved with {len(df)} observations")

df = pd.read_csv("data/synthetic_education_data.csv")
print(df.head())
print(df.shape)

