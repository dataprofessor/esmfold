import streamlit as st
from stmol import showmol
import py3Dmol

st.title('🎈 ESMfold')

showmol(render_pdb(id = '1A2C'))
