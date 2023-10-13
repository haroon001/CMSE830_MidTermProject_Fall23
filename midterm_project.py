import streamlit as st
import pandas as pd
import json
import numpy as np
import seaborn as sns

def load_csv(csv_path, save = False):
	with pd.read_csv(csv_path, iterator=True) as reader:
		chunk_df = reader.get_chunk(10000)	
		chunk_df.sort_values(by='date', inplace = True)
		print(chunk_df['date'].iloc[0], chunk_df['date'].iloc[5000], chunk_df['date'].iloc[-1])
		
		if save:
			chunk_df.to_csv('/home/builder/Downloads/CMSE/gcrp_50K.csv', index=False)

	return chunk_df


if __name__=='__main__':

	path = 'gcrp_5K.csv'
	df = pd.read_csv(path)
	df.dropna(inplace = True)

	st.write("Users distribution globally.")
	st.map(df, latitude='lat', longitude='long')