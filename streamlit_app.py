import streamlit as st
from stmol import showmol, render_pdb, obj_upload
import py3Dmol
import requests
import tempfile

st.set_page_config(layout = 'wide')


# ESMfold

DEFAULT_SEQ = "MGSSHHHHHHSSGLVPRGSHMRGPNPTAASLEASAGPFTVRSFTVSRPSGYGAGTVYYPTNAGGTVGAIAIVPGYTARQSSIKWWGPRLASHGFVVITIDTNSTLDQPSSRSSQQMAALRQVASLNGTSSSPIYGKVDTARMGVMGWSMGGGGSLISAANNPSLKAAAPQAPWDSSTNFSSVTVPTLIFACENDSIAPVNSSALPIYDSMSRNAKQFLEINGGSHSCANSGNSNQALIGKKGVAWMKRFMDNDTRYSTFACENPNSTRVSDFRTANCSLEDPAANKARKEAELAAATAEQ"

txt = st.text_area('Input sequence', DEFAULT_SEQ)
st.write(txt)

#st.button('Predict', on_click=update)

# The App

st.title('🎈 ESMfold')

#uploaded_file = st.sidebar.file_uploader('Upload PDB file')

##showmol(render_pdb(id = '3EQM'))

#if uploaded_file is not None:
#  showmol(obj_upload(uploaded_file).setStyle({'cartoon':{'color':'spectrum'}}) )
#else:
#  st.info('Awaiting input ...')
