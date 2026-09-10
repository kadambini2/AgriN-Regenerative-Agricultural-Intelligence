
import streamlit as st
import pandas as pd
import requests
import plotly.graph_objects as go
import plotly.express as px

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AgriN | Regenerative Agricultural Intelligence",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PREMIUM UI
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #f5f8f5;
}

header, footer, #MainMenu {
    visibility: hidden;
}

.block-container {
    max-width: 1450px;
    padding: 28px 45px;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e7eee9;
}

.brand {
    font-size: 30px;
    font-weight: 800;
    color: #123d2d;
}

.brand span {
    color: #36a66d;
}

.subtitle {
    font-size: 10px;
    color: #89958e;
    letter-spacing: 1px;
    margin-bottom: 25px;
}

/* HERO */

.hero {
    min-height: 320px;
    border-radius: 28px;
    padding: 42px;
    color: white;

    background:
        linear-gradient(
            90deg,
            rgba(5,54,35,0.94),
            rgba(12,85,54,0.72),
            rgba(12,85,54,0.12)
        ),
        url("https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1800&q=85");

    background-size: cover;
    background-position: center;

    box-shadow: 0 15px 40px rgba(30,80,50,0.15);
}

.hero h1 {
    font-size: 45px;
    line-height: 1.05;
    margin: 12px 0;
}

.hero p {
    max-width: 620px;
    color: #e4f2e9;
    font-size: 16px;
}

.hero-label {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #ccebd9;
}

.location {
    display: inline-block;
    margin-top: 15px;
    padding: 9px 17px;
    border-radius: 30px;
    background: rgba(255,255,255,0.16);
}

/* SECTION */

.section {
    color: #153d2d;
    font-size: 25px;
    font-weight: 800;
    margin: 30px 0 18px;
}

/* CARDS */

.card {
    background: white;
    border: 1px solid #e6eee8;
    border-radius: 20px;
    padding: 23px;
    margin-bottom: 18px;
    box-shadow: 0 7px 25px rgba(30,70,45,0.055);
}

.card h3 {
    color: #153d2d;
}

.metric-card {
    background: white;
    border: 1px solid #e6eee8;
    border-radius: 20px;
    padding: 20px;
    min-height: 125px;
    box-shadow: 0 7px 25px rgba(30,70,45,0.055);
}

.icon {
    width: 44px;
    height: 44px;
    border-radius: 14px;
    background: #eaf7ef;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
}

.number {
    color: #153d2d;
    font-size: 31px;
    font-weight: 800;
    margin-top: 8px;
}

.label {
    color: #7c8780;
    font-size: 12px;
}

/* AI CARD */

