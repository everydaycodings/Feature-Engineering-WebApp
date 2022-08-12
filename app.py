import streamlit as st
from helper import describe, display_null_per, data, display_outliers

st.set_page_config(
     page_title="Data Analysis Web App",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://github.com/everydaycodings/Data-Analysis-Web-App',
         'Report a bug': "https://github.com/everydaycodings/Data-Analysis-Web-App/issues/new",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
)

file_format_type = ["csv"]

st.sidebar.title("Data Analysis Web App")

uploaded_file = st.sidebar.file_uploader("Upload Your file", type=file_format_type)


if uploaded_file is not None:

    data = data(uploaded_file)

    describe, shape, columns, num_category, str_category, null_values, dtypes, unique, str_category, column_with_null_values = describe(data)

    max_nan_hold = st.sidebar.slider(label="Enter the Percentage of the max NaN Value acceptance", help="Enter The Percentage at which you can replace the NaN value if it exceeds the number you select that perticular column will be droped", min_value=1, max_value=100)
    ignore_outliers_col = st.sidebar.multiselect(label="Ignored Numeric Column for Outliers", help="Only Select those columns in which you dont want outliers to be applied.", options=num_category, default=None)

    if st.sidebar.button("Analysis Data"):

        st.header("Overview")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.text("Basic Information")
            st.write("Dataset Name")
            st.text(uploaded_file.name)

            st.write("Dataset Size(MB)")
            number = round((uploaded_file.size*0.000977)*0.000977,2)
            st.write(number)

            st.write("Dataset Shape")
            st.write(shape)
            
        with col2:
            st.text("Dataset Columns")
            st.write(columns)
        
        with col3:
            st.text("Numeric Columns")
            st.dataframe(num_category)
        
        with col4:
            st.text("String Columns")
            st.dataframe(str_category)
            

        col5, col6, col7, col8= st.columns(4)

        with col6:
            st.text("Columns Data-Type")
            st.dataframe(dtypes)
        
        with col7:
            st.text("Counted Unique Values")
            st.write(unique)
        
        with col5:
            st.write("Counted Null Values")
            st.dataframe(null_values)
    

        st.header("Analysis Result")

        col1, col2  = st.columns(2)

        with col1:
            st.text("Percentage of NaN Value in each column")
            st.dataframe(display_null_per(data, max_nan_hold))
        
        with col2:
            st.text("Outliers Caping in Numeric Columns")
            st.dataframe(display_outliers(data, ignore_outliers_col, num_cat=num_category))

