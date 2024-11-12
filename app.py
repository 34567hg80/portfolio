import streamlit as st

# Sidebar/Profile section
st.sidebar.image("pic.jpg", width=150)  # Replace with your profile picture path
st.sidebar.title("Hritesh Ghosh")
st.sidebar.write("Kolkata, India")
st.sidebar.write("📞 +91 7908383263")
st.sidebar.write("✉️ ghoshhritesh@gmail.com")
st.sidebar.write("🔗 [LinkedIn](https://linkedin.com/in/hritesh80)")

# About Section
st.title("Hritesh Ghosh")
st.write("Bachelor of Technology | Computer Science Engineering | Data Enthusiast")
st.write("Based in Kolkata, India")
st.write(
    "I am an aspiring data scientist and developer, skilled in predictive modeling, analysis, process automation, and data visualization. My goal is to apply my technical skills to real-world challenges."
)

# Skills Section
st.header("Skills")
st.write("**Languages**: Python, SQL, JavaScript")
st.write("**Frameworks**: Pandas, NumPy, Matplotlib, Seaborn, Plotly, scikit-learn, Streamlit, QT5, NodeJS")
st.write("**Tools**: PowerBI, Excel, PowerPoint, MySQL, SQLite, AWS, Git, NPM")
st.write("**Soft Skills**: Rapport Building, Strong Stakeholder Management, People Management, Excellent Communication")

# Experience Section
st.header("Experience")

st.subheader("GroIntern - Intern")
st.write("Bhubaneswar, Odisha | June 2023 - August 2023")
st.write("""
- Built dashboards with Dash and Power BI to visualize core KPIs, saving 10 hours weekly.
- Aggregated data from 100+ sources to build structured databases, driving a 70% increase in new product revenue.
- Designed pandas DataFrame to generate Excel reports, aiding stakeholder understanding for a product scaling to 10,000 daily active users.
""")

st.subheader("Accenture - Developer Program")
st.write("Remote | July 2022 - August 2022")
st.write("""
- Completed modules on requirements, design, cloud scaling, debugging, and testing, enhancing productivity by 10x.
- Demonstrated expertise in IAM policies, SDLC security, problem shaping, and data privacy for 200 new requirements.
""")

st.subheader("KIIT - Undergraduate Research Assistant")
st.write("Bhubaneswar, Odisha | January 2022 - June 2022")
st.write("""
- Developed a REST API to test the model and used DynamoDB for data storage, achieving 97% more efficiency.
- Gained experience in requirements gathering, design, cloud scaling, debugging, and unit testing.
""")

# Projects Section
st.header("Projects")

st.subheader("Nafisa_AI")
st.write("2023 - 2024")
st.write("""
- Developed a StreamLite-based app incorporating Google Gemini LLM model for human-like chat interactions, with over 50+ data points.
- Achieved caching prompts five times more efficiently than ChatGPT 4, enhancing performance and responsiveness.
""")

st.subheader("nDed - The Lightweight Browser")
st.write("2022 - 2023")
st.write("""
- Developed a privacy-focused browser optimized for legacy systems and ARM-based boards, ensuring minimal memory usage and performance.
- Integrated WebKIT APIs and PyQt for a user-friendly, efficient browsing experience with strong privacy features.
""")

# Publications Section
st.header("Publications")
st.write("**Smart Garbage Collection System for Indian Municipal Solid Waste**")
st.write("Published in *Frontiers of Intelligent Computing: Theory and Applications (FICTA)*, 10th International Conference, Hosted by NIT Mizoram.")

# Certifications Section
st.header("Certifications")
st.write("- **Python for Data Science (IBM)** - Mastered Python basics, control flow, loops, functions, data structures, and logical capabilities.")
st.write("- **SQL and Relational Databases 101 (IBM)** - Learned data ecosystem, relational databases, and data cleaning techniques.")

st.markdown("---")
st.write("**Connect with me on LinkedIn or reach out via email!**")
