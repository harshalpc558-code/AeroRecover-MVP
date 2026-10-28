"""
AeroRecover — Agentic AI Recovery Operations Layer MVP
Team: Lakeside_Logic | IIM Mumbai
Case 7: Travel, Hospitality & Aviation
"""

import streamlit as st
import time
import random
from datetime import datetime, timedelta

# ──────────────────────────────────────────────────────────────
# Page Configuration
# ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AeroRecover | Agentic Recovery Operations",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────────────────────────
# Custom CSS — Deep Navy / Amber / White Theme (PPT Match)
# ──────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ── Global ─────────────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background-color: #0B192C;
    }

    /* ── Hide Streamlit chrome ──────────────────────────── */
    #MainMenu, footer, header {visibility: hidden;}

    /* ── Typography ─────────────────────────────────────── */
    h1, h2, h3, h4, h5, h6 {
        color: #EAB308 !important;
        font-weight: 700;
    }

    p, span, div, label, .stMarkdown {
        color: #FFFFFF;
    }

    /* ── Hero Header ────────────────────────────────────── */
    .hero-container {
        background: linear-gradient(135deg, #0B192C 0%, #132743 50%, #0B192C 100%);
        border: 1px solid #1E3A5F;
        border-radius: 16px;
        padding: 32px 40px;
        margin-bottom: 24px;
        text-align: center;
    }
    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        color: #EAB308;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        font-size: 1.1rem;
        color: #94A3B8;
        margin-top: 8px;
        font-weight: 400;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(234, 179, 8, 0.15);
        border: 1px solid #EAB308;
        color: #EAB308;
        padding: 4px 16px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-top: 12px;
    }

    /* ── White Cards ────────────────────────────────────── */
    .white-card {
        background: #FFFFFF;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 16px;
        color: #1E293B !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.25);
    }
    .white-card h3, .white-card h4 {
        color: #0B192C !important;
        margin-top: 0;
    }
    .white-card p, .white-card span, .white-card div {
        color: #334155 !important;
    }

    /* ── Metric Cards ───────────────────────────────────── */
    .metric-card {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 18px 20px;
        text-align: center;
        box-shadow: 0 2px 12px rgba(0,0,0,0.2);
        border-top: 4px solid #EAB308;
    }
    .metric-value {
        font-size: 1.9rem;
        font-weight: 800;
        color: #0B192C !important;
        margin: 0;
    }
    .metric-label {
        font-size: 0.78rem;
        color: #64748B !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 4px;
        font-weight: 600;
    }

    /* ── Success Box (Auto-Execution) ───────────────────── */
    .success-box {
        background: #F0FDF4;
        border: 2px solid #22C55E;
        border-left: 6px solid #22C55E;
        border-radius: 12px;
        padding: 20px 24px;
        margin: 12px 0;
        color: #166534 !important;
    }
    .success-box h4 { color: #15803D !important; margin-top: 0; }
    .success-box p, .success-box span, .success-box div { color: #166534 !important; }

    /* ── Warning Box (HITL Escalation) ──────────────────── */
    .warning-box {
        background: #FFF7ED;
        border: 2px solid #F97316;
        border-left: 6px solid #F97316;
        border-radius: 12px;
        padding: 20px 24px;
        margin: 12px 0;
        color: #9A3412 !important;
    }
    .warning-box h4 { color: #C2410C !important; margin-top: 0; }
    .warning-box p, .warning-box span, .warning-box div { color: #9A3412 !important; }

    /* ── WhatsApp Mock ──────────────────────────────────── */
    .whatsapp-bubble {
        background: #DCF8C6;
        border-radius: 12px 12px 0 12px;
        padding: 14px 18px;
        margin: 8px 0 8px auto;
        max-width: 85%;
        color: #1E293B !important;
        font-size: 0.92rem;
        line-height: 1.5;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .whatsapp-bubble strong { color: #0B192C !important; }
    .whatsapp-time {
        font-size: 0.7rem;
        color: #94A3B8 !important;
        text-align: right;
        margin-top: 4px;
    }
    .whatsapp-header {
        background: #075E54;
        color: white !important;
        padding: 12px 18px;
        border-radius: 12px 12px 0 0;
        font-weight: 600;
        font-size: 0.95rem;
    }

    /* ── Agent Status Pill ──────────────────────────────── */
    .agent-pill {
        display: inline-block;
        background: #1E3A5F;
        border: 1px solid #2D5580;
        color: #CBD5E1 !important;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
        margin: 4px 4px 4px 0;
    }
    .agent-pill-active {
        background: rgba(234, 179, 8, 0.15);
        border: 1px solid #EAB308;
        color: #EAB308 !important;
    }
    .agent-pill-done {
        background: rgba(34, 197, 94, 0.12);
        border: 1px solid #22C55E;
        color: #4ADE80 !important;
    }

    /* ── Expander Override ──────────────────────────────── */
    .streamlit-expanderHeader {
        background-color: #132743 !important;
        border-radius: 8px !important;
        color: #EAB308 !important;
        font-weight: 600 !important;
    }
    .streamlit-expanderContent {
        background-color: #0F2137 !important;
        border-radius: 0 0 8px 8px !important;
        border: 1px solid #1E3A5F !important;
    }

    /* ── Buttons ────────────────────────────────────────── */
    .stButton > button {
        background: linear-gradient(135deg, #EAB308, #CA8A04) !important;
        color: #0B192C !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 28px !important;
        font-size: 1rem !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 14px rgba(234, 179, 8, 0.3) !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(234, 179, 8, 0.5) !important;
    }

    /* Green approve button variant */
    .approve-btn .stButton > button {
        background: linear-gradient(135deg, #22C55E, #16A34A) !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 14px rgba(34, 197, 94, 0.3) !important;
    }

    /* ── Divider ────────────────────────────────────────── */
    hr {
        border-color: #1E3A5F !important;
    }

    /* ── Progress bar ───────────────────────────────────── */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #EAB308, #CA8A04) !important;
    }

    /* ── Code / thinking text ───────────────────────────── */
    .thinking-text {
        font-family: 'Courier New', monospace;
        font-size: 0.82rem;
        color: #94A3B8 !important;
        line-height: 1.6;
    }

    /* ── Section header ─────────────────────────────────── */
    .section-header {
        font-size: 1.3rem;
        font-weight: 700;
        color: #EAB308 !important;
        border-bottom: 2px solid #EAB308;
        padding-bottom: 6px;
        margin: 24px 0 16px 0;
        display: inline-block;
    }

    /* ── Tags ───────────────────────────────────────────── */
    .tag {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.72rem;
        font-weight: 600;
        margin: 2px;
    }
    .tag-auto { background: #DCFCE7; color: #15803D; }
    .tag-hitl { background: #FFEDD5; color: #C2410C; }
    .tag-info { background: #DBEAFE; color: #1D4ED8; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────────────
# Session State Initialisation
# ──────────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "stage": "idle",            # idle → orchestrating → resolved
        "disruption_triggered": False,
        "orchestrator_done": False,
        "passenger1_done": False,
        "passenger2_done": False,
        "human_approved": False,
        "human_rejected": False,
        "log": [],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ──────────────────────────────────────────────────────────────
# Mock Data
# ──────────────────────────────────────────────────────────────
PASSENGERS = {
    "P1": {
        "pnr": "6E-2X7KQ",
        "name": "Priya Sharma",
        "tier": "Gold",
        "route": "DEL → BOM",
        "original_flight": "6E-2045 (06:15 → 08:30)",
        "original_fare": 6800,
        "new_flight": "6E-6112 (09:45 → 11:55)",
        "new_fare": 10300,
        "fare_difference": 3500,
        "baggage": "15 kg checked, 7 kg cabin",
        "ssr": None,
        "medical": False,
        "connection": "Tight connection to BLR (2h 15m)",
    },
    "P2": {
        "pnr": "6E-9MTPR",
        "name": "Rajesh Verma",
        "tier": "Platinum",
        "route": "DEL → BLR (via BOM)",
        "original_flight": "6E-2045 (06:15 → 08:30) + 6E-5120 (10:45 → 12:45)",
        "original_fare": 12400,
        "new_flight": "6E-8801 (11:30 → 14:00) + 6E-5124 (16:00 → 18:10)",
        "new_fare": 19900,
        "fare_difference": 7500,
        "baggage": "20 kg checked, 7 kg cabin",
        "ssr": "Wheelchair assistance requested",
        "medical": True,
        "connection": "Multi-leg; connection in BOM",
    },
}

# ──────────────────────────────────────────────────────────────
# Helper UI Components
# ──────────────────────────────────────────────────────────────
def hero():
    st.markdown(
        """
        <div class="hero-container">
            <p class="hero-title">✈️ AeroRecover</p>
            <p class="hero-subtitle">
                Agentic AI Recovery Operations Layer &nbsp;|&nbsp;
                Neuro-Symbolic &nbsp;·&nbsp; Human-Governed &nbsp;·&nbsp; DGCA-Native
            </p>
            <span class="hero-badge">Team Lakeside_Logic · IIM Mumbai · Case 7</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section(title):
    st.markdown(f'<p class="section-header">{title}</p>', unsafe_allow_html=True)


def metric_card(value, label, col):
    with col:
        st.markdown(
            f"""
            <div class="metric-card">
                <p class="metric-value">{value}</p>
                <p class="metric-label">{label}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def agent_thinking(agent_name, lines, expanded=True):
    """Renders an expander simulating the agent's thinking process."""
    with st.expander(f"🧠 Agent Thinking Process — {agent_name}", expanded=expanded):
        for line in lines:
            st.markdown(f'<p class="thinking-text">▸ {line}</p>', unsafe_allow_html=True)
            time.sleep(0.4)


def success_box(title, body):
    st.markdown(
        f"""
        <div class="success-box">
            <h4>✅ {title}</h4>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def warning_box(title, body):
    st.markdown(
        f"""
        <div class="warning-box">
            <h4>⚠️ {title}</h4>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def whatsapp_mock(passenger_name, message, time_str="Now"):
    st.markdown(
        f"""
        <div style="max-width:560px; margin:16px 0;">
            <div class="whatsapp-header">📱 WhatsApp Business — AeroRecover</div>
            <div style="background:#0F2137; padding:16px; border-radius:0 0 12px 12px;">
                <div class="whatsapp-bubble">
                    {message}
                    <div class="whatsapp-time">{time_str} ✓✓</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ──────────────────────────────────────────────────────────────
# Orchestrator Simulation
# ──────────────────────────────────────────────────────────────
def run_orchestrator():
    """Simulates the Orchestrator Agent identifying stranded PNRs."""

    st.session_state.disruption_triggered = True
    st.session_state.stage = "orchestrating"

    # ── Progress simulation ──────────────────────────────
    progress_placeholder = st.empty()
    status_placeholder = st.empty()

    steps = [
        ("🌫️ Ingesting fog disruption signal at DEL...", 10),
        ("📡 Correlating NOTAM + airline ops feed...", 25),
        ("🔍 Identifying stranded PNRs across 3 flights...", 45),
        ("📊 Scoring PNRs by urgency, loyalty, connection risk...", 65),
        ("🧮 Triage Agent: 2 high-priority PNRs identified", 80),
        ("✅ Orchestrator: Dispatching sub-agents...", 100),
    ]

    for msg, pct in steps:
        with progress_placeholder.container():
            st.progress(pct / 100.0)
        with status_placeholder.container():
            st.markdown(
                f'<p style="color:#EAB308; font-size:0.95rem; font-weight:600;">{msg}</p>',
                unsafe_allow_html=True,
            )
        time.sleep(0.9)

    progress_placeholder.empty()
    status_placeholder.empty()

    # ── Agent thinking expander ──────────────────────────
    agent_thinking(
        "Orchestrator + Triage Agent",
        [
            "Trigger received: Dense fog at DEL (CAT III conditions). 14 departures affected.",
            "Querying live GDS (mock Amadeus) for PNRs with DEL origin...",
            "Found 2 stranded PNRs with high urgency scores.",
            "PNR 1: 6E-2X7KQ — Priya Sharma (Gold tier). Urgency: 8.2/10. Connection risk: HIGH.",
            "PNR 2: 6E-9MTPR — Rajesh Verma (Platinum tier). Urgency: 9.1/10. Medical SSR + multi-leg.",
            "Dispatching Rebooking Agent + Fare & DGCA Agent for both PNRs in parallel.",
        ],
    )

    st.session_state.orchestrator_done = True
    st.session_state.stage = "resolved"


# ──────────────────────────────────────────────────────────────
# Passenger 1 — Auto-Execution Flow
# ──────────────────────────────────────────────────────────────
def run_passenger1():
    p = PASSENGERS["P1"]

    st.markdown(
        f"""
        <div class="white-card">
            <h3>👤 Passenger 1 — {p['name']}</h3>
            <p><strong>PNR:</strong> {p['pnr']} &nbsp;|&nbsp; <strong>Tier:</strong> {p['tier']} &nbsp;|&nbsp; <strong>Route:</strong> {p['route']}</p>
            <p><strong>Original:</strong> {p['original_flight']} &nbsp;|&nbsp; <strong>Fare:</strong> ₹{p['original_fare']:,}</p>
            <p><strong>Baggage:</strong> {p['baggage']} &nbsp;|&nbsp; <strong>SSR:</strong> None &nbsp;|&nbsp; <strong>Connection:</strong> {p['connection']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Agent thinking: Rebook + Fare ────────────────────
    agent_thinking(
        "Rebooking Agent → Fare & DGCA Agent",
        [
            "Rebooking Agent: Querying GDS for DEL→BOM alternatives on same day...",
            "Found 3 options: 6E-6112 (09:45), AI-805 (10:30), 6E-5099 (11:15).",
            "Ranking by arrival time, fare, baggage, lounge access...",
            "Top pick: 6E-6112 — arrives 11:55, same-cabin, 15kg baggage honoured.",
            "Fare & DGCA Agent: Calling deterministic Python API for fare diff calculation...",
            "Fare diff API returned: ₹3,500 (new fare ₹10,300 − original ₹6,800).",
            "DGCA check: Same-cabin change, no medical/SSR. Policy gate: ₹3,500 < ₹5,000 threshold.",
            "Verdict: ✅ ELIGIBLE FOR AUTO-EXECUTION.",
        ],
    )

    # ── Auto-execution success box ───────────────────────
    success_box(
        "Auto-Execution Authorised — Fare Diff ₹3,500 < ₹5,000 Threshold",
        f"""
        <strong>Decision:</strong> AI auto-executed the rebooking.<br>
        <strong>New Flight:</strong> {p['new_flight']}<br>
        <strong>Fare Difference:</strong> ₹{p['fare_difference']:,} (within ₹5,000 auto-execute limit)<br>
        <strong>Compliance:</strong> DGCA CAR Section 3, Series M, Part IV — same-cabin, no SSR → auto-eligible.<br>
        <strong>Audit:</strong> Immutable ledger entry created.
        """,
    )

    # ── WhatsApp message mock ────────────────────────────
    whatsapp_mock(
        p["name"],
        f"""
        <strong>Hi {p['name']},</strong><br><br>
        Your flight <strong>{p['original_flight']}</strong> from DEL to BOM has been disrupted due to fog.<br><br>
        ✅ <strong>We've rebooked you automatically!</strong><br><br>
        <strong>New Flight:</strong> {p['new_flight']}<br>
        <strong>Seat:</strong> 12A (Window)<br>
        <strong>Fare Difference:</strong> ₹{p['fare_difference']:,} (waived under DGCA auto-recovery policy)<br><br>
        Your boarding pass will be available at the gate. Lounge access has been extended by 2 hours.<br><br>
        — AeroRecover ✈️
        """,
        time_str="Just now",
    )

    st.session_state.passenger1_done = True


# ──────────────────────────────────────────────────────────────
# Passenger 2 — HITL Escalation Flow
# ──────────────────────────────────────────────────────────────
def run_passenger2():
    p = PASSENGERS["P2"]

    st.markdown(
        f"""
        <div class="white-card">
            <h3>👤 Passenger 2 — {p['name']}</h3>
            <p><strong>PNR:</strong> {p['pnr']} &nbsp;|&nbsp; <strong>Tier:</strong> {p['tier']} &nbsp;|&nbsp; <strong>Route:</strong> {p['route']}</p>
            <p><strong>Original:</strong> {p['original_flight']} &nbsp;|&nbsp; <strong>Fare:</strong> ₹{p['original_fare']:,}</p>
            <p><strong>Baggage:</strong> {p['baggage']} &nbsp;|&nbsp; <strong>SSR:</strong> {p['ssr']} &nbsp;|&nbsp; <strong>Connection:</strong> {p['connection']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Agent thinking: Rebook + Fare + HITL ─────────────
    agent_thinking(
        "Rebooking Agent → Fare & DGCA Agent → HITL Gate",
        [
            "Rebooking Agent: Querying GDS for DEL→BLR via BOM alternatives...",
            "Multi-leg routing required. Found 2 interline options.",
            "Top pick: 6E-8801 (11:30 → 14:00) + 6E-5124 (16:00 → 18:10).",
            "Fare & DGCA Agent: Calling deterministic Python API for fare diff...",
            "Fare diff API returned: ₹7,500 (new fare ₹19,900 − original ₹12,400).",
            "Medical SSR detected: Wheelchair assistance requested.",
            "Policy gate: ₹7,500 > ₹5,000 AND medical SSR present.",
            "Verdict: ⚠️ HITL ESCALATION REQUIRED — building Resolution Pack.",
            "Resolution Pack compiled: fare breakdown, DGCA eligibility, alternative options, audit trail.",
            "Pausing for human agent approval.",
        ],
    )

    # ── Warning box ──────────────────────────────────────
    warning_box(
        "Human-in-the-Loop Escalation Required",
        f"""
        <strong>Reason:</strong> Fare difference ₹{p['fare_difference']:,} exceeds ₹5,000 auto-execute threshold <strong>AND</strong> medical SSR (wheelchair) present.<br>
        <strong>Resolution Pack</strong> has been pre-calculated and is ready for human review.<br>
        <strong>AI Recommendation:</strong> Approve the rebooking — only same-day multi-leg option available.<br>
        <strong>Compliance:</strong> DGCA CAR Section 3, Series M, Part IV — medical SSR requires human approval.
        """,
    )

    # ── Resolution Pack (Human Agent Dashboard) ──────────
    section("🧑‍💼 Human Agent Approval Dashboard — Resolution Pack")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class="white-card">
                <h4>📋 Resolution Pack</h4>
                <p><strong>PNR:</strong> {p['pnr']}</p>
                <p><strong>Passenger:</strong> {p['name']} ({p['tier']} tier)</p>
                <p><strong>Original:</strong> {p['original_flight']}</p>
                <p><strong>New:</strong> {p['new_flight']}</p>
                <p><strong>Fare Diff:</strong> <span style="color:#C2410C; font-weight:700;">₹{p['fare_difference']:,}</span></p>
                <p><strong>SSR:</strong> {p['ssr']}</p>
                <p><strong>Connection:</strong> {p['connection']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="white-card">
                <h4>⚖️ DGCA Compliance Check</h4>
                <p>✅ Same-cabin change — eligible for rebooking</p>
                <p>✅ Qualifying disruption (fog — force majeure)</p>
                <p>✅ Refund slab: ₹5,000–₹10,000 (CAR M-IV)</p>
                <p>⚠️ Medical SSR — requires human sign-off</p>
                <p>⚠️ Fare diff ₹7,500 > ₹5,000 auto-execute limit</p>
                <p><strong>Verdict:</strong> <span style="color:#C2410C; font-weight:700;">HUMAN APPROVAL REQUIRED</span></p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── Alternative options ──────────────────────────────
    st.markdown(
        """
        <div class="white-card">
            <h4>🔄 Ranked Alternative Options</h4>
            <p><strong>Option 1 (AI Recommended):</strong> 6E-8801 (11:30 → 14:00) + 6E-5124 (16:00 → 18:10) — Fare diff ₹7,500 — Arrives 18:10 — Same cabin, wheelchair support confirmed</p>
            <p><strong>Option 2:</strong> AI-502 (13:15 → 15:45) + AI-609 (18:30 → 20:40) — Fare diff ₹9,200 — Arrives 20:40 — Interline, lounge access available</p>
            <p><strong>Option 3:</strong> Full refund + hotel voucher — ₹12,400 refund + ₹3,000 voucher — Next-day rebooking</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Approval buttons ─────────────────────────────────
    st.markdown('<div class="approve-btn">', unsafe_allow_html=True)
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])

    with col_btn1:
        if st.button("✅ Approve & Execute", key="approve_btn", use_container_width=True):
            st.session_state.human_approved = True
            st.session_state.passenger2_done = True
            st.rerun()

    with col_btn2:
        if st.button("❌ Reject & Escalate", key="reject_btn", use_container_width=True):
            st.session_state.human_rejected = True
            st.session_state.passenger2_done = True
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # ── Post-approval states ─────────────────────────────
    if st.session_state.human_approved:
        success_box(
            "Human Approved — Rebooking Executed",
            f"""
            <strong>Human agent approved the Resolution Pack.</strong><br>
            <strong>New Flight:</strong> {p['new_flight']}<br>
            <strong>Fare Difference:</strong> ₹{p['fare_difference']:,} (approved by human agent)<br>
            <strong>SSR:</strong> {p['ssr']} — confirmed with ground staff<br>
            <strong>Audit:</strong> Human approval logged in immutable ledger.
            """,
        )
        whatsapp_mock(
            p["name"],
            f"""
            <strong>Hi {p['name']},</strong><br><br>
            Your multi-leg flight from DEL → BLR (via BOM) has been disrupted due to fog.<br><br>
            ✅ <strong>Your rebooking has been confirmed by our support team!</strong><br><br>
            <strong>New Flights:</strong><br>
            • {p['new_flight'].split(' + ')[0]}<br>
            • {p['new_flight'].split(' + ')[1]}<br><br>
            <strong>Fare Difference:</strong> ₹{p['fare_difference']:,} (approved by human agent)<br>
            <strong>Wheelchair Assistance:</strong> Confirmed at both airports<br><br>
            A human agent has reviewed your case and confirmed all details. Your boarding passes will be available at the gate.<br><br>
            — AeroRecover ✈️
            """,
            time_str="Just now",
        )

    elif st.session_state.human_rejected:
        warning_box(
            "Human Rejected — Escalated to Senior Agent",
            f"""
            <strong>Resolution Pack rejected by human agent.</strong><br>
            Case escalated to senior recovery specialist.<br>
            <strong>Alternative:</strong> Full refund (₹{p['original_fare']:,}) + hotel voucher being processed.<br>
            <strong>Audit:</strong> Rejection logged in immutable ledger.
            """,
        )


# ──────────────────────────────────────────────────────────────
# Main App
# ──────────────────────────────────────────────────────────────
def main():
    hero()

    # ── KPI strip ────────────────────────────────────────
    k1, k2, k3, k4 = st.columns(4)
    metric_card("< 5 min", "Target Resolution", k1)
    metric_card("80%", "Auto-Resolution Target", k2)
    metric_card("₹5,000", "Auto-Execute Threshold", k3)
    metric_card("100%", "Audit Coverage", k4)

    st.markdown("---")

    # ── Trigger section ──────────────────────────────────
    section("🚨 Disruption Simulator")

    if not st.session_state.disruption_triggered:
        col_a, col_b, col_c = st.columns([1, 2, 1])
        with col_b:
            st.markdown(
                """
                <div class="white-card" style="text-align:center;">
                    <h3>🌫️ Fog Disruption at DEL</h3>
                    <p>Simulate a dense fog event at Delhi (DEL) that strands passengers across multiple flights.</p>
                    <p style="font-size:0.85rem; color:#64748B;">This will trigger the full AeroRecover agentic workflow.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("🌫️ Trigger Fog Disruption at DEL", use_container_width=True):
                run_orchestrator()
                st.rerun()

    else:
        # ── Orchestrator completed ───────────────────────
        if st.session_state.orchestrator_done:
            success_box(
                "Orchestrator Agent — Triage Complete",
                """
                <strong>2 stranded PNRs identified and prioritised.</strong><br>
                • PNR 1: 6E-2X7KQ — Priya Sharma (Gold) — Urgency 8.2/10 — Auto-eligible<br>
                • PNR 2: 6E-9MTPR — Rajesh Verma (Platinum) — Urgency 9.1/10 — Medical SSR → HITL<br>
                Dispatching Rebooking + Fare & DGCA Agents in parallel.
                """,
            )

            st.markdown("---")

            # ── Passenger 1 ──────────────────────────────
            section("🟢 Passenger 1 — Auto-Execution Path")
            run_passenger1()

            st.markdown("---")

            # ── Passenger 2 ──────────────────────────────
            section("🟠 Passenger 2 — HITL Escalation Path")
            run_passenger2()

            st.markdown("---")

            # ── Reset button ─────────────────────────────
            if st.button("🔄 Reset Simulation", use_container_width=False):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                init_state()
                st.rerun()

    # ── Footer ───────────────────────────────────────────
    st.markdown(
        """
        <div style="text-align:center; margin-top:48px; padding:24px; border-top:1px solid #1E3A5F;">
            <p style="color:#64748B; font-size:0.8rem;">
                AeroRecover — Team Lakeside_Logic · IIM Mumbai · Case 7: Travel, Hospitality & Aviation<br>
                Neuro-Symbolic AI · Human-Governed · DGCA-Native Compliance
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
