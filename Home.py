import streamlit as st
import pandas as pd

st.set_page_config(page_title="NEET Cuttoff", layout="wide")

rounds = {
    '2022':['R1', 'R2', 'MOPUP_R1', 'MOPUP_R2', 'STRAY_R1'],
    '2023':['R1', 'R2', 'R3', 'STRAY_R1', 'STRAY_R2', 'STRAY_R3']
}

years = ['2023', '2022']

courses = ['MBBS', 'BDS', 'B.Sc. Nursing']

quotas = ['Open Seat Quota',
 'All India',
 'Foreign Country Quota',
 'Deemed/Paid Seats Quota',
 'Non-Resident Indian',
 'Delhi NCR Children/Widows of Personnel of the Armed Forces (CW) Quota',
 'IP University Quota',
 'B.Sc Nursing All India',
 'B.Sc Nursing Delhi NCR (CW) Quota',
 'B.Sc Nursing Delhi NCR',
 'Aligarh Muslim University (AMU) Quota',
 'Non-Resident Indian (AMU) Quota',
 'Employees State Insurance Scheme (ESI)',
 'Jamia Internal Quota',
 'Muslim OBC Quota',
 'Muslim Quota',
 'Muslim ST Quota',
 'Muslim Women Quota',
 'Muslim Minority Quota',
 'Internal Puducherry UT Domicile',
 'Jain Minority Quota',
 'Delhi University Quota',
 'Christian Minority Quota'
]

categories = ['Open',
 'EWS',
 'OBC',
 'SC',
 'ST',
 'OBC PwD', 
 'Open PwD',
 'SC PwD',
 'EWS PwD',
 'ST PwD'
]

year_col, course_col, quota_col, category_col, r_col = st.columns(5)

year = year_col.selectbox("Year", years)

course = course_col.selectbox("Course", courses)

quota = quota_col.selectbox("Quota", quotas)

category = category_col.selectbox("Category", categories)

r = r_col.selectbox("Round", rounds[year])

df = pd.read_csv(f'{year}/C_{r}.csv')

df = df[ (df['Course']==course) & (df['Quota']==quota) & (df['Category']==category)]

if len(df)==0:
    st.error("NO DATA")
else:
    df = df[["Rank", "Institute"]].sort_values('Rank')
    st.dataframe(df, hide_index=True, use_container_width=True)