.ai-card {
    background: linear-gradient(135deg, #0d402e, #21855a);
    color: white;
    padding: 28px;
    border-radius: 23px;
    min-height: 235px;
    box-shadow: 0 12px 30px rgba(15,80,50,0.15);
}

.ai-card h2 {
    color: white;
}

.ai-card p {
    color: #dcefe4;
}

/* ACTION */

.action {
    background: #f7fbf8;
    border: 1px solid #e4eee7;
    padding: 15px 18px;
    border-radius: 15px;
    margin: 9px 0;
}

/* BADGE */

.badge {
    display: inline-block;
    padding: 7px 13px;
    background: #e7f6ed;
    color: #17814f;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 700;
}

/* SCORE */

.big-score {
    font-size: 65px;
    font-weight: 800;
    color: #22935c;
    text-align: center;
}

.score-label {
    text-align: center;
    color: #77837c;
}

/* STREAMLIT BUTTON */

.stButton > button {
    border-radius: 12px;
    border: none;
    background: #1d8b59;
    color: white;
    font-weight: 700;
    padding: 10px 20px;
}

.stButton > button:hover {
    background: #126b43;
    color: white;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #89938d;
    padding: 35px;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA
# =========================================================

panchayats = {
    "Afzalpur": [
        "Afzalpur",
        "Ainapur",
        "Allagi"
    ],
    "Aland": [
        "Aland",
        "Nandarga"
    ],
    "Chincholi": [
        "Chincholi",
        "Honnakiranagi"
    ],
    "Chittapur": [
        "Chittapur",
        "Wadi",
        "Nalwar"
    ],
    "Jevargi": [
        "Jevargi",
        "Nelogi"
    ],
    "Kalaburagi": [
        "Kalaburagi",
        "Kamalapur",
        "Nandur",
        "Sannur"
    ],
    "Sedam": [
        "Sedam",
        "Mudhol"
    ]
}

soils = [
    "Black Soil",
    "Red Soil",
    "Loamy Soil",
    "Sandy Soil",
    "Mixed Soil"
]

crops = [
    "Jowar",
    "Tur / Pigeon Pea",
    "Chickpea",
    "Groundnut",
    "Cotton",
    "Soybean",
    "Maize",
    "Bajra",
    "Millets"
]

# =========================================================
# SESSION STATE
# =========================================================

if "farm" not in st.session_state:
    st.session_state.farm = {}

# =========================================================
# WEATHER FUNCTION
# =========================================================

@st.cache_data(ttl=1800)
def get_weather():

    try:

        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=17.3297"
            "&longitude=76.8343"
            "&current=temperature_2m,relative_humidity_2m,"
            "precipitation,wind_speed_10m"
            "&daily=temperature_2m_max,temperature_2m_min,"
            "precipitation_sum"
            "&timezone=Asia%2FKolkata"
        )

        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()

        current = data["current"]

        return {
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "rain": current["precipitation"],
            "wind": current["wind_speed_10m"]
        }

    except:

        return {
            "temperature": 28,
            "humidity": 55,
            "rain": 0,
            "wind": 10
        }

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="brand">🌱 Agri<span>N</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">REGENERATIVE AGRICULTURAL INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "👨‍🌾 My Farm",
            "🤖 AI Farm Copilot",
            "🌾 Crop Intelligence",
            "🔄 Regenerative Planner",
            "💧 Water Intelligence",
            "♻️ Waste-to-Value",
            "🌳 Biodiversity",
            "📸 AI Crop Doctor",
            "🧪 Soil Scanner",
            "🏘️ Panchayat Intelligence",
            "🌡️ Climate Resilience",
            "💰 Regenerative ROI",
            "📅 30-Day Challenge",
            "🪪 Farm Passport",
            "📊 Impact Dashboard"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    if st.session_state.farm:

        st.markdown(
            '<span class="badge">● FARM CONNECTED</span>',
            unsafe_allow_html=True
        )

        st.write(
            "📍 " +
            st.session_state.farm.get(
                "panchayat",
                "Farm"
            )
        )

    else:

        st.info(
            "Create your farm profile to unlock personalized intelligence."
        )

# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    farm = st.session_state.farm

    if farm:

        location = (
            f"{farm['district']} • "
            f"{farm['taluk']} • "
            f"{farm['panchayat']}"
        )

    else:

        location = "Kalaburagi • North Karnataka"

    st.markdown(
        f"""
        <div class="hero">

        <div class="hero-label">
        GOOD MORNING, FARMER 🌱
        </div>

        <h1>
        Grow better.<br>
        Restore the soil.
        </h1>

        <p>
        AI-powered regenerative farming intelligence
        for healthier soil, smarter water use,
        biodiversity and resilient income.
        </p>

        <div class="location">
        📍 {location}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # METRICS

    st.markdown(
        '<div class="section">Farm at a glance</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(4)

    metrics = [
        ("🌱", "74", "Regeneration Score"),
        ("🧪", "70", "Soil Health"),
        ("💧", "68", "Water Resilience"),
        ("🌳", "61", "Biodiversity")
    ]

    for col, item in zip(cols, metrics):

        with col:

            st.markdown(
                f"""
                <div class="metric-card">

                <div class="icon">{item[0]}</div>

                <div class="number">
                {item[1]}
                </div>

                <div class="label">
                {item[2]}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    # WEATHER

    weather = get_weather()

    st.markdown(
        '<div class="section">🌦️ Live Weather Intelligence</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(4)

    weather_data = [
        ("🌡️", f"{weather['temperature']}°C", "Temperature"),
        ("💧", f"{weather['humidity']}%", "Humidity"),
        ("🌧️", f"{weather['rain']} mm", "Rainfall"),
        ("💨", f"{weather['wind']} km/h", "Wind")
    ]

    for col, item in zip(cols, weather_data):

        with col:

            st.markdown(
                f"""
                <div class="metric-card">

                <div class="icon">{item[0]}</div>

                <div class="number">
                {item[1]}
                </div>

                <div class="label">
                {item[2]}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    # AI

    st.markdown(
        '<div class="section">🤖 Today\'s Intelligence</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns([1.5, 1])

    with left:

        st.markdown("""
        <div class="ai-card">

        <h2>🤖 AI Farm Copilot</h2>

        <p>
        Your farm's next best regenerative actions.
        </p>

        <br>

        <b>🌱 Priority Action</b>

        <p>
        Check soil moisture before irrigation and
        maintain soil cover to reduce evaporation.
        </p>

        <b>♻️ Opportunity</b>

        <p>
        Crop residue can potentially be converted
        into compost, mulch or other value pathways.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with right:

        st.markdown("""
        <div class="card">

        <div class="big-score">
        74
        </div>

        <h3 style="text-align:center">
        Regeneration Score
        </h3>

        <p class="score-label">
        Your farm is moving toward
        a more resilient system.
        </p>

        </div>
        """, unsafe_allow_html=True)

    # QUICK ACTIONS

    st.markdown(
        '<div class="section">⚡ Quick Actions</div>',
        unsafe_allow_html=True
    )

    actions = [
        ("📸", "Scan Crop", "Detect crop stress"),
        ("🧪", "Scan Soil", "Analyze soil report"),
        ("🌾", "Plan Crops", "Choose regenerative crops"),
        ("💧", "Check Water", "Optimize irrigation"),
        ("♻️", "Use Waste", "Find waste value"),
        ("📅", "30-Day Challenge", "Build better practices")
    ]

    cols = st.columns(3)

    for i, action in enumerate(actions):

        with cols[i % 3]:

            st.markdown(
                f"""
                <div class="card">

                <h3>{action[0]} {action[1]}</h3>

                <p style="color:#7b857f">
                {action[2]}
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

# =========================================================
# MY FARM
# =========================================================

elif page == "👨‍🌾 My Farm":

    st.markdown(
        '<div class="section">👨‍🌾 My Farm Profile</div>',
        unsafe_allow_html=True
    )

    district = st.selectbox(
        "📍 District",
        ["Kalaburagi", "Other District"]
    )

    if district == "Kalaburagi":

        taluk = st.selectbox(
            "🏘️ Taluk",
            list(panchayats.keys())
        )

        panchayat = st.selectbox(
            "🏡 Gram Panchayat / Local Area",
            panchayats[taluk]
        )

    else:

        taluk = st.text_input("Taluk")

        panchayat = st.text_input(
            "Gram Panchayat"
        )

    col1, col2 = st.columns(2)

    with col1:

        land = st.number_input(
            "🌾 Land Area (acres)",
            min_value=0.1,
            max_value=1000.0,
            value=2.0,
            step=0.5
        )

        soil = st.selectbox(
            "🧪 Soil Type",
            soils
        )

        crop = st.selectbox(
            "🌱 Main Crop",
            crops
        )

    with col2:

        water = st.selectbox(
            "💧 Water Availability",
            [
                "Abundant",
                "Moderate",
                "Limited",
                "Very Limited"
            ]
        )

        irrigation = st.selectbox(
            "🚿 Irrigation Method",
            [
                "Rainfed",
                "Flood",
                "Drip",
                "Sprinkler"
            ]
        )

        budget = st.number_input(
            "💰 Annual Farm Budget (₹)",
            min_value=0,
            value=50000,
            step=5000
        )

    skills = st.multiselect(
        "👩‍🌾 Available Family/Farm Skills",
        [
            "Beekeeping",
            "Goat Rearing",
            "Poultry",
            "Mushroom Farming",
            "Pickle Making",
            "Food Processing",
            "Dairy",
            "Nursery",
            "Handicrafts"
        ]
    )

    if st.button(
        "💾 Save Farm Profile",
        use_container_width=True
    ):

        st.session_state.farm = {
            "district": district,
            "taluk": taluk,
            "panchayat": panchayat,
            "land": land,
            "soil": soil,
            "crop": crop,
            "water": water,
            "irrigation": irrigation,
            "budget": budget,
            "skills": skills
        }

        st.success(
            "✅ Farm profile saved!"
        )

        st.balloons()

# =========================================================
# AI COPILOT
# =========================================================

elif page == "🤖 AI Farm Copilot":

    st.markdown(
        '<div class="section">🤖 AI Farm Copilot</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.farm:

        st.warning(
            "Please create your Farm Profile first."
        )

    else:

        farm = st.session_state.farm

        st.markdown(
            f"""
            <div class="ai-card">

            <h2>🌱 AgriN Copilot</h2>

            <p>
            Personalized intelligence for
            <b>{farm['panchayat']}</b>
            </p>

            <br>

            <b>Today's Priority</b>

            <p>
            Monitor soil moisture and avoid unnecessary
            irrigation. Maintain soil cover wherever possible.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        question = st.text_input(
            "💬 Ask AgriN anything about your farm"
        )

        if question:

            st.success(
                "🤖 AgriN: Start by checking soil moisture, "
                "crop health and current weather before making "
                "a farming decision."
            )

# =========================================================
# CROP INTELLIGENCE
# =========================================================

elif page == "🌾 Crop Intelligence":

    st.markdown(
        '<div class="section">🌾 Crop Intelligence</div>',
        unsafe_allow_html=True
    )

    soil = st.selectbox(
        "Select Soil Type",
        soils
    )

    recommendations = {

        "Black Soil": [
            "Jowar",
            "Tur / Pigeon Pea",
            "Chickpea",
            "Cotton",
            "Soybean"
        ],

        "Red Soil": [
            "Groundnut",
            "Millets",
            "Tur / Pigeon Pea",
            "Chickpea"
        ],

        "Loamy Soil": [
            "Maize",
            "Chickpea",
            "Jowar",
            "Millets"
        ],

        "Sandy Soil": [
            "Bajra",
            "Groundnut",
            "Millets"
        ],

        "Mixed Soil": [
            "Jowar",
            "Tur / Pigeon Pea",
            "Millets"
        ]
    }

    cols = st.columns(3)

    for i, crop in enumerate(
        recommendations[soil]
    ):

        with cols[i % 3]:

            st.markdown(
                f"""
                <div class="card">

                <h3>🌾 {crop}</h3>

                <p>
                Potential candidate based on
                prototype soil rules.
                </p>

                <span class="badge">
                RECOMMENDED
                </span>

                </div>
                """,
                unsafe_allow_html=True
            )

# =========================================================
# REGENERATIVE PLANNER
# =========================================================

elif page == "🔄 Regenerative Planner":

    st.markdown(
        '<div class="section">🔄 Regenerative Planner</div>',
        unsafe_allow_html=True
    )

    practices = st.multiselect(
        "🌱 Select practices you can adopt",
        [
            "Crop Rotation",
            "Cover Crops",
            "Mulching",
            "Composting",
            "Organic Matter",
            "Drip Irrigation",
            "Agroforestry",
            "Intercropping",
            "Pollinator Zone",
            "Farm Pond",
            "Reduced Tillage",
            "Crop Residue Management"
        ]
    )

    score = min(
        100,
        30 + len(practices) * 6
    )

    c1, c2 = st.columns([1, 2])

    with c1:

        st.markdown(
            f"""
            <div class="card">

            <div class="big-score">
            {score}
            </div>

            <div class="score-label">
            Regeneration Score
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            '<div class="card"><h3>🌱 Your Action Plan</h3>',
            unsafe_allow_html=True
        )

        for p in practices:

            st.markdown(
                f"""
                <div class="action">
                ✓ {p}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

# =========================================================
# WATER INTELLIGENCE
# =========================================================

elif page == "💧 Water Intelligence":

    st.markdown(
        '<div class="section">💧 Water Intelligence</div>',
        unsafe_allow_html=True
    )

    weather = get_weather()

    c1, c2 = st.columns(2)

    with c1:

        moisture = st.slider(
            "Estimated Soil Moisture (%)",
            0,
            100,
            45
        )

    with c2:

        rainfall = st.slider(
            "Expected Rain Reliability (%)",
            0,
            100,
            50
        )

    score = int(
        moisture * 0.6 +
        rainfall * 0.4
    )

    st.markdown(
        f"""
        <div class="card">

        <div class="big-score">
        {score}
        </div>

        <div class="score-label">
        Water Resilience Score
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(score / 100)

    if moisture < 30:

        st.error(
            "🚨 High water stress detected."
        )

    elif moisture < 50:

        st.warning(
            "⚠️ Moderate water stress."
        )

    else:

        st.success(
            "💧 Moisture level appears adequate."
        )

    recommendations = [
        "Use mulch to reduce evaporation.",
        "Irrigate during cooler hours.",
        "Prefer drip irrigation where practical.",
        "Check soil moisture before irrigation.",
        "Use drought-tolerant crops when appropriate."
    ]

    for r in recommendations:

        st.markdown(
            f"""
            <div class="action">
            💧 {r}
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# WASTE TO VALUE
# =========================================================

elif page == "♻️ Waste-to-Value":

    st.markdown(
        '<div class="section">♻️ Waste-to-Value Intelligence</div>',
        unsafe_allow_html=True
    )

    waste = st.selectbox(
        "Select Waste",
        [
            "Crop Residue",
            "Cotton Residue",
            "Maize Stalk",
            "Groundnut Shells",
            "Animal Manure",
            "Organic Farm Waste"
        ]
    )

    pathways = {

        "Crop Residue": [
            "Compost",
            "Mulch",
            "Biochar",
            "Biomass"
        ],

        "Cotton Residue": [
            "Compost",
            "Mulch",
            "Biomass"
        ],

        "Maize Stalk": [
            "Compost",
            "Mulch",
            "Biomass"
        ],

        "Groundnut Shells": [
            "Compost",
            "Mulch",
            "Biomass"
        ],

        "Animal Manure": [
            "Compost",
            "Biogas",
            "Organic Fertilizer"
        ],

        "Organic Farm Waste": [
            "Compost",
            "Vermicompost",
            "Biogas"
        ]
    }

    for item in pathways[waste]:

        st.markdown(
            f"""
            <div class="card">

            <h3>♻️ {item}</h3>

            <p>
            Potential pathway for converting agricultural
            waste into useful resources or value.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# BIODIVERSITY
# =========================================================

elif page == "🌳 Biodiversity":

    st.markdown(
        '<div class="section">🌳 Biodiversity Planner</div>',
        unsafe_allow_html=True
    )

    selected = st.multiselect(
        "Choose biodiversity actions",
        [
            "Native Trees",
            "Pollinator Zone",
            "Intercropping",
            "Farm Boundary Vegetation",
            "Bird Habitat",
            "Flowering Plants",
            "Agroforestry",
            "Reduced Pesticide Dependency"
        ]
    )

    score = min(
        100,
        25 + len(selected) * 9
    )

    st.markdown(
        f"""
        <div class="card">

        <div class="big-score">
        {score}
        </div>

        <div class="score-label">
        Biodiversity Score
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(score / 100)

# =========================================================
# AI CROP DOCTOR
# =========================================================

elif page == "📸 AI Crop Doctor":

    st.markdown(
        '<div class="section">📸 AI Crop Doctor</div>',
        unsafe_allow_html=True
    )

    image = st.file_uploader(
        "Upload crop / leaf image",
        type=["jpg", "jpeg", "png"]
    )

    if image:

        st.image(
            image,
            caption="Uploaded Crop Image",
            use_container_width=True
        )

        if st.button(
            "🔍 Analyze Crop",
            use_container_width=True
        ):

            st.markdown("""
            <div class="card">

            <h3>🤖 Preliminary Crop Analysis</h3>

            <div class="action">
            🌱 Possible leaf stress
            </div>

            <div class="action">
            💧 Check water stress
            </div>

            <div class="action">
            🧪 Check nutrient condition
            </div>

            <div class="action">
            🐛 Inspect for pest/disease symptoms
            </div>

            </div>
            """, unsafe_allow_html=True)

            st.warning(
                "Prototype only. A trained computer-vision model "
                "is required for real disease diagnosis."
            )

    else:

        st.info(
            "Upload a crop image to start the analysis."
        )

# =========================================================
# SOIL SCANNER
# =========================================================

elif page == "🧪 Soil Scanner":

    st.markdown(
        '<div class="section">🧪 Soil Intelligence Scanner</div>',
        unsafe_allow_html=True
    )

    uploaded = st.file_uploader(
        "Upload soil report",
        type=["jpg", "jpeg", "png", "pdf"]
    )

    st.markdown("""
    <div class="card">

    <h3>🧪 What AgriN can analyse</h3>

    <div class="action">pH</div>
    <div class="action">Nitrogen</div>
    <div class="action">Phosphorus</div>
    <div class="action">Potassium</div>
    <div class="action">Organic Carbon</div>
    <div class="action">Electrical Conductivity</div>

    </div>
    """, unsafe_allow_html=True)

    if uploaded:

        st.success(
            "✅ Soil report uploaded successfully."
        )

        st.info(
            "Connect OCR + soil analysis model to automatically "
            "extract values from this report."
        )

# =========================================================
# PANCHAYAT INTELLIGENCE
# =========================================================

elif page == "🏘️ Panchayat Intelligence":

    st.markdown(
        '<div class="section">🏘️ Panchayat Intelligence Center</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

    <h3>🌍 Community Regeneration Intelligence</h3>

    <p>
    AgriN can aggregate anonymized farm indicators to help
    Panchayats understand soil, water, biodiversity and
    climate resilience.
    </p>

    </div>
    """, unsafe_allow_html=True)

    taluk = st.selectbox(
        "🏘️ Select Taluk",
        list(panchayats.keys())
    )

    panchayat = st.selectbox(
        "🏡 Select Panchayat",
        panchayats[taluk]
    )

    scores = {
        "Regeneration": 72,
        "Soil Health": 68,
        "Water Resilience": 64,
        "Biodiversity": 61,
        "Climate Resilience": 70
    }

    cols = st.columns(5)

    icons = [
        "🌱",
        "🧪",
        "💧",
        "🌳",
        "🌡️"
    ]

    for col, (label, value), icon in zip(
        cols,
        scores.items(),
        icons
    ):

        with col:

            st.markdown(
                f"""
                <div class="metric-card">

                <div class="icon">{icon}</div>

                <div class="number">
                {value}
                </div>

                <div class="label">
                {label}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    df = pd.DataFrame({
        "Indicator": list(scores.keys()),
        "Score": list(scores.values())
    })

    fig = px.bar(
        df,
        x="Indicator",
        y="Score",
        range_y=[0, 100],
        title=f"{panchayat} Regenerative Profile"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.caption(
        "⚠️ Panchayat scores are prototype values until "
        "verified local datasets are connected."
    )

# =========================================================
# CLIMATE
# =========================================================

elif page == "🌡️ Climate Resilience":

    st.markdown(
        '<div class="section">🌡️ Climate Resilience Index</div>',
        unsafe_allow_html=True
    )

    drought = st.slider(
        "Drought Risk",
        0,
        100,
        45
    )

    heat = st.slider(
        "Heat Risk",
        0,
        100,
        40
    )

    rainfall = st.slider(
        "Rainfall Variability",
        0,
        100,
        50
    )

    resilience = int(
        100 -
        (
            drought * 0.35 +
            heat * 0.25 +
            rainfall * 0.40
        )
    )

    resilience = max(
        0,
        min(100, resilience)
    )

    st.markdown(
        f"""
        <div class="card">

        <div class="big-score">
        {resilience}
        </div>

        <div class="score-label">
        Climate Resilience Score
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(
        resilience / 100
    )

    for item in [
        "Use drought-tolerant crops.",
        "Increase soil organic matter.",
        "Maintain soil cover.",
        "Improve rainwater harvesting.",
        "Diversify farm income.",
        "Consider agroforestry where suitable."
    ]:

        st.markdown(
            f"""
            <div class="action">
            🛡️ {item}
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# ROI
# =========================================================

elif page == "💰 Regenerative ROI":

    st.markdown(
        '<div class="section">💰 Regenerative ROI Calculator</div>',
        unsafe_allow_html=True
    )

    current = st.number_input(
        "Current Annual Income (₹)",
        min_value=0,
        value=100000,
        step=10000
    )

    water_save = st.number_input(
        "Potential Water Savings (₹)",
        min_value=0,
        value=10000,
        step=1000
    )

    input_save = st.number_input(
        "Potential Input Savings (₹)",
        min_value=0,
        value=12000,
        step=1000
    )

    extra = st.number_input(
        "Potential Additional Income (₹)",
        min_value=0,
        value=20000,
        step=5000
    )

    total = (
        current +
        water_save +
        input_save +
        extra
    )

    improvement = (
        ((total - current) / current) * 100
        if current else 0
    )

    cols = st.columns(3)

    cols[0].metric(
        "Current Income",
        f"₹{current:,.0f}"
    )

    cols[1].metric(
        "Potential Value",
        f"₹{total:,.0f}"
    )

    cols[2].metric(
        "Potential Improvement",
        f"{improvement:.1f}%"
    )

    st.warning(
        "These are planning estimates, not guaranteed returns."
    )

# =========================================================
# 30 DAY CHALLENGE
# =========================================================

elif page == "📅 30-Day Challenge":

    st.markdown(
        '<div class="section">📅 30-Day Regeneration Challenge</div>',
        unsafe_allow_html=True
    )

    tasks = [
        "Observe soil condition",
        "Check soil moisture",
        "Start mulching",
        "Record crop health",
        "Plan crop rotation",
        "Reuse crop residue",
        "Create biodiversity zone",
        "Inspect irrigation",
        "Check pest symptoms",
        "Review water usage",
        "Track farm expenses",
        "Measure regeneration progress"
    ]

    completed = st.slider(
        "Completed activities",
        0,
        len(tasks),
        0
    )

    percentage = int(
        completed / len(tasks) * 100
    )

    st.markdown(
        f"""
        <div class="card">

        <div class="big-score">
        {percentage}%
        </div>

        <div class="score-label">
        Challenge Progress
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(
        completed / len(tasks)
    )

    for i, task in enumerate(tasks, 1):

        icon = "✅" if i <= completed else "○"

        st.markdown(
            f"""
            <div class="action">
            {icon} <b>Day {i}</b> — {task}
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# FARM PASSPORT
# =========================================================

elif page == "🪪 Farm Passport":

    st.markdown(
        '<div class="section">🪪 Farm Regeneration Passport</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.farm:

        st.warning(
            "Create your Farm Profile first."
        )

    else:

        farm = st.session_state.farm

        st.markdown(
            f"""
            <div class="hero">

            <div class="hero-label">
            AGRI-N FARM PASSPORT
            </div>

            <h1>
            🌱 {farm['panchayat']}
            </h1>

            <p>
            {farm['taluk']} • {farm['district']}
            </p>

            <div class="location">
            🌱 Regeneration Score: 74 / 100
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section">Farm Indicators</div>',
            unsafe_allow_html=True
        )

        indicators = [
            ("🧪", 70, "Soil Health"),
            ("💧", 64, "Water"),
            ("🌳", 61, "Biodiversity"),
            ("🌡️", 75, "Climate")
        ]

        cols = st.columns(4)

        for col, item in zip(
            cols,
            indicators
        ):

            with col:

                st.markdown(
                    f"""
                    <div class="metric-card">

                    <div class="icon">
                    {item[0]}
                    </div>

                    <div class="number">
                    {item[1]}
                    </div>

                    <div class="label">
                    {item[2]}
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

# =========================================================
# IMPACT DASHBOARD
# =========================================================

elif page == "📊 Impact Dashboard":

    st.markdown(
        '<div class="section">📊 AgriN Impact Dashboard</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(4)

    impact = [
        ("👨‍🌾", "1,250", "Farmers"),
        ("🌱", "8,450", "Acres"),
        ("💧", "12.4M L", "Water Potential"),
        ("♻️", "1,840 T", "Waste Potential")
    ]

    for col, item in zip(cols, impact):

        with col:

            st.markdown(
                f"""
                <div class="metric-card">

                <div class="icon">
                {item[0]}
                </div>

                <div class="number">
                {item[1]}
                </div>

                <div class="label">
                {item[2]}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        '<div class="section">🌍 Regenerative Impact</div>',
        unsafe_allow_html=True
    )

    data = pd.DataFrame({
        "Area": [
            "Water",
            "Soil",
            "Biodiversity",
            "Waste",
            "Climate"
        ],
        "Score": [
            72,
            68,
            61,
            78,
            70
        ]
    })

    fig = px.bar(
        data,
        x="Area",
        y="Score",
        range_y=[0, 100],
        title="AgriN Regenerative Impact"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.caption(
        "Prototype impact figures — replace with actual "
        "measured platform data."
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

🌱 <b>AgriN</b> — Regenerative Agricultural Intelligence

<br><br>

Observe • Diagnose • Recommend • Act • Measure • Improve

</div>
""", unsafe_allow_html=True)
```

