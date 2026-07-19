import streamlit as st

from services.asset_service import get_assets

st.set_page_config(
    page_title="Asset 360",
    page_icon="🏭"
)

st.title("🏭 Asset 360")

assets = get_assets()

if len(assets) == 0:

    st.warning("No processed assets found.")

    st.stop()

names = []

for asset in assets:

    names.append(asset.get("Equipment", "Unknown"))

selected = st.selectbox(

    "Select Asset",

    names

)

asset = assets[names.index(selected)]

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.metric(

        "Equipment",

        asset.get("Equipment", "-")

    )

    st.metric(

        "Equipment Tag",

        asset.get("Equipment Tag", "-")

    )

    st.metric(

        "Temperature",

        asset.get("Temperature", "-")

    )

with col2:

    st.metric(

        "Failure",

        asset.get("Failure", "-")

    )

    st.metric(

        "Maintenance Action",

        asset.get("Maintenance Action", "-")

    )

    st.metric(

        "Person",

        asset.get("Person", "-")

    )

st.divider()

st.json(asset)