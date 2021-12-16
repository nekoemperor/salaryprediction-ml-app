from numpy.lib.npyio import load
import pandas as pd

def load_data():
    df = pd.read_csv("./salaryprediction/data/survey_results_public_2021.csv")
    return df


def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_experience(x):
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)


def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'


def clean_data(df):
    df = df[[
        "Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"
    ]]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)

    df = df[df["Salary"].notnull()]

    df = df.dropna()

    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)

    country_map = shorten_categories(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(country_map)

    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df['Country'] != 'Other']

    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)

    df['EdLevel'] = df['EdLevel'].apply(clean_education)

    return df


if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    print(df.head(10))
