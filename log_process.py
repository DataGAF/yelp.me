
from firebase_admin import credentials, firestore
from datetime import datetime
from config import service_key
from pytz import timezone

import streamlit as st
import firebase_admin
import uuid
import json


def firebase_initialize() -> None:
    if "firebase_app" not in st.session_state:
        try:
            cred = credentials.Certificate(json.loads(service_key))
            st.session_state.firebase_app = firebase_admin.initialize_app(cred)
        except:
            pass


def user_log(subject: str, message: dict):
    firebase_initialize()
    if "id_user" not in st.session_state:
        st.session_state.setdefault("id_user", str(uuid.uuid4()))

    db = firestore.client()
    turkey_timezone = timezone("Europe/Istanbul")
    log_time = datetime.now(turkey_timezone).strftime("%Y-%m-%d %H:%M:%S")
    db.collection("user_logs").add({
        "id_user": st.session_state["id_user"],
        "subject": subject,
        "action_time": log_time,
        "message": message
    })
