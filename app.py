import streamlit as st

def main():
    st.set_page_config(
        page_title="Anthony Lee's Resume",
        page_icon=":memo:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Set CSS styles
    st.markdown(
        """
        <style>
        .content-section {
            padding: 1em;
            background-color: #2E5A88;
            border-radius: 0.5rem;
            color: white;
            transition: all 0.5s ease-in-out;
        }

        .content-section:hover {
            background-color: #54b3d6;
            color: white;
            box-shadow: 0 0 0 5px #54b3d6;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # Header section
    st.title("Anthony Lee's Resume")

    # Contact Information grid
    contact_col1, contact_col2 = st.columns(2)
    with contact_col1:
        st.image("cropped_image.png", width=200)

    with contact_col2:
        st.subheader("Contact Information")
      
        st.write("Email: alee97422@gmail.com")

        st.subheader("Social Media")
        st.write("LinkedIn: [Anthony Lee](www.linkedin.com/in/anthony-lee97422)")
        st.write("GitHub: [alee97422](https://github.com/alee97422)")

    # Skills grid
    st.subheader("Skills")
    skills_col1, skills_col2 = st.columns(2)
    with skills_col1:
        st.markdown(
            """
            <div class="content-section">
                <h3>Technical skills</h3>
                <ul>
                    <li>Computer repair and troubleshooting</li>
                    <li>Cell phone repair</li>
                    <li>Game system repair</li>
                    <li>Customer service</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with skills_col2:
        st.markdown(
            """
            <div class="content-section">
                <h3>Professional skills</h3>
                <ul>
                    <li>Data analysis</li>
                    <li>PC and cell repair tech</li>
                    <li>Software programming</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Experience grid
    st.subheader("Experience")
    exp_col1, exp_col2 = st.columns(2)
    with exp_col1:
        st.markdown(
            """
            <div class="content-section">
                <h3>Professional Experience</h3>
                <ul>
                    <li>Synergy3 tech services (Feb 2018 - Jan 2019)</li>
                    <li>Walmart Distribution Center 6082 (Jan 2019 - August 2020)</li>
                    <li>Asurion (September 2020 - July 2021)</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with exp_col2:
        st.markdown(
            """
            <div class="content-section">
                <h3>Education</h3>
                <ul>
                    <li>Little Rock Adult Education Center (November 2012)</li>
                    <li>Vista College (2018)</li> 
                    <li>Coursera Certificates (2021)</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            """,
            unsafe_allow_html=True
        )

    # Coursera certificates section
    st.markdown(
        """
        <div style="text-align: center;">
            <h4>Coursera Certificates</h4>
            <p>You can find my Coursera certificates <a href="https://www.coursera.org/user/e628f8317b0882fcdbfdfda00198c563">here</a>.</p>
         </div>
         <div style="text-align: center;">
            <p>I am actively working on expanding my skills and learning more in my free time.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
