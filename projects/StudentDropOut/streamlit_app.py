"""Streamlit UI for the student dropout API.

The UI does not load the model itself: it sends the form to the FastAPI service
(predict.py) and shows the answer, so there is only one place that serves the model.

Run:  streamlit run streamlit_app.py      (API must be running on API_URL)
"""

import json
import os
from pathlib import Path

import requests
import streamlit as st

from features import load_data

# 127.0.0.1 rather than localhost: on Windows "localhost" tries IPv6 first, uvicorn listens on IPv4
API_URL = os.getenv("API_URL", "http://127.0.0.1:9696").rstrip("/")
EXAMPLES_DIR = Path(__file__).parent / "examples"
REQUEST_TIMEOUT = 10

PRESETS = {
    "Example: student at risk (real dropout)": "student_at_risk.json",
    "Example: student on track (real graduate)": "student_on_track.json",
}

COURSE_NAMES = {
    33: "Biofuel Production Technologies", 171: "Animation and Multimedia Design",
    8014: "Social Service (evening)", 9003: "Agronomy", 9070: "Communication Design",
    9085: "Veterinary Nursing", 9119: "Informatics Engineering", 9130: "Equinculture",
    9147: "Management", 9238: "Social Service", 9254: "Tourism", 9500: "Nursing",
    9556: "Oral Hygiene", 9670: "Advertising and Marketing Management",
    9773: "Journalism and Communication", 9853: "Basic Education", 9991: "Management (evening)",
}
MARITAL_NAMES = {1: "Single", 2: "Married", 3: "Widower", 4: "Divorced", 5: "Facto union", 6: "Legally separated"}

RISK_STYLE = {
    "low": ("🟢", "Low risk", st.success),
    "medium": ("🟠", "Medium risk", st.warning),
    "high": ("🔴", "High risk", st.error),
}


@st.cache_data
def code_options() -> dict[str, list[int]]:
    """Codes that actually appear in the dataset, for each categorical field."""
    df = load_data()
    fields = ["application_mode", "previous_qualification", "nationality", "mothers_qualification",
              "fathers_qualification", "mothers_occupation", "fathers_occupation"]
    return {f: sorted(int(v) for v in df[f].unique()) for f in fields}


def load_preset(filename: str) -> dict:
    return json.loads((EXAMPLES_DIR / filename).read_text())


def apply_preset() -> None:
    """Copy the chosen example student into the form widgets."""
    for field, value in load_preset(PRESETS[st.session_state.preset]).items():
        st.session_state[field] = value


def yes_no(label: str, key: str, help_text: str | None = None) -> None:
    st.selectbox(label, [1, 0], key=key, format_func=lambda v: "Yes" if v else "No", help=help_text)


def code_select(label: str, key: str, options: list[int], names: dict[int, str] | None = None) -> None:
    names = names or {}
    st.selectbox(label, options, key=key, format_func=lambda v: f"{names[v]} ({v})" if v in names else f"Code {v}")


def background_section(opts: dict[str, list[int]]) -> None:
    st.subheader("Background")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.selectbox("Gender", [0, 1], key="gender", format_func=lambda v: "Male" if v else "Female")
        st.number_input("Age at enrolment", 15, 100, key="age_at_enrollment")
        code_select("Marital status", "marital_status", list(MARITAL_NAMES), MARITAL_NAMES)
    with c2:
        code_select("Nationality", "nationality", opts["nationality"])
        yes_no("International student", "international")
        yes_no("Displaced (studies away from home)", "displaced")
    with c3:
        yes_no("Educational special needs", "special_needs")
        code_select("Mother's qualification", "mothers_qualification", opts["mothers_qualification"])
        code_select("Father's qualification", "fathers_qualification", opts["fathers_qualification"])
    c4, c5 = st.columns(2)
    with c4:
        code_select("Mother's occupation", "mothers_occupation", opts["mothers_occupation"])
    with c5:
        code_select("Father's occupation", "fathers_occupation", opts["fathers_occupation"])


def admission_section(opts: dict[str, list[int]]) -> None:
    st.subheader("Admission and finances")
    c1, c2, c3 = st.columns(3)
    with c1:
        code_select("Course", "course", sorted(COURSE_NAMES), COURSE_NAMES)
        st.selectbox("Attendance", [1, 0], key="daytime_attendance",
                     format_func=lambda v: "Daytime" if v else "Evening")
        code_select("Application mode", "application_mode", opts["application_mode"])
    with c2:
        st.number_input("Application order (0 = first choice)", 0, 9, key="application_order")
        code_select("Previous qualification", "previous_qualification", opts["previous_qualification"])
        st.number_input("Previous qualification grade (0–200)", 0.0, 200.0, step=0.1, key="previous_qualification_grade")
    with c3:
        st.number_input("Admission grade (0–200)", 0.0, 200.0, step=0.1, key="admission_grade")
        yes_no("Tuition fees up to date", "tuition_up_to_date")
        yes_no("Debtor", "debtor")
        yes_no("Scholarship holder", "scholarship_holder")


