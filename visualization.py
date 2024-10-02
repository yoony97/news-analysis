# visualization.py
import streamlit as st
import pandas as pd
from pymongo import MongoClient

def load_data():
    client = MongoClient(host='localhost', port=27017)
    db = client['project1']
    collection = db['NewsAnalysis']
    data = list(collection.find())
    sentiments = []
    for item in data:
        for sentiment in item['sentiments']:
            sentiment['seendate'] = item['seendate']
            sentiments.append(sentiment)
    df = pd.DataFrame(sentiments)
    df['seendate'] = pd.to_datetime(df['seendate'])
    return df

def main():
    st.title("기업별 날짜에 따른 감성 지수 변화")
    df = load_data()
    organizations = df['organization'].unique()
    organization = st.selectbox("기업을 선택하세요", organizations)
    selected_df = df[df['organization'] == organization].set_index('seendate')
    st.line_chart(selected_df[['positive', 'negative', 'neutral']])

if __name__ == "__main__":
    main()
