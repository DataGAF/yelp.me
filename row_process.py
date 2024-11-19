import streamlit as st


def card(business_id: str, business_name: str, main_category: str, sub_category: str, hybrid_score: float, img_url: str, business_url: str, segment: str) -> None:
    detail = f"{main_category} | {sub_category}"
    star = f"Star : {round(hybrid_score,2)} / 5 ⭐"
    st.markdown("<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css'>", unsafe_allow_html=True)
    html_code = f"""
        <div class="card-deck">
            <div class="card bg-dark text-white h-100">
                <a href="{business_url}" target="_self"><img class="card-img-top" height="300px" src="{img_url}" alt="Card image cap"></a>
                <div class="card-body">
                    <h5 class="card-title" style="font-size: 20px;">{business_name}</h5>
                    <a href="/business_page?business_id={business_id}" target="_self"><button class="btn btn-danger">Read More</button></a>
                    <hr>
                    <p class="card-text">Segment : {segment}</p>
                    <p class="card-text"><small>{detail}</small></p>
                    <hr>
                    <p class="card-text"><small>{star}</small></p>
                </div>
            </div>
        </div>"""
    st.markdown(html_code, unsafe_allow_html=True)


def row(key: str, all_data: dict) -> None:
    images_per_page = 5
    num_pages = (len(all_data) + images_per_page - 1) // images_per_page

    page_key = f"page_{key}"

    st.session_state.setdefault(page_key, 0)

    col1, col2, col3 = st.columns([1, 6, 0.5])
    with col1:
        if st.button(key=f"previous_{key}", label="⬅️ Previous") and st.session_state[page_key] > 0:
            st.session_state[page_key] -= 1
    with col3:
        if st.button(key=f"next_{key}", label="Next ➡️") and st.session_state[page_key] < num_pages - 1:
            st.session_state[page_key] += 1

    start_idx = st.session_state[page_key] * images_per_page

    st.write(f"Page {st.session_state[page_key] + 1} / {num_pages}")
    cols = st.columns(images_per_page)
    for idx, data in enumerate(all_data[start_idx: start_idx + images_per_page]):
        with cols[idx % images_per_page]:
            card(**data)
