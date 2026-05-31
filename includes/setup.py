import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

OXFORD_BLUE = "#002147"
CLINICAL_RED = "#C73E3A"
ACCENT_BLUE = "#3A7CA5"

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"

columns = [
    "age","sex","cp","trestbps","chol","fbs","restecg",
    "thalach","exang","oldpeak","slope","ca","thal","num"
]

df = pd.read_csv(url, header=None, names=columns, na_values="?")
df["heart_disease"] = np.where(
    df["num"] == 0,
    "No Heart Disease",
    "Heart Disease"
)