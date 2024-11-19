import pandas as pd
import streamlit as st
import warnings

warnings.filterwarnings('ignore')


@st.cache_data
def load_data():
    user_recommend = pd.read_csv("data/user_recommend.csv")
    business_predict = pd.read_csv("data/business_predict.csv")
    return user_recommend, business_predict


@st.cache_data
def top10_business() -> list[dict]:
    df_top10_business = pd.read_csv("data/top10_business.csv")
    return df_top10_business.to_dict("records")


def user_recommend() -> dict:
    user_recommend, _ = load_data()

    df_user_filter = user_recommend[["user_name", "user_id"]].drop_duplicates()
    df_user_filter.set_index("user_name", inplace=True)

    sc = st.session_state.get("select_user", None)
    if sc:
        user_recommend = user_recommend[user_recommend["user_name"].isin([sc])]

    data = {}
    data["user"] = df_user_filter.squeeze().to_dict()
    data["business"] = user_recommend[user_recommend.columns.tolist()[:-2]].to_dict("records")
    return data


def business_predict() -> list[dict]:
    _, business_predict = load_data()
    sc = st.session_state.get("select_user", None)
    if sc:
        business_predict = business_predict[business_predict["user_name"].isin([sc])]

    return business_predict[business_predict.columns.tolist()[:-4]].to_dict("records")


@st.cache_data
def business_detail(business_id: str) -> list[dict]:
    df_business_detail = pd.read_csv("data/business_detail.csv")
    df_business_detail.set_index("business_id", inplace=True)
    return df_business_detail.to_dict("index")[business_id]


@st.cache_data
def business_review_sorting(business_id: str) -> pd.DataFrame:
    df_review_sorting = pd.read_csv("data/business_review_sorting.csv")
    return edit_user_data(df_review_sorting, business_id)


@st.cache_data
def tips_segment(business_id: str) -> pd.DataFrame:
    df_tips_segment = pd.read_csv("data/tips_sentiment.csv")
    return edit_user_data(df_tips_segment, business_id)


@st.cache_data
def emotion_segment(business_id: str) -> pd.DataFrame:
    df_emotion = pd.read_csv("data/emotion_segment.csv")
    df_emotion = df_emotion[df_emotion["business_id"] == business_id]
    most_angry, most_joyful, most_sad = df_emotion.groupby("business_id").mean().iloc[0]
    emotions = {"Most Angry": [most_angry, "😡"], "Most Joyful": [most_joyful, "🏆"], "Most Sad": [most_sad, "😢"]}
    return emotions


@st.cache_data
def time_series(business_id: str) -> pd.DataFrame:
    df_time_series = pd.read_csv("data/time_series.csv")
    df_time_series = df_time_series[df_time_series["business_id"] == business_id][["date", "avg_polarity_score"]]
    df_time_series.interpolate(method="linear", inplace=True)
    df_time_series["date"] = pd.to_datetime(df_time_series["date"])
    df_time_series.set_index("date", inplace=True)
    return df_time_series


@st.cache_data
def term_freq(business_id: str) -> pd.DataFrame:
    df_term_freq = pd.read_csv("data/term_frequencies.csv")
    df_term_freq = df_term_freq[df_term_freq["business_id"] == business_id]
    return df_term_freq


@st.cache_data
def filter_data(data: pd.DataFrame, category_selection: str | None = None, subcategory_selection: str | None = None, cagegory_col="main_category", sub_category_col="sub_category") -> pd.DataFrame:
    dataframe = pd.DataFrame(data)
    dataframe = dataframe[dataframe[cagegory_col].isin(category_selection)]

    if subcategory_selection:
        dataframe = dataframe[dataframe[sub_category_col].isin(subcategory_selection)]

    return dataframe.to_dict("records")


@st.cache_data
def edit_user_data(data: pd.DataFrame, business_id: str) -> pd.DataFrame:
    df = pd.DataFrame(data)
    df["user_id"] = df["user_id"].str[:3] + "**"
    return df[df["business_id"] == business_id].set_index("user_id").iloc[:, 1:]