def semester_section(sem: int) -> None:
    p = f"sem{sem}_"
    st.subheader(f"{'First' if sem == 1 else 'Second'} semester")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.number_input("Units enrolled", 0, 60, key=p + "enrolled")
        st.number_input("Units approved (passed)", 0, 60, key=p + "approved")
    with c2:
        st.number_input("Units credited", 0, 60, key=p + "credited")
        st.number_input("Evaluations taken", 0, 100, key=p + "evaluations")
    with c3:
        st.number_input("Average grade (0–20)", 0.0, 20.0, step=0.1, key=p + "grade")
        st.number_input("Units without evaluations", 0, 60, key=p + "without_evaluations")


def economy_section() -> None:
    st.subheader("Economy in the year of enrolment")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.number_input("Unemployment rate (%)", 0.0, 100.0, step=0.1, key="unemployment_rate")
    with c2:
        st.number_input("Inflation rate (%)", -50.0, 100.0, step=0.1, key="inflation_rate")
    with c3:
        st.number_input("GDP growth", -50.0, 50.0, step=0.01, key="gdp")


def collect_payload(fields: list[str]) -> dict:
    return {f: st.session_state[f] for f in fields}


def call_api(payload: dict) -> tuple[dict | None, str | None]:
    """Return (prediction, error message)."""
    try:
        response = requests.post(f"{API_URL}/predict", json=payload, timeout=REQUEST_TIMEOUT)
    except requests.RequestException:
        return None, f"Could not reach the prediction API at {API_URL}. Is the service running?"
    if response.status_code == 422:
        problems = [f"{'.'.join(str(p) for p in e['loc'][1:])}: {e['msg']}" for e in response.json()["detail"]]
        return None, "The API rejected some inputs:\n\n- " + "\n- ".join(problems)
    if response.status_code != 200:
        return None, f"The API returned an error (HTTP {response.status_code})."
    return response.json(), None


def show_result(result: dict, payload: dict) -> None:
    icon, label, box = RISK_STYLE[result["risk_level"]]
    probability = result["dropout_probability"]
    box(f"{icon} **{label}**: estimated dropout probability **{probability:.0%}**")
    st.progress(min(max(probability, 0.0), 1.0))

    c1, c2, c3 = st.columns(3)
    c1.metric("Dropout probability", f"{probability:.1%}")
    c2.metric("Decision threshold", f"{result['threshold']:.1%}")
    c3.metric("Flagged as at risk", "Yes" if result["dropout_risk"] else "No")

    def semester_summary(sem: int) -> str:
        enrolled, approved = payload[f"sem{sem}_enrolled"], payload[f"sem{sem}_approved"]
        if not enrolled:
            return f"semester {sem}: no units enrolled"
        return f"semester {sem}: passed {approved} of {enrolled} units ({approved / enrolled:.0%})"

    tuition = "up to date" if payload["tuition_up_to_date"] else "NOT up to date"
    st.caption(
        f"Context: {semester_summary(1)}; {semester_summary(2)}; tuition fees {tuition}. "
        "These are the strongest signals the model learned from the data."
    )


def main() -> None:
    st.set_page_config(page_title="Student Dropout Risk", page_icon="🎓", layout="wide")
    st.title("🎓 Student Dropout Risk")
    st.write("Fill in a student's end-of-first-year data and get an estimated dropout risk. "
             "Start from one of the real example students in the sidebar and change any field.")

    fields = list(load_preset(PRESETS[next(iter(PRESETS))]))
    if "preset" not in st.session_state:
        st.session_state.preset = next(iter(PRESETS))
        apply_preset()

    with st.sidebar:
        st.header("Start from an example")
        st.radio("Example student", list(PRESETS), key="preset", on_change=apply_preset)
        st.divider()
        st.caption(f"API: `{API_URL}`")
        try:
            healthy = requests.get(f"{API_URL}/health", timeout=3).ok
        except requests.RequestException:
            healthy = False
        st.write("API status:", "🟢 online" if healthy else "🔴 offline")

    opts = code_options()
    with st.form("student"):
        tab1, tab2, tab3 = st.tabs(["Student", "Academic record", "Economy"])
        with tab1:
            background_section(opts)
            admission_section(opts)
        with tab2:
            semester_section(1)
            semester_section(2)
        with tab3:
            economy_section()
        submitted = st.form_submit_button("Predict dropout risk", type="primary", use_container_width=True)

    if submitted:
        payload = collect_payload(fields)
        with st.spinner("Asking the model..."):
            result, error = call_api(payload)
        if error:
            st.error(error)
        else:
            show_result(result, payload)


if __name__ == "__main__":
    main()
