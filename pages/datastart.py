import streamlit as st
st.set_page_config(page_title="Start data log")
st.title("start Logging")
st.header("you can start logging your farm data here")

fv={
    "name":None,
    "area":None,
    "past crops grown":None,
    "seed type":None,
    "farming method to be used":None,
    "irrigation type":None,
    "expected harvest period":None,
    "season cycle":None,
    "ph":None,
    "soil type":None,
    "fertilizer type":None
}

ideal_conditions = {
    "Rice": {"ph": (5.5, 7.0), "soil": ["Clay", "Silty Clay", "Loam"], "season": ["monsoon"]},
    "Wheat": {"ph": (6.0, 7.5), "soil": ["Loam", "Clay"], "season": ["winter"]},
    "Maize": {"ph": (5.5, 7.0), "soil": ["Loam", "Sandy"], "season": ["summer", "monsoon"]},
    "Sugarcane": {"ph": (6.0, 8.0), "soil": ["Loam", "Clay"], "season": ["summer", "monsoon"]},
    "Cotton": {"ph": (5.8, 8.0), "soil": ["Sandy", "Loam"], "season": ["summer"]},
    "Pulses": {"ph": (6.0, 7.5), "soil": ["Loam", "Sandy"], "season": ["winter", "autunm"]},
    "Soybean": {"ph": (6.0, 7.5), "soil": ["Loam", "Clay"], "season": ["monsoon"]},
    "Groundnut": {"ph": (6.0, 7.5), "soil": ["Sandy", "Loam"], "season": ["summer"]},
    "Mustard": {"ph": (6.0, 7.5), "soil": ["Loam"], "season": ["winter"]},
    "Barley": {"ph": (6.0, 7.5), "soil": ["Loam", "Sandy"], "season": ["winter"]},
    "Millets": {"ph": (5.5, 7.0), "soil": ["Sandy", "Loam"], "season": ["summer"]},
    "Tea": {"ph": (4.5, 5.5), "soil": ["Loam", "Clay"], "season": ["monsoon"]},
    "Coffee": {"ph": (5.0, 6.0), "soil": ["Loam", "Clay"], "season": ["monsoon"]},
    "Jute": {"ph": (6.0, 7.0), "soil": ["Loam", "Clay"], "season": ["monsoon"]},
    "Potatoes": {"ph": (5.0, 6.0), "soil": ["Sandy", "Loam"], "season": ["winter"]},
    "Onions": {"ph": (6.0, 7.0), "soil": ["Loam"], "season": ["winter", "summer"]},
    "Bananas": {"ph": (5.5, 7.0), "soil": ["Loam", "Clay"], "season": ["monsoon", "summer"]},
    "Turmeric": {"ph": (5.5, 7.5), "soil": ["Loam"], "season": ["monsoon"]},
    "Chillies": {"ph": (6.0, 7.0), "soil": ["Loam", "Sandy"], "season": ["summer", "monsoon"]},
    "Gram": {"ph": (6.0, 7.5), "soil": ["Loam"], "season": ["winter"]},
    "Arhar": {"ph": (6.0, 7.5), "soil": ["Loam", "Sandy"], "season": ["monsoon", "autunm"]}
}
st.sidebar.success("pick something")
with st.form(key="sample form"):
    st.header("Initial Farm Log")
    fv["name"]=st.selectbox("The crop being grown",['Rice','Wheat','Maize','Sugarcane','Cotton','Pulses','Oilseeds','Soybean','Groundnut','Mustard','Barley','Millets','Tea','Coffee','Jute','Tobacco','Potatoes','Onions','Bananas','Turmeric','Chillies','Gram',' Arhar'])
    fv["area"]=st.text_input("Area of growth( in sq feet)")
    fv["past crops grown"]=st.text_input("wt crops were grown in the past on the same soil")
    fv["seed type"]= st.selectbox("Seed Type", ['Hybrid', 'Local Variety', 'High-Yield Variety'])
    fv["farming method to be used"]= st.selectbox("Farming Method", ['Traditional', 'Organic', 'Modern/Mechanized'])
    fv["irrigation type"]= st.selectbox("Irrigation Source", ['Rain-fed', 'Borewell', 'Canal', 'Tank', 'Drip Irrigation'])
 
    fv["expected harvest period"]=st.text_input("Expected time to harvest from start of growth")
    fv["season cycle"]=st.selectbox("wt was the season during the crop cycle",['summer','autunm','monsoon','winter','spring'])
    fv["ph"]=st.select_slider("select soil PH quality:",options=[1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    fv["soil type"]=st.selectbox("soil type",['Sandy','Clay','Silt','Loam','Peat','Chalk'])
    fv["fertilizer type"]=st.selectbox("fertilizer used",['organic','chemical','none at all'])
    submit_ans=st.form_submit_button(label="submit")
    if submit_ans:
        if not all (fv.values()):
            st.warning("pls fill all the details")
        else:
            st.write("###info")
            for (key,value) in fv.items():
                st.write(f"{key}:{value}")
        for key, value in fv.items():
         st.text(f"{key}: {value}")


    

if submit_ans:
    st.subheader("🧠 Smart Crop Suitability Report")

    ideal = ideal_conditions[fv["name"]]
    issues = []

    
    if not (ideal["ph"][0] <= fv["ph"]<= ideal["ph"][1]):
        issues.append(f"❌ Soil pH {fv["ph"]} not suitable. Ideal range: {ideal['ph'][0]} - {ideal['ph'][1]}")

    
    if fv["soil type"] not in ideal["soil"]:
        issues.append(f"❌ Soil type '{fv["soil type"]}' not ideal. Recommended: {', '.join(ideal['soil'])}")

    
    if fv["season cycle"] not in ideal["season"]:
        issues.append(f"❌ Crop is usually grown in {', '.join(ideal['season'])} season(s), not {fv["season cycle"]}")

    
    if issues:
        st.error("⚠️ Some conditions may affect crop yield:")
        for i in issues:
            st.write(i)
    else:
        st.balloons()
        st.success("✅ All conditions are suitable for this crop!")

if st.button("Now let's move on to weekly update"):
    st.switch_page("pages/weeklyupdate.py")