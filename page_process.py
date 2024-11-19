import streamlit as st
from row_process import row
import data_process as dp
from log_process import user_log
from config import image_home_url, user_default_image, gif1, gif2, gif3, gif4
from streamlit_folium import st_folium
import folium
import base64


def markdown(content, tag="div", style="", link=None) -> None:
    html_content = f"<{tag} style='{style}'>{content}</{tag}>"
    if link:
        html_content = f"<a href='{link}' target='_self'>{html_content}</a>"
    st.markdown(f"<center>{html_content}</center>", unsafe_allow_html=True)


def page_initialize() -> None:
    st.set_page_config(layout="wide", page_title="YELP ME", initial_sidebar_state="collapsed", page_icon="logo.png")

    with open("tag.png", "rb") as image_file:
        tag_image = base64.b64encode(image_file.read()).decode()

    with open("logo.png", "rb") as image_file:
        logo_image = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; height: 10vh; padding: 0 10px;">
            <div style="flex: 1; text-align: center;">
                <img src="data:image/png;base64,{tag_image}" alt="Tag Image" style="max-width: 100%; height: auto;">
            </div>
            <div style="flex: 0; text-align: right;">
                <img src="data:image/png;base64,{logo_image}" alt="Logo Image" style="max-width: 180px; height: auto;">
            </div>
        </div>
        """, unsafe_allow_html=True)


def page_top10_business() -> None:
    markdown("Top 10 Businesses and Events", "h4", "text-align: left; color: white;")
    st.divider()
    row("top10_business", dp.top10_business())
    st.divider()


def page_user_recommend() -> None:
    markdown("Discover Your Perfect Match", "h4", "text-align: left; color: white;")

    st.session_state.setdefault("prev_user", "Karen")
    st.session_state.setdefault("select_user", "Karen")

    user_dict, business_dict = dp.user_recommend()["user"], dp.user_recommend()["business"]

    selected_user = st.sidebar.selectbox("Select User :", options=list(user_dict.keys()), key="select_user")
    if selected_user not in ["Steven", "Ken"]:
        st.sidebar.markdown(f"<div style='display: flex; align-items: center;'><img src='{image_home_url}/{user_dict[selected_user]}/ls.jpg' width='80' height='80' style='margin-right: 10px;'/><span>{selected_user}</span></div>", unsafe_allow_html=True)
    else:
        st.sidebar.markdown(f"<div style='display: flex; align-items: center;'><img src='{user_default_image}' width='80' height='80' style='margin-right: 10px;'/><span>{selected_user}</span></div>", unsafe_allow_html=True)

    st.sidebar.divider()

    main_category_list = list({i["main_category"] for i in business_dict})
    st.session_state.setdefault("prev_main_category", main_category_list)
    st.session_state.setdefault("select_main_category", main_category_list)

    selected_main_categories = st.sidebar.multiselect("Select Main Category :", options=main_category_list, default=main_category_list, key="select_main_category")

    business_dict = dp.filter_data(dp.user_recommend()["business"], selected_main_categories)

    st.sidebar.divider()

    sub_category_list = list({i["sub_category"] for i in business_dict})
    st.session_state.setdefault("prev_sub_category", sub_category_list)
    st.session_state.setdefault("select_sub_category", sub_category_list)

    selected_subcategories = st.sidebar.multiselect("Select Sub Category :", options=sub_category_list, default=sub_category_list, key="select_sub_category")

    business_dict = dp.filter_data(business_dict, selected_main_categories, selected_subcategories)
    row("user_recommend", business_dict)
    st.divider()

    select_control = (selected_user != st.session_state["prev_user"]) or (selected_main_categories != st.session_state["prev_main_category"]) or (selected_subcategories != st.session_state["prev_sub_category"])
    if select_control:
        user_log("user_recommend", {"selected_user": selected_user, "selected_main_categories": selected_main_categories, "selected_sub_categories": selected_subcategories})
        st.session_state["prev_user"] = selected_user
        st.session_state["prev_main_category"] = selected_main_categories
        st.session_state["prev_sub_category"] = selected_subcategories


def page_business_predict() -> None:
    markdown("Business Predict For User", "h4", "text-align: left; color: white;")

    st.session_state.setdefault("prev_business", "Old St Louis Chop Suey")
    st.session_state.setdefault("select_business", "Old St Louis Chop Suey")

    business_dict = dp.business_predict()

    selected_business = st.selectbox("Select Business :", options=[i["business_name"] for i in business_dict], key="select_business")
    business_dict = dp.filter_data(business_dict, [selected_business], cagegory_col="business_name")

    get_data = business_dict[0]
    get_gif = select_gif(get_data["liked_proba"])
    col1, col2, col3 = st.columns(3)

    with col1:
        markdown(content=f"<img src='{get_data['img_url']}' style='width:500px; height:400px;'>", style="", link=get_data["business_url"])
    with col2:
        markdown(get_data["business_name"], "h2")
        markdown(f"Segment : {get_data['segment']}", "h4")
        markdown(f"{round(get_data['hybrid_score'], 2)} / 5 ⭐", "h4")
        markdown(f"Liking Probality Score : {round(get_data['liked_proba'], 3)}", "h4")
        markdown(f"<img src='{get_gif}' style='width:200px; height:200px;'>", "div")

        st.write("")
        markdown(f"<a href=/business_page?business_id={get_data['business_id']} target='_self'><button class='btn btn-danger'>Read More</button></a>", "div")
    with col3:
        m = folium.Map(location=[get_data["latitude"], get_data["longitude"]], zoom_start=7)
        folium.Marker(location=[get_data["latitude"], get_data["longitude"]], popup=get_data["business_name"], icon=folium.Icon(color="blue", icon="info-sign")).add_to(m)
        st_folium(m, width=600, height=400)

    select_control = selected_business != st.session_state["prev_business"]
    if select_control:
        user_log("business_predict", {"selected_business": selected_business})
        st.session_state["prev_business"] = selected_business


def select_gif(liked_score: float) -> str:
    if liked_score >= 0.90:
        return gif1
    elif liked_score >= 0.80:
        return gif2
    elif liked_score >= 0.70:
        return gif3
    else:
        return gif4
