from log_process import user_log
import streamlit as st
import page_process as pp
import data_process as dp
import base64
import altair as alt
import matplotlib.pyplot as plt

pp.page_initialize()

business_id = st.query_params.get("business_id", None)


def detail_row1() -> None:
    pp.markdown("<br><br><br>")
    col1, col2, col3 = st.columns(3)

    with col1:
        data = dp.business_detail(business_id)
        pp.markdown(f"<img src='{data['img_url']}' style='width:600px; height:375px;'>", "center")
    with col2:
        pp.markdown(f"<h2>{data['business_name']}</h2>", "center")
        st.write("")
        st.write("")
        pp.markdown("<h5>Address | City | State</h5>", "center")
        pp.markdown(f"<h5>{data['address']} | {data['city']} | {data['state']}</h5>", "center")
        pp.markdown(f"<h4>{round(data['hybrid_score'], 2)} / 5 ⭐</h4>", "center")

        emotions = dp.emotion_segment(business_id)
        most_emotion = max(emotions, key=lambda x: emotions[x][0])
        st.markdown(f"<center>Customer Emotion is: {most_emotion} {round(emotions[most_emotion][0],3)} {emotions[most_emotion][1]}</center>", unsafe_allow_html=True)

    with col3:
        with open(f"wordcloud/{business_id}.png", "rb") as image_file:
            tag_image = base64.b64encode(image_file.read()).decode()
        st.markdown(f"""<img src="data:image/png;base64,{tag_image}" alt="Logo Image" style="width:600px; height:375px;" />""", unsafe_allow_html=True)
    user_log("business_detail", {"selected_business": data["business_name"]})


def detail_row2() -> None:
    pp.markdown("<br><br><br>")
    col1, col2 = st.columns([0.7, 0.5])

    with col1:
        pp.markdown("Review Table", "h4", "text-align: center; color: white;")
        st.dataframe(dp.business_review_sorting(business_id), column_config={"name": "App name", "stars": st.column_config.NumberColumn("stars", format="%d ⭐")})

    with col2:
        pp.markdown("User Advice", "h4", "text-align: center; color: white;")
        st.write(dp.tips_segment(business_id))


def detail_row3() -> None:
    col1, col2 = st.columns([0.6, 0.5])

    with col1:
        pp.markdown("<br><br><br>")
        pp.markdown("Time Series with Sentiments", "h4", "text-align: center; color: white;")
        chart = (alt.Chart(dp.time_series(business_id).reset_index()).mark_line().encode(x="date:T", y="avg_polarity_score:Q").properties(width=600, height=800))
        st.altair_chart(chart, use_container_width=True)

    with col2:
        pp.markdown("<br><br><br>")
        pp.markdown("Top 10 Frequently Words", "h4", "text-align: center; color: white;")
        text_color = "white"
        bg_color = "#0E1117"

        data = dp.term_freq(business_id)
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.barh(data['words'], data['tf'], color='skyblue')
        ax.set_xlabel('Word Frequency', color=text_color)
        ax.set_ylabel('Words', color=text_color)

        fig.patch.set_facecolor(bg_color)
        ax.set_facecolor(bg_color)
        ax.tick_params(axis='x', colors=text_color)
        ax.tick_params(axis='y', colors=text_color)

        st.pyplot(fig)


if business_id:
    detail_row1()
    detail_row2()
    detail_row3()
else:
    st.error("Please select an item on main page")
