
import streamlit as st

st.set_page_config(page_title="Sangli Grape Export Connect", page_icon="🍇", layout="wide")

st.title("🍇 Sangli Grape Export Connect")
st.write("Grape Export Readiness Platform | Sangli, Maharashtra")

tab1, tab2, tab3 = st.tabs([
    "Farmer Registration",
    "Export Readiness",
    "Buyer & Logistics"
])

with tab1:
    st.subheader("Farmer Registration")
    with st.form("farmer"):
        name = st.text_input("Farmer Name")
        village = st.text_input("Village")
        variety = st.selectbox("Grape Variety", [
            "Thompson Seedless", "Sonaka", "Flame Seedless", "Other"
        ])
        quantity = st.number_input("Quantity (tonnes)", min_value=0.0)
        phone = st.text_input("Contact Number")
        submit = st.form_submit_button("Register Farmer")

        if submit:
            if name.strip() and village.strip() and phone.strip() and quantity > 0:
                st.success(f"Registration received for {name}!")
                st.write(village, variety, f"{quantity} tonnes")
            else:
                st.error("Please fill all fields correctly.")

with tab2:
    st.subheader("Export Readiness Checklist")
    tasks = [
        "Farm traceability records",
        "Quality testing requirements",
        "Certification requirements",
        "Packaging and labelling",
        "Export documentation",
        "Cold-chain logistics"
    ]
    done = sum(st.checkbox(task, key=f"task{i}") for i, task in enumerate(tasks))
    st.progress(done / len(tasks))
    st.write(f"{done}/{len(tasks)} tasks completed")

with tab3:
    st.subheader("Buyer & Logistics Enquiry")
    with st.form("enquiry"):
        contact = st.text_input("Contact Person / Organisation")
        kind = st.selectbox("Enquiry Type", [
            "Buyer Enquiry", "Freight / Logistics", "Export Support"
        ])
        destination = st.text_input("Destination / Route")
        details = st.text_area("Requirement Details")
        send = st.form_submit_button("Submit Enquiry")

        if send:
            if contact.strip() and details.strip():
                st.success("Enquiry received in this demo.")
            else:
                st.error("Enter contact name and requirement.")

st.divider()
st.caption("Student MVP Prototype | Sangli, Maharashtra")
