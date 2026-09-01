import pandas as pd
import plotly.express as px
import streamlit as st

st.sidebar.header('Controles')

dark_mode = st.sidebar.toggle('Modo oscuro')

if dark_mode:
    plotly_template = 'plotly_dark'
    graph_bg = '#0e1117'
    graph_text = 'white'
    subtitle_color = '#8AB4F8'

    st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #0e1117;
        color: white;
    }

    [data-testid="stSidebar"] {
        background-color: #161b22;
    }

    h1, h2, h3, p, label {
        color: white !important;
    }

  /* SELECTBOX - MODO OSCURO */

div[data-baseweb="select"] {
    background-color: white !important;
}

div[data-baseweb="select"] > div {
    background-color: white !important;
    border-color: #555 !important;
    color: #262730 !important;
}

div[data-baseweb="select"] div[role="combobox"] {
    background-color: white !important;
    color: #262730 !important;
}

div[data-baseweb="select"] div[role="combobox"] * {
    color: #262730 !important;
    -webkit-text-fill-color: #262730 !important;
}

div[data-baseweb="select"] svg {
    fill: #262730 !important;
    color: #262730 !important;
}

    /* Menú desplegable */

    div[data-baseweb="popover"] {
        background-color: #262730 !important;
    }

    ul[role="listbox"] {
        background-color: #262730 !important;
    }

    li[role="option"] {
        background-color: #262730 !important;
        color: white !important;
    }

li[role="option"] * {
    color: white !important;
}

li[role="option"]:hover {
    background-color: #3a3b44 !important;
    color: white !important;
}

    </style>
    """,
    unsafe_allow_html=True
)
else:
    plotly_template = 'plotly_white'
    graph_bg = 'white'
    graph_text = 'black'
    subtitle_color = '#315A8A'

    st.markdown(
        """
        <style>

        /* SELECTBOX - MODO CLARO */

    div[data-baseweb="select"] {
        background-color: white !important;
    }

    div[data-baseweb="select"] > div {
        background-color: white !important;
        border-color: #ccc !important;
        color: #262730 !important;
    }

    div[data-baseweb="select"] input {
        color: #262730 !important;
        -webkit-text-fill-color: #262730 !important;
    }

    div[data-baseweb="select"] span {
        color: #262730 !important;
    }
        
        </style>
        """,
        unsafe_allow_html=True
    )

car_data = pd.read_csv('vehicles_us.csv')

st.sidebar.divider()
st.sidebar.subheader('Filtros')

vehicle_types = ['Todos'] + sorted(
    car_data['type'].dropna().unique().tolist()
)

selected_type = st.sidebar.selectbox(
    'Tipo de vehículo',
    vehicle_types
)

if selected_type == 'Todos':
    filtered_data = car_data
else:
    filtered_data = car_data[
        car_data['type'] == selected_type
    ]

hist_button = st.sidebar.checkbox('Mostrar histograma')
scatter_button = st.sidebar.checkbox('Mostrar gráfico de dispersión')

st.header('Análisis de anuncios de vehículos')

st.markdown(
    f"""
    <p style="
        color: {subtitle_color};
        font-size: 16px;
        margin-top: 5px;
        margin-bottom: 20px;
    ">
        Explora la distribución del millaje y su relación con el precio de los vehículos.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    [data-testid="stMetric"] {
        background-color: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.10);
        padding: 14px 18px;
        border-radius: 12px;
    }

    [data-testid="stMetricLabel"] {
        font-size: 15px;
    }

    [data-testid="stMetricValue"] {
        font-size: 28px;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

col1.metric('Vehículos', f'{len(filtered_data):,}')
col2.metric(
    'Precio promedio',
    f"${filtered_data['price'].mean():,.0f}"
)
col3.metric(
    'Millaje promedio',
    f"{filtered_data['odometer'].mean():,.0f} mi"
)

st.divider()
st.subheader('Distribución del millaje')

if hist_button:

    fig = px.histogram(
        filtered_data,
        x='odometer',
        template=plotly_template
    )

    fig.update_layout(
        paper_bgcolor=graph_bg,
        plot_bgcolor=graph_bg,
        font_color=graph_text
    )
    st.plotly_chart(fig, width='stretch', theme=None)


st.divider()
st.subheader('Relación entre millaje y precio')

if scatter_button:

    fig = px.scatter(
        filtered_data,
        x='odometer',
        y='price',
        template=plotly_template
    )

    fig.update_layout(
        paper_bgcolor=graph_bg,
        plot_bgcolor=graph_bg,
        font_color=graph_text
    )
    st.plotly_chart(fig, width='stretch', theme=None)