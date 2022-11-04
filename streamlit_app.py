import streamlit as st
from stmol import showmol, render_pdb, obj_upload
import py3Dmol
from transformers import AutoTokenizer, EsmForProteinFolding

# ESMfold
tokenizer = AutoTokenizer.from_pretrained("facebook/esmfold_v1")
model = EsmForProteinFolding.from_pretrained("facebook/esmfold_v1", low_cpu_mem_usage=True)

model = model.cuda()

# The App
st.set_page_config(layout = 'wide')

st.title('🎈 ESMfold')

uploaded_file = st.sidebar.file_uploader('Upload PDB file')

#showmol(render_pdb(id = '3EQM'))

if uploaded_file is not None:
  showmol(obj_upload(uploaded_file).setStyle({'cartoon':{'color':'spectrum'}}) )
else:
  st.info('Awaiting input ...')
