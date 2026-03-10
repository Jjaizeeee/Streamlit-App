import streamlit as st
import pandas as pd
from datetime import date, time

st.set_page_config(page_title="StudyBuddy Planner", page_icon="📚", layout="wide")

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("📚 StudyBuddy Planner")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Student Profile", "Study Planner", "Habit Tracker", "Results", "About"]
)

# -----------------------------
# HOME
# -----------------------------
if page == "Home":
    st.title("📚 StudyBuddy Planner")
    st.subheader("Your simple student study planner and habit tracker")
    st.markdown("""
    Welcome to **StudyBuddy Planner**.  
    This app helps students organize their study schedule, track habits, and receive a simple personalized study recommendation.
    """)
    st.info("Use the sidebar to navigate through the app.")
    st.caption("Demo app for Streamlit UI requirements")

    col1, col2, col3 = st.columns(3)
    col1.metric("Subjects Supported", "10+")
    col2.metric("Planner Status", "Ready")
    col3.metric("UI Components", "20+")

    with st.expander("Why use this app?"):
        st.write("""
        - Helps students stay organized
        - Encourages habit tracking
        - Easy to use and beginner-friendly
        """)

# -----------------------------
# STUDENT PROFILE
# -----------------------------
elif page == "Student Profile":
    st.header("👤 Student Profile")

    name = st.text_input("Enter your name")
    bio = st.text_area("Short introduction about yourself")
    age = st.number_input("Age", min_value=10, max_value=60, value=18)
    year_level = st.selectbox("Year Level", ["Senior High", "1st Year", "2nd Year", "3rd Year", "4th Year"])
    gender = st.radio("Gender", ["Male", "Female", "Prefer not to say"])
    subjects = st.multiselect(
        "Select your subjects",
        ["Math", "Science", "English", "Programming", "Statistics", "Database", "Networking", "History"]
    )
    favorite_color = st.color_picker("Pick your favorite theme color", "#4CAF50")
    profile_pic = st.file_uploader("Upload a profile image (optional)", type=["png", "jpg", "jpeg"])
    accepted = st.checkbox("I confirm that the information above is correct")

    if accepted:
        st.success("Profile saved successfully!")

# -----------------------------
# STUDY PLANNER
# -----------------------------
elif page == "Study Planner":
    st.header("🗓️ Study Planner")

    study_goal = st.text_input("What is your main study goal?")
    exam_date = st.date_input("Exam / Deadline Date", value=date.today())
    preferred_start = st.time_input("Preferred Study Start Time", value=time(19, 0))
    study_hours = st.slider("How many hours can you study per day?", 1, 12, 3)
    focus_level = st.slider("Current focus level", 1, 10, 5)
    learning_style = st.selectbox(
        "Preferred learning style",
        ["Reading", "Watching videos", "Practice problems", "Group study", "Flashcards"]
    )
    available_days = st.multiselect(
        "Available study days",
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    )
    use_timer = st.toggle("Enable Pomodoro suggestion")
    notes = st.text_area("Additional notes")

    tab1, tab2 = st.tabs(["Daily Plan", "Tips"])

    with tab1:
        st.subheader("Suggested Daily Plan")
        if study_hours <= 2:
            st.write("Light study load: 25-min focus sessions with 5-min breaks.")
        elif study_hours <= 5:
            st.write("Balanced plan: 45-min focus sessions with 10-min breaks.")
        else:
            st.write("Heavy study load: 50-min focus sessions with 10-min breaks, plus a long break.")

        if use_timer:
            st.info("Pomodoro mode enabled: Recommended 25 minutes study + 5 minutes break.")

    with tab2:
        st.subheader("Study Tips")
        st.markdown("""
        - Study difficult subjects first
        - Avoid multitasking
        - Keep your phone away during focus time
        - Review before sleeping
        """)

# -----------------------------
# HABIT TRACKER
# -----------------------------
elif page == "Habit Tracker":
    st.header("📈 Habit Tracker")

    sleep_hours = st.slider("Sleep hours last night", 0, 12, 7)
    water_intake = st.number_input("Glasses of water today", min_value=0, max_value=20, value=5)
    mood = st.selectbox("Current mood", ["Excellent", "Good", "Neutral", "Tired", "Stressed"])
    exercise = st.checkbox("Did you exercise today?")
    reviewed_notes = st.checkbox("Did you review your notes today?")
    phone_distraction = st.radio("Phone distraction level", ["Low", "Medium", "High"])

    progress_value = 0
    if sleep_hours >= 7:
        progress_value += 25
    if water_intake >= 6:
        progress_value += 25
    if exercise:
        progress_value += 25
    if reviewed_notes:
        progress_value += 25

    st.subheader("Today's Progress")
    st.progress(progress_value)

    if progress_value >= 75:
        st.success("Great job! You are maintaining strong habits.")
    elif progress_value >= 50:
        st.warning("You're doing okay, but there is still room for improvement.")
    else:
        st.error("Try improving your rest, hydration, and study habits.")

# -----------------------------
# RESULTS
# -----------------------------
elif page == "Results":
    st.header("📊 Results Summary")

    st.write("Click the button below to generate a demo summary.")
    if st.button("Generate Summary"):
        st.balloons()

        summary_data = {
            "Category": ["Focus", "Discipline", "Health", "Readiness"],
            "Score": [8, 7, 6, 8]
        }

        df = pd.DataFrame(summary_data)
        st.dataframe(df, use_container_width=True)

        st.markdown("### Personalized Recommendation")
        st.write("""
        Based on your input, you should focus on building a consistent study schedule,
        improving sleep, and using your preferred learning style more often.
        """)

        report_text = """
StudyBuddy Planner Report

This student shows good readiness for studying.
Recommended actions:
- Keep a fixed study time
- Improve sleeping habits
- Continue reviewing notes daily
- Use practice problems and active recall
        """

        st.download_button(
            label="Download Report",
            data=report_text,
            file_name="studybuddy_report.txt",
            mime="text/plain"
        )

# -----------------------------
# ABOUT
# -----------------------------
elif page == "About":
    st.header("ℹ️ About This App")

    st.markdown("""
    ### What the app does
    **StudyBuddy Planner** helps students plan their study routine, track daily habits, and receive simple study recommendations.

    ### Target user
    The target users are **students**, especially those who want to manage their time better and improve academic performance.

    ### Inputs collected
    The app collects:
    - Personal profile information
    - Subjects
    - Study hours
    - Learning style
    - Schedule preferences
    - Sleep, mood, hydration, and habit data

    ### Outputs shown
    The app shows:
    - A suggested study plan
    - Habit progress
    - Summary table
    - Personalized recommendations
    """)

    st.info("This app is for educational demonstration purposes only.")
