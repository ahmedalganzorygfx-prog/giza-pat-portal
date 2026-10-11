import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="المنصة الرقمية - الأكاديمية المهنية للمعلمين فرع الجيزة",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تنسيقات الهوية البصرية الرسمية (Custom CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: #f4f6f9;
    }

    .header-container {
        background: linear-gradient(135deg, #10233F 0%, #1e3d6b 100%);
        padding: 30px 20px;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 8px 20px rgba(16, 35, 63, 0.15);
        border-bottom: 5px solid #C9A227;
    }
    
    .header-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 8px;
        color: #ffffff;
    }
    
    .header-subtitle {
        font-size: 1.1rem;
        color: #C9A227;
        font-weight: 600;
    }

    .service-card {
        background: #ffffff;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
        border-right: 6px solid #C9A227;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.3s ease;
    }

    .service-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.08);
        border-right-color: #10233F;
    }

    .card-header {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .card-icon {
        font-size: 2rem;
        background: #f8fafc;
        padding: 8px 12px;
        border-radius: 10px;
        border: 1px solid #edf2f7;
    }

    .card-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #10233F;
        margin: 0;
    }

    .card-desc {
        color: #64748b;
        font-size: 0.92rem;
        margin-top: 10px;
        line-height: 1.5;
    }

    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        color: #64748b;
        font-size: 0.9rem;
        border-top: 1px solid #e2e8f0;
    }
    </style>
""", unsafe_allow_html=True)

# الهيدر الرئيسي
st.markdown("""
    <div class="header-container">
        <div class="header-title">🏛️ المنصة الرقمية الموحدة</div>
        <div class="header-subtitle">الأكاديمية المهنية للمعلمين - فرع الجيزة</div>
    </div>
""", unsafe_allow_html=True)

# قائمة المستودعات والأنظمة الـ 8
systems = [
    {
        "title": "حضور وانصراف العاملين",
        "desc": "نظام متابعة وتسجيل حضور وانصراف الموظفين بالفرع.",
        "icon": "⏰",
        "url": "https://employee-attendance.streamlit.app"
    },
    {
        "title": "الأرشيف الرقمي للصادر والوارد",
        "desc": "إدارة وأرشفة المعاملات والمكاتبات الرسمية للفرع.",
        "icon": "📁",
        "url": "https://archive-system.streamlit.app"
    },
    {
        "title": "تجديد الشهادات",
        "desc": "متابعة وإصدار طلبات تجديد صلاحية الشهادات.",
        "icon": "📜",
        "url": "https://tagdeed-certificates.streamlit.app"
    },
    {
        "title": "سجل الأمن Smart Check-in",
        "desc": "نظام حماية وتسجيل حركة دخول المترددين والزوار.",
        "icon": "🛡️",
        "url": "https://smart-checkin-system.streamlit.app"
    },
    {
        "title": "نظام تذاكر أسبقية الحضور",
        "desc": "تنظيم أسبقية الدور وحجز تذاكر المراجعين بالفرع.",
        "icon": "🎫",
        "url": "https://attendance-system.streamlit.app"
    },
    {
        "title": "اختبارات الفرع",
        "desc": "منصة جدولة وتنظيم اختبارات المعلمين المعتمدة.",
        "icon": "📝",
        "url": "https://pat-giza-exams.streamlit.app"
    },
    {
        "title": "الخدمات الرقمية وإدارة البيانات",
        "desc": "قواعد البيانات المتكاملة والبرامج التدريبية للمعلمين.",
        "icon": "👨‍🏫",
        "url": "https://giza-academy-programms.streamlit.app"
    },
    {
        "title": "المنصة الإحصائية والتقارير",
        "desc": "عرض المؤشرات والإحصائيات التجميعية لخدمات الفرع.",
        "icon": "📊",
        "url": "https://giza-pat-analytics.streamlit.app"
    }
]

# عرض البطاقات
col1, col2 = st.columns(2)

for idx, sys in enumerate(systems):
    target_col = col1 if idx % 2 == 0 else col2
    
    with target_col:
        st.markdown(f"""
            <div class="service-card">
                <div>
                    <div class="card-header">
                        <span class="card-icon">{sys['icon']}</span>
                        <h3 class="card-title">{sys['title']}</h3>
                    </div>
                    <p class="card-desc">{sys['desc']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.link_button(
            label=f"الدخول إلى {sys['title']} 🔗",
            url=sys['url'],
            use_container_width=True
        )
        st.write("")

st.markdown("""
    <div class="footer">
        © جميع الحقوق محفوظة - المنصة الرقمية للأكاديمية المهنية للمعلمين فرع الجيزة
    </div>
""", unsafe_allow_html=True)
