import pandas as pd
import requests
import tldextract
import whois
from sklearn.ensemble import RandomForestClassifier


data = pd.read_csv('urls_dataset.csv')

def extract_features(url):
    features = {}
    features['length'] = len(url)
    features['has_at'] = '@' in url
    features['num_dots'] = url.count('.')
    features['has_https'] = url.startswith('https://')

    
    try:
        w = whois.whois(url)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if creation_date is None:
            features['domain_age'] = 0
        else:
            features['domain_age'] = (pd.Timestamp.now() - pd.to_datetime(creation_date)).days
    except Exception:
        features['domain_age'] = 0
    return features


df_features = data['url'].apply(extract_features)
features_df = pd.DataFrame(df_features.tolist())


features_df = features_df.apply(pd.to_numeric, errors='coerce').fillna(0)


X = features_df
y = data['label']


model = RandomForestClassifier()
model.fit(X, y)


input_url = 'http://example-phish.com/login'
input_features = extract_features(input_url)
input_features_df = pd.DataFrame([input_features])
input_features_df = input_features_df.apply(pd.to_numeric, errors='coerce').fillna(0)

result = model.predict(input_features_df)

if result[0] == 1:
    print("Phishing detected!")
else:
    print("Website is safe.")

def check_phishtank(url):
    response = requests.get(f'https://checkurl.phishtank.com/checkurl/?url={url}')
    print(response.status_code)    
    print(response.text)           
   
    if response.text.strip():
        try:
            print(response.json())
        except Exception as e:
            print("JSON decode failed:", e)
    else:
        print("Empty response from PhishTank API.")