import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import hashlib
import json
import streamlit.components.v1 as components
from datetime import datetime

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AgriN | Regenerative Agricultural Intelligence",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(34,197,94,0.08), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(14,165,233,0.07), transparent 25%),
        #f7faf8;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #092d20 0%, #0b3d2b 100%);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.brand {
    padding: 18px 5px 25px 5px;
    text-align: center;
}

.brand-logo {
    width: 60px;
    height: 60px;
    margin: auto;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    background: linear-gradient(135deg, #22c55e, #16a34a);
    box-shadow: 0 12px 30px rgba(0,0,0,0.25);
}

.brand-title {
    font-size: 25px;
    font-weight: 800;
    margin-top: 10px;
}

.brand-sub {
    font-size: 11px;
    opacity: 0.7;
}

/* Cards */

.card {
    background: rgba(255,255,255,0.94);
    border: 1px solid #e7eee9;
    border-radius: 20px;
    padding: 22px;
    box-shadow: 0 8px 30px rgba(16, 45, 30, 0.06);
    margin-bottom: 18px;
}

.card:hover {
    box-shadow: 0 14px 35px rgba(16, 45, 30, 0.10);
}

.hero {
    background:
        linear-gradient(135deg, rgba(5,70,43,0.97), rgba(12,110,68,0.94));
    border-radius: 28px;
    padding: 38px;
    color: white;
    margin-bottom: 24px;
    box-shadow: 0 20px 50px rgba(5,70,43,0.20);
}

.hero h1 {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero p {
    color: rgba(255,255,255,0.82);
    font-size: 16px;
}

.badge {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 30px;
    background: rgba(255,255,255,0.13);
    border: 1px solid rgba(255,255,255,0.18);
    font-size: 12px;
    margin-bottom: 14px;
}

.metric-card {
    background: white;
    border-radius: 18px;
    padding: 20px;
    border: 1px solid #e6eee8;
    min-height: 130px;
}

.metric-icon {
    font-size: 25px;
}

.metric-value {
    font-size: 28px;
    font-weight: 800;
    margin-top: 8px;
    color: #123c29;
}

.metric-label {
    font-size: 13px;
    color: #728079;
}

.section-title {
    font-size: 23px;
    font-weight: 800;
    color: #123c29;
    margin: 22px 0 15px 0;
}

.quick {
    background: white;
    border: 1px solid #e5eee8;
    border-radius: 18px;
    padding: 20px;
    min-height: 145px;
}

.quick-icon {
    font-size: 30px;
}

.quick-title {
    font-weight: 700;
    margin-top: 10px;
    color: #153b29;
}

.quick-text {
    font-size: 12px;
    color: #75827a;
}

.alert {
    border-radius: 16px;
    padding: 17px;
    background: #fff8e7;
    border-left: 5px solid #f59e0b;
    margin-bottom: 12px;
}

.success-alert {
    border-radius: 16px;
    padding: 17px;
    background: #ecfdf3;
    border-left: 5px solid #22c55e;
    margin-bottom: 12px;
}

.voice-card {
    background: linear-gradient(135deg, #092d20, #0d5a3c);
    border-radius: 25px;
    padding: 25px;
    color: white;
}

.voice-circle {
    width: 85px;
    height: 85px;
    border-radius: 50%;
    margin: auto;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255,255,255,0.12);
    border: 2px solid rgba(255,255,255,0.3);
    font-size: 40px;
}

.passport {
    background:
        linear-gradient(135deg, #073522, #0e6944);
    border-radius: 25px;
    padding: 28px;
    color: white;
    min-height: 270px;
}

.passport-id {
    font-size: 12px;
    opacity: 0.7;
}

.passport-name {
    font-size: 30px;
    font-weight: 800;
    margin-top: 18px;
}

.profile-chip {
    padding: 10px 14px;
    border-radius: 14px;
    background: rgba(255,255,255,0.10);
    margin-top: 8px;
    font-size: 12px;
}

.login-box {
    max-width: 850px;
    margin: 50px auto;
}

.login-brand {
    text-align: center;
    margin-bottom: 30px;
}

.login-logo {
    width: 80px;
    height: 80px;
    margin: auto;
    background: linear-gradient(135deg,#22c55e,#15803d);
    border-radius: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 43px;
    box-shadow: 0 20px 40px rgba(22,163,74,0.25);
}

.login-title {
    font-size: 38px;
    font-weight: 800;
    color: #103b27;
    margin-top: 14px;
}

.login-sub {
    color: #718078;
}

.small-muted {
    color: #77847c;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HELPERS
# ============================================================

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def farm_template(
    name="Demo Farmer",
    district="Kalaburagi",
    village="Kalaburagi",
    land=5.0,
    water="Moderate",
    soil="Black Soil",
    budget=50000
):
    return {
        "name": name,
        "district": district,
        "village": village,
        "land": float(land),
        "water": water,
        "soil": soil,
        "budget": int(budget),
        "phone": "",
        "primary_crop": "Jowar",
        "skills": ["Crop farming"],
    }


def initialize():
    if "users" not in st.session_state:
        st.session_state.users = {
            "demo@agrin.in": {
                "password": hash_password("AgriN@123"),
                "farm": farm_template()
            }
        }

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "current_user" not in st.session_state:
        st.session_state.current_user = None

    if "farm" not in st.session_state:
        st.session_state.farm = farm_template()

    if "language" not in st.session_state:
        st.session_state.language = "English"

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "challenge_day" not in st.session_state:
        st.session_state.challenge_day = 7


initialize()

# ============================================================
# TRANSLATIONS
# ============================================================

TRANSLATIONS = {
    "English": {
        "dashboard": "Dashboard",
        "farm": "My Farm",
        "copilot": "AI Farm Copilot",
        "voice": "Voice Assistant",
        "crop": "Crop Intelligence",
        "soil": "Soil Intelligence",
        "water": "Water Intelligence",
        "weather": "Climate & Weather",
        "waste": "Waste-to-Value",
        "biodiversity": "Biodiversity",
        "doctor": "Crop Doctor",
        "panchayat": "Panchayat Connect",
        "roi": "ROI Calculator",
        "passport": "Farm Passport",
        "impact": "Impact Dashboard",
        "challenge": "30-Day Challenge",
        "alerts": "Farm Alerts",
        "welcome": "Good afternoon",
        "logout": "Logout"
    },
    "Kannada": {
        "dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "farm": "ನನ್ನ ಜಮೀನು",
        "copilot": "AI ಕೃಷಿ ಸಹಾಯಕ",
        "voice": "ಧ್ವನಿ ಸಹಾಯಕ",
        "crop": "ಬೆಳೆ ಬುದ್ಧಿಮತ್ತೆ",
        "soil": "ಮಣ್ಣಿನ ಬುದ್ಧಿಮತ್ತೆ",
        "water": "ನೀರಿನ ಬುದ್ಧಿಮತ್ತೆ",
        "weather": "ಹವಾಮಾನ",
        "waste": "ತ್ಯಾಜ್ಯದಿಂದ ಸಂಪತ್ತು",
        "biodiversity": "ಜೈವ ವೈವಿಧ್ಯತೆ",
        "doctor": "ಬೆಳೆ ವೈದ್ಯ",
        "panchayat": "ಪಂಚಾಯತ್ ಸಂಪರ್ಕ",
        "roi": "ಆದಾಯ ಲೆಕ್ಕಾಚಾರ",
        "passport": "ಕೃಷಿ ಪಾಸ್‌ಪೋರ್ಟ್",
        "impact": "ಪರಿಣಾಮ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "challenge": "30 ದಿನಗಳ ಸವಾಲು",
        "alerts": "ಕೃಷಿ ಎಚ್ಚರಿಕೆಗಳು",
        "welcome": "ಶುಭ ಮಧ್ಯಾಹ್ನ",
        "logout": "ಲಾಗ್ ಔಟ್"
    },
    "Hindi": {
        "dashboard": "डैशबोर्ड",
        "farm": "मेरा खेत",
        "copilot": "AI कृषि सहायक",
        "voice": "वॉइस असिस्टेंट",
        "crop": "फसल इंटेलिजेंस",
        "soil": "मिट्टी इंटेलिजेंस",
        "water": "जल इंटेलिजेंस",
        "weather": "मौसम",
        "waste": "कचरे से कमाई",
        "biodiversity": "जैव विविधता",
        "doctor": "फसल डॉक्टर",
        "panchayat": "पंचायत कनेक्ट",
        "roi": "ROI कैलकुलेटर",
        "passport": "फार्म पासपोर्ट",
        "impact": "इम्पैक्ट डैशबोर्ड",
        "challenge": "30-दिन चुनौती",
        "alerts": "कृषि अलर्ट",
        "welcome": "शुभ दोपहर",
        "logout": "लॉग आउट"
    }
}


def t(key):
    return TRANSLATIONS[st.session_state.language].get(
        key,
        TRANSLATIONS["English"].get(key, key)
    )


# ============================================================
# AI FARM RESPONSE
# ============================================================

def assistant_reply(question):
    q = question.lower()
    lang = st.session_state.language

    if lang == "Kannada":
        if "ಮಣ್ಣು" in q or "soil" in q:
            return "ನಿಮ್ಮ ಕಪ್ಪು ಮಣ್ಣಿಗೆ ಜೋಳ, ತೊಗರಿ ಮತ್ತು ಸಜ್ಜೆ ಉತ್ತಮ ಆಯ್ಕೆಗಳು. ಮಣ್ಣಿನ ತೇವಾಂಶವನ್ನು ಗಮನಿಸಿ."
        if "ನೀರು" in q or "water" in q:
            return "ನೀರಿನ ಕೊರತೆ ಇದ್ದರೆ ಡ್ರಿಪ್ ನೀರಾವರಿ, ಮಲ್ಚಿಂಗ್ ಮತ್ತು ಕಡಿಮೆ ನೀರಿನ ಬೆಳೆಗಳನ್ನು ಪರಿಗಣಿಸಿ."
        if "ಬೆಳೆ" in q or "crop" in q:
            return "ನಿಮ್ಮ ಪರಿಸ್ಥಿತಿಗೆ ಜೋಳ + ತೊಗರಿ ಸಂಯೋಜನೆ ಉತ್ತಮ ಆರಂಭಿಕ ಆಯ್ಕೆಯಾಗಿದೆ."
        if "ಹವಾಮಾನ" in q or "weather" in q:
            return "ಮಳೆಯ ಸಾಧ್ಯತೆ ಇದ್ದಾಗ ಬಿತ್ತನೆ ಸಮಯವನ್ನು ಸರಿಹೊಂದಿಸಿ ಮತ್ತು ಮಣ್ಣಿನ ತೇವಾಂಶವನ್ನು ಪರಿಶೀಲಿಸಿ."
        return "ನಿಮ್ಮ ಜಮೀನು, ನೀರು ಮತ್ತು ಬಜೆಟ್ ಆಧರಿಸಿ ಉತ್ತಮ ನಿರ್ಧಾರ ತೆಗೆದುಕೊಳ್ಳಲು ನಾನು ಸಹಾಯ ಮಾಡುತ್ತೇನೆ."

    if lang == "Hindi":
        if "मिट्टी" in q or "soil" in q:
            return "आपकी काली मिट्टी के लिए ज्वार, अरहर और बाजरा अच्छे विकल्प हैं। मिट्टी की नमी पर ध्यान दें।"
        if "पानी" in q or "water" in q:
            return "पानी की कमी होने पर ड्रिप सिंचाई, मल्चिंग और कम पानी वाली फसलों को प्राथमिकता दें।"
        if "फसल" in q or "crop" in q:
            return "आपकी स्थिति के लिए ज्वार + अरहर का संयोजन एक अच्छा शुरुआती विकल्प है।"
        if "मौसम" in q or "weather" in q:
            return "बारिश की संभावना होने पर बुवाई का समय समायोजित करें और मिट्टी की नमी जांचें।"
        return "मैं आपकी जमीन, पानी और बजट के आधार पर बेहतर कृषि निर्णय लेने में मदद कर सकता हूं."

    if "soil" in q:
        return "Your black soil has good moisture-holding capacity. Consider Jowar + Tur, millet, or pulse-based rotations."
    if "water" in q:
        return "Prioritize drip irrigation, mulching and drought-tolerant crops. Avoid irrigation when soil moisture is already sufficient."
    if "crop" in q:
        return "For your current profile, Jowar + Tur intercropping is a strong low-risk option with climate resilience."
    if "weather" in q or "rain" in q:
        return "Monitor rainfall before sowing. If rain is expected, prepare seed treatment and avoid unnecessary irrigation."
    if "income" in q or "money" in q:
        return "You can diversify income through goats, beekeeping, poultry, millet processing or farm-waste products."
    if "waste" in q:
        return "Crop residue can become compost, mulch, briquettes or livestock feed instead of being burned."
    if "scheme" in q:
        return "Use the Panchayat Connect section to identify relevant agriculture, livestock and water-support schemes."
    return "I can help you with crops, soil, water, weather, income diversification, waste-to-value and regenerative farming."


# ============================================================
# VOICE ASSISTANT
# ============================================================

def voice_assistant():
    language_codes = {
        "English": "en-IN",
        "Kannada": "kn-IN",
        "Hindi": "hi-IN"
    }

    lang_code = language_codes[st.session_state.language]

    html = """
    <div style="
        background:linear-gradient(135deg,#092d20,#0d5b3d);
        border-radius:24px;
        padding:28px;
        color:white;
        font-family:Arial,sans-serif;
        text-align:center;
    ">

        <div style="
            width:85px;
            height:85px;
            border-radius:50%;
            margin:0 auto 15px auto;
            display:flex;
            align-items:center;
            justify-content:center;
            background:rgba(255,255,255,.12);
            border:2px solid rgba(255,255,255,.25);
            font-size:40px;
        ">🎙️</div>

        <h2 style="margin:0;">Arya — AgriN Voice Assistant</h2>

        <p style="opacity:.75;">
            Ask about crops, soil, water, weather or farm income
        </p>

        <button id="listenBtn" style="
            border:none;
            border-radius:30px;
            padding:13px 24px;
            background:#22c55e;
            color:white;
            font-weight:bold;
            cursor:pointer;
            margin:8px;
        ">🎤 Start Listening</button>

        <button id="speakBtn" style="
            border:none;
            border-radius:30px;
            padding:13px 24px;
            background:#ffffff;
            color:#123c29;
            font-weight:bold;
            cursor:pointer;
            margin:8px;
        ">🔊 Speak Answer</button>

        <div style="
            background:rgba(255,255,255,.08);
            border-radius:15px;
            padding:15px;
            margin-top:18px;
            text-align:left;
        ">
            <b>What I heard:</b>
            <div id="transcript" style="margin-top:7px;opacity:.8;">
                Tap Start Listening...
            </div>
        </div>

        <div style="
            background:rgba(255,255,255,.08);
            border-radius:15px;
            padding:15px;
            margin-top:12px;
            text-align:left;
        ">
            <b>Arya's advice:</b>
            <div id="answer" style="margin-top:7px;line-height:1.6;">
                Hello farmer! How can I help your farm today?
            </div>
        </div>

        <div id="status" style="
            margin-top:15px;
            font-size:12px;
            opacity:.65;
        ">
            Browser voice ready
        </div>
    </div>

    <script>

    const LANG = "__LANG__";

    const SpeechRecognition =
        window.SpeechRecognition ||
        window.webkitSpeechRecognition;

    let recognition = null;
    let lastAnswer = "Hello farmer! How can I help your farm today?";

    function createAnswer(text) {

        const q = text.toLowerCase();

        if (LANG === "kn-IN") {

            if (q.includes("ಮಣ್ಣು") || q.includes("soil")) {
                return "ನಿಮ್ಮ ಕಪ್ಪು ಮಣ್ಣಿಗೆ ಜೋಳ, ತೊಗರಿ ಮತ್ತು ಸಜ್ಜೆ ಉತ್ತಮ ಆಯ್ಕೆಗಳು.";
            }

            if (q.includes("ನೀರು") || q.includes("water")) {
                return "ಡ್ರಿಪ್ ನೀರಾವರಿ, ಮಲ್ಚಿಂಗ್ ಮತ್ತು ಕಡಿಮೆ ನೀರಿನ ಬೆಳೆಗಳನ್ನು ಬಳಸಿ.";
            }

            if (q.includes("ಬೆಳೆ") || q.includes("crop")) {
                return "ಜೋಳ ಮತ್ತು ತೊಗರಿ ಸಂಯೋಜನೆ ನಿಮ್ಮ ಪ್ರದೇಶಕ್ಕೆ ಉತ್ತಮ ಆರಂಭಿಕ ಆಯ್ಕೆಯಾಗಿದೆ.";
            }

            if (q.includes("ಹವಾಮಾನ") || q.includes("weather")) {
                return "ಮಳೆಯ ಮುನ್ಸೂಚನೆಯನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ಮಣ್ಣಿನ ತೇವಾಂಶಕ್ಕೆ ಅನುಗುಣವಾಗಿ ನೀರು ನೀಡಿ.";
            }

            return "ಬೆಳೆ, ಮಣ್ಣು, ನೀರು, ಹವಾಮಾನ ಅಥವಾ ಆದಾಯದ ಬಗ್ಗೆ ನನ್ನನ್ನು ಕೇಳಬಹುದು.";
        }

        if (LANG === "hi-IN") {

            if (q.includes("मिट्टी") || q.includes("soil")) {
                return "आपकी काली मिट्टी के लिए ज्वार, अरहर और बाजरा अच्छे विकल्प हैं।";
            }

            if (q.includes("पानी") || q.includes("water")) {
                return "ड्रिप सिंचाई, मल्चिंग और कम पानी वाली फसलों को प्राथमिकता दें।";
            }

            if (q.includes("फसल") || q.includes("crop")) {
                return "ज्वार और अरहर का संयोजन एक अच्छा जलवायु-लचीला विकल्प है।";
            }

            if (q.includes("मौसम") || q.includes("weather")) {
                return "बारिश की संभावना होने पर सिंचाई कम करें और मिट्टी की नमी जांचें।";
            }

            return "आप फसल, मिट्टी, पानी, मौसम या आय के बारे में पूछ सकते हैं।";
        }

        if (q.includes("soil")) {
            return "Your black soil is suitable for Jowar, Tur, millet and pulse rotations.";
        }

        if (q.includes("water")) {
            return "Use drip irrigation, mulching and drought-tolerant crops to improve water efficiency.";
        }

        if (q.includes("crop")) {
            return "Jowar plus Tur intercropping is a strong climate-resilient option for your farm.";
        }

        if (q.includes("weather") || q.includes("rain")) {
            return "Check rainfall before irrigation and avoid unnecessary watering before expected rain.";
        }

        if (q.includes("income") || q.includes("money")) {
            return "Consider goats, beekeeping, poultry, millet processing and farm-waste products for additional income.";
        }

        return "I can help you with crops, soil, water, weather and farm income.";
    }

    function speak(text) {
        if (!window.speechSynthesis) {
            document.getElementById("status").innerText =
                "Speech synthesis is not supported in this browser.";
            return;
        }

        window.speechSynthesis.cancel();

        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = LANG;
        utterance.rate = 0.95;

        window.speechSynthesis.speak(utterance);
    }

    document.getElementById("speakBtn").onclick = function() {
        speak(lastAnswer);
    };

    document.getElementById("listenBtn").onclick = function() {

        if (!SpeechRecognition) {
            document.getElementById("status").innerText =
                "Voice recognition is not supported. Try Chrome or Edge.";
            return;
        }

        recognition = new SpeechRecognition();

        recognition.lang = LANG;
        recognition.continuous = false;
        recognition.interimResults = false;

        document.getElementById("status").innerText =
            "Listening... speak now 🎙️";

        recognition.start();

        recognition.onresult = function(event) {

            const text =
                event.results[0][0].transcript;

            document.getElementById("transcript").innerText = text;

            lastAnswer = createAnswer(text);

            document.getElementById("answer").innerText =
                lastAnswer;

            document.getElementById("status").innerText =
                "Answer generated ✓";

            speak(lastAnswer);
        };

        recognition.onerror = function() {

            document.getElementById("status").innerText =
                "Could not hear you. Please try again.";
        };

        recognition.onend = function() {

            if (
                document.getElementById("status").innerText ===
                "Listening... speak now 🎙️"
            ) {
                document.getElementById("status").innerText =
                    "Voice session ended.";
            }
        };
    };

    </script>
    """

    html = html.replace("__LANG__", lang_code)

    components.html(
        html,
        height=560,
        scrolling=False
    )


# ============================================================
# LOGIN SCREEN
# ============================================================

def login_screen():

    st.markdown("""
    <div class="login-box">

        <div class="login-brand">

            <div class="login-logo">🌱</div>

            <div class="login-title">AgriN</div>

            <div class="login-sub">
                Regenerative Agricultural Intelligence
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])

    with center:

        tab_login, tab_register = st.tabs(
            ["🔐 Login", "📝 Create Farmer Account"]
        )

        with tab_login:

            st.markdown(
                '<div class="card">',
                unsafe_allow_html=True
            )

            email = st.text_input(
                "Email",
                placeholder="farmer@example.com",
                key="login_email"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password",
                key="login_password"
            )

            if st.button(
                "🚜 Login to AgriN",
                use_container_width=True
            ):

                email_clean = email.strip().lower()

                if (
                    email_clean in st.session_state.users
                    and st.session_state.users[email_clean]["password"]
                    == hash_password(password)
                ):

                    st.session_state.logged_in = True
                    st.session_state.current_user = email_clean
                    st.session_state.farm = dict(
                        st.session_state.users[email_clean]["farm"]
                    )

                    st.rerun()

                else:
                    st.error(
                        "Invalid email or password."
                    )

            st.markdown(
                """
                <div style="
                    background:#f0fdf4;
                    border-radius:12px;
                    padding:12px;
                    margin-top:15px;
                    font-size:12px;
                ">
                <b>Demo account</b><br>
                Email: demo@agrin.in<br>
                Password: AgriN@123
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("</div>", unsafe_allow_html=True)

        with tab_register:

            st.markdown(
                '<div class="card">',
                unsafe_allow_html=True
            )

            name = st.text_input(
                "Full Name",
                placeholder="Enter your name"
            )

            reg_email = st.text_input(
                "Email Address",
                placeholder="farmer@example.com"
            )

            reg_phone = st.text_input(
                "Mobile Number",
                placeholder="+91 XXXXX XXXXX"
            )

            reg_password = st.text_input(
                "Create Password",
                type="password"
            )

            reg_district = st.selectbox(
                "District",
                [
                    "Kalaburagi",
                    "Bidar",
                    "Yadgir",
                    "Raichur",
                    "Vijayapura",
                    "Bagalkot",
                    "Koppal",
                    "Ballari",
                    "Gadag",
                    "Dharwad",
                    "Haveri",
                    "Belagavi",
                    "Chitradurga"
                ]
            )

            reg_land = st.number_input(
                "Land Area (acres)",
                min_value=0.1,
                max_value=500.0,
                value=5.0,
                step=0.5
            )

            if st.button(
                "🌱 Create Farmer Account",
                use_container_width=True
            ):

                email_clean = reg_email.strip().lower()

                if not name or not email_clean or not reg_password:
                    st.warning(
                        "Please fill all required fields."
                    )

                elif email_clean in st.session_state.users:
                    st.error(
                        "An account with this email already exists."
                    )

                elif len(reg_password) < 6:
                    st.error(
                        "Password should contain at least 6 characters."
                    )

                else:

                    new_farm = farm_template(
                        name=name,
                        district=reg_district,
                        village=reg_district,
                        land=reg_land
                    )

                    new_farm["phone"] = reg_phone

                    st.session_state.users[email_clean] = {
                        "password": hash_password(reg_password),
                        "farm": new_farm
                    }

                    st.session_state.logged_in = True
                    st.session_state.current_user = email_clean
                    st.session_state.farm = new_farm

                    st.success(
                        "Account created successfully!"
                    )

                    st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#718078;
            font-size:12px;
            margin-top:25px;
        ">
        🌱 Designed for climate-resilient and regenerative farming
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SIDEBAR
# ============================================================

def sidebar():

    farm = st.session_state.farm

    st.sidebar.markdown("""
    <div class="brand">

        <div class="brand-logo">🌱</div>

        <div class="brand-title">AgriN</div>

        <div class="brand-sub">
            REGENERATIVE AGRICULTURAL INTELLIGENCE
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown(
        f"""
        <div class="profile-chip">
        👨‍🌾 <b>{farm["name"]}</b><br>
        📍 {farm["district"]}<br>
        🌾 {farm["land"]} acres
        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown("### 🌐 Language")

    st.session_state.language = st.sidebar.selectbox(
        "Choose language",
        ["English", "Kannada", "Hindi"],
        index=["English", "Kannada", "Hindi"].index(
            st.session_state.language
        )
    )

    navigation = {
        "🏠 Dashboard": t("dashboard"),
        "👨‍🌾 My Farm": t("farm"),
        "🤖 AI Farm Copilot": t("copilot"),
        "🎙️ Voice Assistant": t("voice"),
        "🌱 Crop Intelligence": t("crop"),
        "🧪 Soil Intelligence": t("soil"),
        "💧 Water Intelligence": t("water"),
        "🌦️ Climate & Weather": t("weather"),
        "♻️ Waste-to-Value": t("waste"),
        "🐝 Biodiversity": t("biodiversity"),
        "🩺 Crop Doctor": t("doctor"),
        "🏛️ Panchayat Connect": t("panchayat"),
        "💰 ROI Calculator": t("roi"),
        "🪪 Farm Passport": t("passport"),
        "📊 Impact Dashboard": t("impact"),
        "📅 30-Day Challenge": t("challenge"),
        "🔔 Farm Alerts": t("alerts")
    }

    page = st.sidebar.radio(
        "Navigation",
        list(navigation.keys()),
        label_visibility="collapsed"
    )

    st.sidebar.markdown("---")

    if st.sidebar.button(
        "🚪 " + t("logout"),
        use_container_width=True
    ):

        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.rerun()

    st.sidebar.markdown(
        """
        <div style="
            text-align:center;
            opacity:.55;
            font-size:10px;
            margin-top:20px;
        ">
        AgriN v2.0<br>
        Climate Intelligence Platform
        </div>
        """,
        unsafe_allow_html=True
    )

    return page


# ============================================================
# DASHBOARD
# ============================================================

def dashboard():

    farm = st.session_state.farm

    st.markdown(
        f"""
        <div class="hero">

            <span class="badge">
            🟢 FARM SYSTEM ONLINE
            </span>

            <h1>{t("welcome")}, {farm["name"].split()[0]} 👋</h1>

            <p>
            Your farm intelligence center is ready.
            AgriN is continuously helping you make
            climate-smart and income-focused decisions.
            </p>

            <div style="margin-top:20px;">
                📍 {farm["district"]} &nbsp; • &nbsp;
                🌾 {farm["land"]} acres &nbsp; • &nbsp;
                🧪 {farm["soil"]}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # Metrics

    cols = st.columns(4)

    metrics = [
        ("🌱", "Farm Health", "86%", "+8%"),
        ("💧", "Water Efficiency", "72%", "+14%"),
        ("💰", "Income Potential", "₹1.8L", "+21%"),
        ("🌍", "Climate Score", "82/100", "+6")
    ]

    for col, item in zip(cols, metrics):

        with col:
            st.markdown(
                f"""
                <div class="metric-card">

                    <div class="metric-icon">
                    {item[0]}
                    </div>

                    <div class="metric-value">
                    {item[2]}
                    </div>

                    <div class="metric-label">
                    {item[1]}
                    </div>

                    <div style="
                        color:#16a34a;
                        font-size:12px;
                        margin-top:6px;
                    ">
                    ↑ {item[3]} this season
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        '<div class="section-title">🤖 Today\'s Intelligence</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns([1.55, 1])

    with left:

        st.markdown(
            """
            <div class="card">

                <h3>🌦️ Priority Recommendation</h3>

                <p>
                Rainfall is expected soon. Avoid unnecessary irrigation
                and prepare your field for moisture retention.
                </p>

                <div class="success-alert">
                <b>AI Recommendation</b><br>
                Apply organic mulch around the crop root zone
                and inspect drainage channels.
                </div>

                <div class="alert">
                <b>⚠️ Attention</b><br>
                Soil moisture should be checked before the next irrigation cycle.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        st.markdown(
            """
            <div class="card">

                <h3>🌱 Next Best Actions</h3>

                <p>✓ Check soil moisture</p>
                <p>✓ Prepare seed treatment</p>
                <p>✓ Inspect drip lines</p>
                <p>✓ Record crop expenses</p>
                <p>✓ Check market prices</p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">⚡ Quick Farm Actions</div>',
        unsafe_allow_html=True
    )

    qcols = st.columns(4)

    quicks = [
        ("🎙️", "Ask Arya", "Talk to your AI farm assistant"),
        ("🌱", "Find Crop", "Get climate-smart crop suggestions"),
        ("🧪", "Scan Soil", "Analyse your soil condition"),
        ("💰", "Estimate Income", "Calculate possible farm returns")
    ]

    for col, q in zip(qcols, quicks):

        with col:

            st.markdown(
                f"""
                <div class="quick">

                    <div class="quick-icon">{q[0]}</div>

                    <div class="quick-title">
                    {q[1]}
                    </div>

                    <div class="quick-text">
                    {q[2]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        '<div class="section-title">📈 Farm Intelligence Score</div>',
        unsafe_allow_html=True
    )

    score_df = pd.DataFrame({
        "Category": [
            "Soil",
            "Water",
            "Biodiversity",
            "Climate",
            "Income"
        ],
        "Score": [88, 72, 69, 82, 76]
    })

    fig = px.bar(
        score_df,
        x="Category",
        y="Score",
        range_y=[0, 100],
        title="Current Farm Readiness"
    )

    fig.update_layout(
        height=330,
        margin=dict(l=10, r=10, t=50, b=10)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# MY FARM
# ============================================================

def my_farm():

    farm = st.session_state.farm

    st.markdown(
        '<div class="section-title">👨‍🌾 My Farm Profile</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Your profile powers AgriN's personalized recommendations."
    )

    c1, c2 = st.columns(2)

    with c1:

        name = st.text_input(
            "Farmer Name",
            value=farm["name"]
        )

        district = st.selectbox(
            "District",
            [
                "Kalaburagi",
                "Bidar",
                "Yadgir",
                "Raichur",
                "Vijayapura",
                "Bagalkot",
                "Koppal",
                "Ballari",
                "Gadag",
                "Dharwad",
                "Haveri",
                "Belagavi",
                "Chitradurga"
            ],
            index=0
        )

        village = st.text_input(
            "Village",
            value=farm["village"]
        )

    with c2:

        land = st.number_input(
            "Land Area (acres)",
            min_value=0.1,
            max_value=500.0,
            value=float(farm["land"]),
            step=0.5
        )

        water = st.selectbox(
            "Water Availability",
            ["Very Low", "Low", "Moderate", "Good"],
            index=[
                "Very Low",
                "Low",
                "Moderate",
                "Good"
            ].index(farm["water"])
            if farm["water"] in [
                "Very Low",
                "Low",
                "Moderate",
                "Good"
            ] else 2
        )

        soil = st.selectbox(
            "Soil Type",
            [
                "Black Soil",
                "Red Soil",
                "Sandy Soil",
                "Loamy Soil",
                "Mixed Soil"
            ],
            index=0
        )

    budget = st.number_input(
        "Seasonal Farming Budget (₹)",
        min_value=1000,
        max_value=10000000,
        value=int(farm["budget"]),
        step=5000
    )

    skills = st.multiselect(
        "Family / Farm Skills",
        [
            "Crop farming",
            "Goat rearing",
            "Poultry",
            "Beekeeping",
            "Mushroom cultivation",
            "Food processing",
            "Pickle making",
            "Millet processing",
            "Handicrafts",
            "Kasuti",
            "Bidri",
            "Agarbatti making"
        ],
        default=farm.get("skills", ["Crop farming"])
    )

    if st.button(
        "💾 Save Farm Profile",
        use_container_width=True
    ):

        st.session_state.farm.update({
            "name": name,
            "district": district,
            "village": village,
            "land": land,
            "water": water,
            "soil": soil,
            "budget": budget,
            "skills": skills
        })

        email = st.session_state.current_user

        if email in st.session_state.users:
            st.session_state.users[email]["farm"] = dict(
                st.session_state.farm
            )

        st.success(
            "Farm profile updated successfully!"
        )

    st.markdown(
        '<div class="section-title">🧭 Farm Summary</div>',
        unsafe_allow_html=True
    )

    a, b, c, d = st.columns(4)

    a.metric("Land", f'{farm["land"]} acres')
    b.metric("Water", farm["water"])
    c.metric("Soil", farm["soil"])
    d.metric("Budget", f'₹{farm["budget"]:,}')


# ============================================================
# AI COPILOT
# ============================================================

def copilot():

    st.markdown(
        """
        <div class="hero">

            <span class="badge">🤖 AI FARM COPILOT</span>

            <h1>Ask Arya</h1>

            <p>
            Your intelligent farming companion for
            climate, crops, soil, water and income.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    suggestions = [
        "Which crop should I grow?",
        "How can I save water?",
        "How can I increase income?",
        "What can I do with crop waste?",
        "How can I improve my soil?"
    ]

    cols = st.columns(5)

    for col, suggestion in zip(cols, suggestions):

        with col:

            if st.button(
                suggestion,
                use_container_width=True
            ):

                reply = assistant_reply(suggestion)

                st.session_state.chat_history.append(
                    ("user", suggestion)
                )

                st.session_state.chat_history.append(
                    ("assistant", reply)
                )

    for role, message in st.session_state.chat_history:

        with st.chat_message(
            "user" if role == "user" else "assistant"
        ):

            st.write(message)

    question = st.chat_input(
        "Ask Arya anything about your farm..."
    )

    if question:

        st.session_state.chat_history.append(
            ("user", question)
        )

        reply = assistant_reply(question)

        st.session_state.chat_history.append(
            ("assistant", reply)
        )

        st.rerun()


# ============================================================
# VOICE ASSISTANT
# ============================================================

def voice_page():

    st.markdown(
        """
        <div class="hero">

            <span class="badge">🎙️ VOICE-FIRST AGRICULTURE</span>

            <h1>Meet Arya</h1>

            <p>
            A farmer-friendly voice assistant designed
            for simple, natural conversations.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    voice_assistant()

    st.markdown(
        '<div class="section-title">💬 You can ask</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(4)

    examples = [
        "🌱 Which crop is best?",
        "💧 How to save water?",
        "🌦️ What about rain?",
        "💰 How can I earn more?"
    ]

    for col, text in zip(cols, examples):

        with col:
            st.markdown(
                f'<div class="quick"><b>{text}</b></div>',
                unsafe_allow_html=True
            )

    st.info(
        "For best voice recognition, open the deployed app in Chrome or Edge and allow microphone access."
    )


# ============================================================
# CROP INTELLIGENCE
# ============================================================

def crop_intelligence():

    st.markdown(
        '<div class="section-title">🌱 AI Crop Intelligence</div>',
        unsafe_allow_html=True
    )

    farm = st.session_state.farm

    water_score = {
        "Very Low": 1,
        "Low": 2,
        "Moderate": 3,
        "Good": 4
    }.get(farm["water"], 3)

    recommendations = [
        {
            "Crop": "Jowar",
            "Water Need": "Low",
            "Climate Resilience": 94,
            "Income Potential": 82,
            "Why": "Highly suitable for dryland farming."
        },
        {
            "Crop": "Tur",
            "Water Need": "Low",
            "Climate Resilience": 91,
            "Income Potential": 84,
            "Why": "Good pulse crop for rotation and intercropping."
        },
        {
            "Crop": "Bajra",
            "Water Need": "Very Low",
            "Climate Resilience": 96,
            "Income Potential": 78,
            "Why": "Excellent drought resilience."
        },
        {
            "Crop": "Groundnut",
            "Water Need": "Moderate",
            "Climate Resilience": 78,
            "Income Potential": 87,
            "Why": "Potentially attractive where moisture is available."
        }
    ]

    df = pd.DataFrame(recommendations)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.success(
        "🏆 AI Pick: Jowar + Tur intercropping"
    )

    st.write(
        "This recommendation balances drought resilience, "
        "water demand, soil improvement and income diversification."
    )


# ============================================================
# SOIL
# ============================================================

def soil_intelligence():

    st.markdown(
        '<div class="section-title">🧪 Soil Intelligence</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Upload a soil photo for a future AI-vision integration, "
        "or use the current profile-based assessment."
    )

    uploaded = st.file_uploader(
        "📸 Upload Soil Photo",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded:

        st.image(
            uploaded,
            caption="Uploaded soil sample",
            use_container_width=True
        )

        st.success(
            "Visual sample received. Prototype AI assessment: "
            "dark soil indicates potentially good organic matter, "
            "but laboratory testing is recommended for actual nutrient decisions."
        )

    st.markdown(
        """
        <div class="card">

        <h3>🧠 Current Soil Assessment</h3>

        <p><b>Soil:</b> Black Soil</p>
        <p><b>Moisture Retention:</b> High</p>
        <p><b>Recommended:</b> Pulses + millets + organic matter</p>
        <p><b>Action:</b> Add compost and maintain crop residue cover</p>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# WATER
# ============================================================

def water_intelligence():

    st.markdown(
        '<div class="section-title">💧 Water Intelligence</div>',
        unsafe_allow_html=True
    )

    water_df = pd.DataFrame({
        "Method": [
            "Drip Irrigation",
            "Mulching",
            "Rainwater Harvesting",
            "Farm Pond",
            "Sprinkler"
        ],
        "Potential Saving (%)": [
            45, 30, 35, 40, 25
        ]
    })

    fig = px.bar(
        water_df,
        x="Method",
        y="Potential Saving (%)",
        title="Potential Water Savings"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown(
        """
        <div class="success-alert">
        <b>💧 AgriN Recommendation</b><br>
        Combine mulching + drip irrigation for the strongest
        water-efficiency improvement.
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# WEATHER
# ============================================================

def climate_weather():

    st.markdown(
        '<div class="section-title">🌦️ Climate & Weather Intelligence</div>',
        unsafe_allow_html=True
    )

    city = st.session_state.farm["district"]

    try:

        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=17.3297"
            "&longitude=76.8343"
            "&current=temperature_2m,relative_humidity_2m,"
            "precipitation,wind_speed_10m"
        )

        response = requests.get(
            url,
            timeout=5
        )

        data = response.json()

        current = data.get("current", {})

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "🌡️ Temperature",
            f'{current.get("temperature_2m", "--")} °C'
        )

        c2.metric(
            "💧 Humidity",
            f'{current.get("relative_humidity_2m", "--")} %'
        )

        c3.metric(
            "🌧️ Rain",
            f'{current.get("precipitation", "--")} mm'
        )

        c4.metric(
            "💨 Wind",
            f'{current.get("wind_speed_10m", "--")} km/h'
        )

        st.success(
            f"Live weather connection active for {city} region."
        )

    except Exception:

        st.warning(
            "Live weather is temporarily unavailable. "
            "The rest of the AgriN intelligence system is still available."
        )


# ============================================================
# WASTE
# ============================================================

def waste_to_value():

    st.markdown(
        '<div class="section-title">♻️ Waste-to-Value Network</div>',
        unsafe_allow_html=True
    )

    waste = st.selectbox(
        "Select available farm waste",
        [
            "Crop residue",
            "Coconut waste",
            "Millet husk",
            "Vegetable waste",
            "Animal manure",
            "Sugarcane residue"
        ]
    )

    options = {
        "Crop residue": [
            "Compost",
            "Mulch",
            "Briquettes",
            "Animal feed"
        ],
        "Coconut waste": [
            "Coir",
            "Compost",
            "Biochar",
            "Handicrafts"
        ],
        "Millet husk": [
            "Animal feed",
            "Compost",
            "Biofuel"
        ],
        "Vegetable waste": [
            "Compost",
            "Biogas",
            "Animal feed"
        ],
        "Animal manure": [
            "Compost",
            "Biogas",
            "Vermicompost"
        ],
        "Sugarcane residue": [
            "Mulch",
            "Biomass",
            "Compost"
        ]
    }

    st.success(
        "♻️ Potential resource pathways:"
    )

    cols = st.columns(4)

    for col, option in zip(
        cols,
        options[waste]
    ):

        with col:
            st.markdown(
                f"""
                <div class="quick">
                    <div class="quick-icon">♻️</div>
                    <div class="quick-title">{option}</div>
                    <div class="quick-text">
                    Potential value pathway
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# BIODIVERSITY
# ============================================================

def biodiversity():

    st.markdown(
        '<div class="section-title">🐝 Biodiversity Intelligence</div>',
        unsafe_allow_html=True
    )

    practices = [
        ("🐝", "Bee-friendly plants", 20),
        ("🌳", "Native tree plantation", 25),
        ("🌼", "Flower borders", 15),
        ("🪱", "Earthworm ecosystem", 20),
        ("🐦", "Bird-friendly habitat", 10)
    ]

    for icon, name, score in practices:

        c1, c2 = st.columns([3, 1])

        with c1:
            st.write(f"{icon} **{name}**")
            st.progress(score / 25)

        with c2:
            st.write(f"+{score} points")


# ============================================================
# CROP DOCTOR
# ============================================================

def crop_doctor():

    st.markdown(
        '<div class="section-title">🩺 AI Crop Doctor</div>',
        unsafe_allow_html=True
    )

    uploaded = st.file_uploader(
        "📸 Upload a crop/leaf photo",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded:

        st.image(
            uploaded,
            use_container_width=True
        )

        st.markdown(
            """
            <div class="card">

            <h3>🔬 Prototype AI Screening</h3>

            <p><b>Possible issue:</b> Leaf stress / nutrient imbalance</p>

            <p><b>Confidence:</b> 78%</p>

            <p>
            Recommended action: inspect the underside of leaves,
            check soil moisture and consult a local agriculture officer
            before applying chemical treatment.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.info(
            "Upload a clear leaf photo to activate the prototype screening interface."
        )


# ============================================================
# PANCHAYAT
# ============================================================

def panchayat():

    st.markdown(
        '<div class="section-title">🏛️ Panchayat Connect</div>',
        unsafe_allow_html=True
    )

    schemes = pd.DataFrame({
        "Support Area": [
            "Micro Irrigation",
            "Livestock",
            "Soil Health",
            "Farmer Training",
            "Self Help Groups"
        ],
        "Priority": [
            "High",
            "High",
            "Medium",
            "Medium",
            "High"
        ],
        "Action": [
            "Check eligibility",
            "Contact local office",
            "Soil test",
            "Register",
            "Join group"
        ]
    })

    st.dataframe(
        schemes,
        use_container_width=True,
        hide_index=True
    )

    st.warning(
        "Scheme eligibility and availability should be verified with the official local department before applying."
    )


# ============================================================
# ROI
# ============================================================

def roi_calculator():

    st.markdown(
        '<div class="section-title">💰 Farm ROI Calculator</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:

        land = st.number_input(
            "Land Area (acres)",
            0.5,
            500.0,
            float(st.session_state.farm["land"]),
            0.5
        )

        yield_per_acre = st.number_input(
            "Expected Yield (kg/acre)",
            100.0,
            10000.0,
            900.0
        )

    with c2:

        price = st.number_input(
            "Expected Selling Price (₹/kg)",
            1.0,
            1000.0,
            35.0
        )

        cost = st.number_input(
            "Total Cost (₹)",
            1000.0,
            10000000.0,
            50000.0
        )

    revenue = land * yield_per_acre * price
    profit = revenue - cost
    roi = (profit / cost) * 100 if cost > 0 else 0

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Expected Revenue",
        f"₹{revenue:,.0f}"
    )

    c2.metric(
        "Estimated Profit",
        f"₹{profit:,.0f}"
    )

    c3.metric(
        "ROI",
        f"{roi:.1f}%"
    )

    if profit > 0:
        st.success(
            "🌱 Positive projected return. Consider testing the model on a small area before scaling."
        )
    else:
        st.error(
            "⚠️ Current assumptions indicate a negative return. Adjust crop, price, yield or cost assumptions."
        )


# ============================================================
# FARM PASSPORT
# ============================================================

def farm_passport():

    farm = st.session_state.farm

    passport_id = (
        "AGN-"
        + hashlib.md5(
            st.session_state.current_user.encode()
        ).hexdigest()[:8].upper()
    )

    st.markdown(
        '<div class="section-title">🪪 Digital Farm Passport</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="passport">

            <div class="passport-id">
            DIGITAL FARM PASSPORT • {passport_id}
            </div>

            <div class="passport-name">
            {farm["name"]}
            </div>

            <p>
            📍 {farm["village"]}, {farm["district"]}
            </p>

            <p>
            🌾 Farm Size: {farm["land"]} acres
            </p>

            <p>
            🧪 Soil: {farm["soil"]}
            </p>

            <p>
            💧 Water: {farm["water"]}
            </p>

            <p>
            🌱 Regenerative Score: <b>86 / 100</b>
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "### 🌍 Farm Identity"

    )

    st.write(
        "The Digital Farm Passport creates a structured identity "
        "for tracking farm practices, climate resilience, "
        "resource efficiency and impact over time."
    )


# ============================================================
# IMPACT
# ============================================================

def impact_dashboard():

    st.markdown(
        '<div class="section-title">📊 Impact Dashboard</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "💧 Water Saved",
        "31,500 L"
    )

    c2.metric(
        "🌱 Soil Improvement",
        "18%"
    )

    c3.metric(
        "♻️ Waste Reused",
        "420 kg"
    )

    c4.metric(
        "💰 Extra Income",
        "₹38,000"
    )

    impact_df = pd.DataFrame({
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ],
        "Regenerative Score": [
            54,
            59,
            65,
            72,
            79,
            86
        ]
    })

    fig = px.line(
        impact_df,
        x="Month",
        y="Regenerative Score",
        markers=True,
        title="Regenerative Progress"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# 30 DAY CHALLENGE
# ============================================================

def challenge():

    st.markdown(
        '<div class="section-title">📅 30-Day Regenerative Farming Challenge</div>',
        unsafe_allow_html=True
    )

    day = st.session_state.challenge_day

    st.progress(
        day / 30
    )

    st.markdown(
        f"""
        <div class="card">

        <h2>Day {day} of 30 🌱</h2>

        <p>
        Today's mission:
        </p>

        <h3>
        💧 Measure soil moisture before irrigation.
        </h3>

        <p class="small-muted">
        Small actions compound into stronger soil,
        better water efficiency and climate resilience.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "✅ Complete Today's Mission",
        use_container_width=True
    ):

        if day < 30:
            st.session_state.challenge_day += 1

        st.success(
            "Mission completed! Your regenerative score increased."
        )

        st.rerun()


# ============================================================
# ALERTS
# ============================================================

def alerts():

    st.markdown(
        '<div class="section-title">🔔 Farm Alerts</div>',
        unsafe_allow_html=True
    )

    alerts_data = [
        (
            "🌧️ Weather Alert",
            "Rain may arrive soon. Avoid unnecessary irrigation."
        ),
        (
            "💧 Water Alert",
            "Check soil moisture before the next irrigation cycle."
        ),
        (
            "🌱 Crop Alert",
            "Inspect crop leaves for early signs of stress."
        ),
        (
            "♻️ Sustainability Alert",
            "Do not burn crop residue. Consider compost, mulch or biomass use."
        )
    ]

    for title, text in alerts_data:

        st.markdown(
            f"""
            <div class="alert">

            <b>{title}</b><br>

            {text}

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# MAIN APP
# ============================================================

if not st.session_state.logged_in:

    login_screen()

else:

    page = sidebar()

    if page == "🏠 Dashboard":
        dashboard()

    elif page == "👨‍🌾 My Farm":
        my_farm()

    elif page == "🤖 AI Farm Copilot":
        copilot()

    elif page == "🎙️ Voice Assistant":
        voice_page()

    elif page == "🌱 Crop Intelligence":
        crop_intelligence()

    elif page == "🧪 Soil Intelligence":
        soil_intelligence()

    elif page == "💧 Water Intelligence":
        water_intelligence()

    elif page == "🌦️ Climate & Weather":
        climate_weather()

    elif page == "♻️ Waste-to-Value":
        waste_to_value()

    elif page == "🐝 Biodiversity":
        biodiversity()

    elif page == "🩺 Crop Doctor":
        crop_doctor()

    elif page == "🏛️ Panchayat Connect":
        panchayat()

    elif page == "💰 ROI Calculator":
        roi_calculator()

    elif page == "🪪 Farm Passport":
        farm_passport()

    elif page == "📊 Impact Dashboard":
        impact_dashboard()

    elif page == "📅 30-Day Challenge":
        challenge()

    elif page == "🔔 Farm Alerts":
        alerts()


