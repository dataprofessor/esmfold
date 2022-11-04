import streamlit as st
from stmol import showmol, render_pdb
import py3Dmol

st.set_page_config(layout = 'wide')

st.title('🎈 ESMfold')

showmol(render_pdb(id = '3EQM'))
