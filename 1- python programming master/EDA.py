import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

def piechart(counts,selected_col,small_values_sum):
    st.subheader(f'A pie chart for `{selected_col}`')
    st.write('if there are values that has a small count all them will appear as other')

#if there is values that its repeatition is less then p(len(df)/100) will be added as other
    if small_values_sum[0] > p:
        new_row={'count':small_values}
        c = pd.concat([counts, pd.DataFrame([new_row], index=['Other'])])
        c=c['count']
    else:
        c=counts['count']

    plt.figure(figsize=(5,5))
    fig, ax = plt.subplots()
    ax.pie(c,labels=c.index.values.tolist(),rotatelabels=True)
    col1, col2, col3 = st.columns([2,10,2])
    with col2:
        st.pyplot(fig)
    st.write('---')    

def barchart(c,selected_col): 
    st.subheader(f'A bar chart for `{selected_col}`')
    plt.figure(figsize=(5,5))
    fig, ax = plt.subplots()
    ax.bar(c.T.columns,c['count'])
    ax.set_xlabel(f'{selected_col}')
    ax.set_ylabel('counts')
    plt.xticks(rotation=90)
    ax.grid(True)
    ol1, col2, col3 = st.columns([2,10,2])
    with col2:
        st.pyplot(fig)
    st.write('---')    


def histogram(c,selected_col): 
    st.subheader(f'A histogram chart for `{selected_col}`')
    plt.figure(figsize=(5,5))
    fig, ax = plt.subplots()
    values, bins , patches = ax.hist(c[selected_col],bins=50,edgecolor='white')
    for i in range(0,17):
        patches[i].set_facecolor('g')
    for i in range(17,34):
        patches[i].set_facecolor('r')
    for i in range(34,len(patches)):
        patches[i].set_facecolor('black')
    ax.set_xlabel(f'{selected_col}')
    ax.set_ylabel('frequency')
    ax.grid(True)
    plt.xlim(c[selected_col].min(),c[selected_col].max())
    ol1, col2, col3 = st.columns([2,10,2])
    with col2:
        st.pyplot(fig)   
    st.write('---')    


st.markdown("<h1 style='text-align: center;'>Automated Exploratory Data Analysis</h1>", unsafe_allow_html=True)
x=False

#uploading and reading data
data = st.file_uploader('Upload a CSV or excel file')

#checkin if the file is valied or not
if data:
    st.success('uploaded successfully')
    if data.name.split('.')[-1] == 'csv':
        df = pd.read_csv(data)
        x=True
    elif data.name.split('.')[-1] == 'xlsx':
        df = pd.read_excel(data)
        x=True
    else:
        st.error('please enter a valied file')
        x=False
st.write('---')

if x==True:
    
    df.drop_duplicates()
    tab1, tab2, tab3= st.tabs(["Data", "Unique values",'description'])
    tab1.subheader("there is the data")
    tab1.write(df)
    tab2.subheader("there are the unique values")
    tab2.write(pd.DataFrame(df.nunique()).T)
    tab3.subheader("there is the description of data")
    tab3.write(pd.DataFrame(df.describe()))

    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    string_cols = df.select_dtypes(include=['object']).columns
    
    selected_col_type=st.selectbox('Pick the type of columns',['','numerical','string'] )

    a=''
    if selected_col_type=='numerical':
        selected_col=st.selectbox('Pick columne',['',*numerical_cols])
        a=selected_col
    elif selected_col_type=='string':
        selected_col=st.selectbox('Pick columne', ['',*string_cols])   
        a=selected_col

    if a!='':
        col1, col2, col3 = st.columns([10,2,10])
        with col1:
            st.subheader(f'there is the `{a}` column ')
            st.write(pd.DataFrame(df[a]))
        
        counts = df[a].value_counts()
        counts=pd.DataFrame(counts)
        
        with col3:
            st.subheader(f'The number of repetition for each value in `{a}`')
            st.write(counts) 
        st.write('---')

#handling missing values
        if selected_col_type=='numerical':
            nan_percent = ((counts['count'].isna().sum()) / len(df)) *100
            if nan_percent >=40:
                counts.dropna(inplace=True)
            elif nan_percent >=20:
                counts.fillna(method='ffill',inplace=True)
            elif nan_percent <20 : 
                counts.fillna(counts['count'].median(),inplace=True)  
        elif selected_col_type=='string':
            counts.fillna('Missing', inplace=True)

        p = len(df) / 100 
        small_values = counts[counts < p].sum()
        counts=counts.drop(counts[counts['count'] < p].index)


        piechart(counts,a,small_values)
        barchart(counts,a)
        if selected_col_type=='numerical':
            histogram(df,a)



