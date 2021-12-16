from sklearn.preprocessing import LabelEncoder

def label_encoder(df):
    le_education = LabelEncoder()
    le_country = LabelEncoder()
    le_education.fit(df['EdLevel'])
    le_country.fit(df['Country'])

    return [le_education, le_country]
