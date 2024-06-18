import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff

# Data
most_downloaded_data = {
    "Platform": ["iOS App Store", "iOS App Store", "iOS App Store", "iOS App Store", "iOS App Store", 
                 "iOS App Store", "iOS App Store", "iOS App Store", "iOS App Store", "iOS App Store",
                 "Google Play", "Google Play", "Google Play", "Google Play", "Google Play",
                 "Google Play", "Google Play", "Google Play", "Google Play", "Google Play",
                 "Combined Total", "Combined Total", "Combined Total", "Combined Total", "Combined Total",
                 "Combined Total", "Combined Total", "Combined Total", "Combined Total", "Combined Total"],
    "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
             1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Game": ["Brawl Stars", "Block Blast!", "Roblox", "Subway Surfers", "Happy Fishing",
             "Last War", "DNF Mobile", "Pizza Ready!", "Township", "Whiteout Survival",
             "Pizza Ready!", "Subway Surfers", "Ludo King™", "Wood Nuts & Bolts", "Free Fire MAX",
             "Roblox", "Relax Mini Games", "Free Fire", "Block Blast!", "Subway Princess Runner",
             "Subway Surfers", "Pizza Ready!", "Ludo King™", "Roblox", "Wood Nuts & Bolts",
             "Block Blast!", "Free Fire MAX", "Free Fire", "Relax Mini Games", "Brawl Stars"],
    "Downloads (M)": [4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 
                      19, 19, 15, 13, 13, 12, 12, 11, 10, 10,
                      22, 22, 16, 15, 15, 14, 13, 13, 12, 12]
}

highest_earning_data = {
    "Platform": ["iOS App Store", "iOS App Store", "iOS App Store", "iOS App Store", "iOS App Store", 
                 "iOS App Store", "iOS App Store", "iOS App Store", "iOS App Store", "iOS App Store",
                 "Google Play", "Google Play", "Google Play", "Google Play", "Google Play",
                 "Google Play", "Google Play", "Google Play", "Google Play", "Google Play",
                 "Combined Total", "Combined Total", "Combined Total", "Combined Total", "Combined Total",
                 "Combined Total", "Combined Total", "Combined Total", "Combined Total", "Combined Total"],
    "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
             1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Game": ["King of Glory", "MONOPOLY GO!", "Peace Elite", "Royal Match", "Brawl Stars",
             "Roblox", "DNF Mobile", "Candy Crush Saga", "Last War", "Fantasy",
             "Royal Match", "Coin Master", "Candy Crush Saga", "Last War", "Whiteout Survival",
             "Roblox", "MONOPOLY GO!", "Gardenscapes", "Brawl Stars", "Fishdom",
             "King of Glory", "MONOPOLY GO!", "Royal Match", "Peace Elite", "Candy Crush Saga",
             "Roblox", "Last War", "Brawl Stars", "Whiteout Survival", "Coin Master"],
    "Revenue ($M)": [131, 96, 90, 68, 45, 45, 44, 43, 39, 36, 
                     28, 27, 27, 21, 20, 19, 19, 15, 14, 12,
                     131, 116, 96, 90, 70, 64, 63, 59, 51, 50]
}

# Convert to DataFrames
most_downloaded_df = pd.DataFrame(most_downloaded_data)
highest_earning_df = pd.DataFrame(highest_earning_data)

# Streamlit app
st.set_page_config(layout="wide")
st.sidebar.title("Data Analysis - Mobile Games May2024")
st.info("build by dw - global")
st.image("gsmetop.png")
# Show checkboxes at the top of the sidebar
show_most_downloaded_ios = st.sidebar.checkbox("Show Most Downloaded - iOS", value=True)
show_most_downloaded_google_play = st.sidebar.checkbox("Show Most Downloaded - Google Play", value=True)
show_most_downloaded_combined = st.sidebar.checkbox("Show Most Downloaded - Combined", value=True)
show_highest_earning_ios = st.sidebar.checkbox("Show Highest Earning - iOS", value=True)
show_highest_earning_google_play = st.sidebar.checkbox("Show Highest Earning - Google Play", value=True)
show_highest_earning_combined = st.sidebar.checkbox("Show Highest Earning - Combined", value=True)

# Sidebar selection for data types
st.sidebar.markdown("### Select Data Types")
most_downloaded_ios = st.sidebar.radio("Most Downloaded - iOS", ["Bar Chart", "Pie Chart", "Histogram", "Box and Whisker Plot", 
                                                                 "Area Chart", "Scatter Plot", "Heat Map", "Pictogram Chart"], index=0)
most_downloaded_google_play = st.sidebar.radio("Most Downloaded - Google Play", ["Bar Chart", "Pie Chart", "Histogram", "Box and Whisker Plot", 
                                                                                 "Area Chart", "Scatter Plot", "Heat Map", "Pictogram Chart"], index=0)
most_downloaded_combined = st.sidebar.radio("Most Downloaded - Combined", ["Bar Chart", "Pie Chart", "Histogram", "Box and Whisker Plot", 
                                                                           "Area Chart", "Scatter Plot", "Heat Map", "Pictogram Chart"], index=0)
highest_earning_ios = st.sidebar.radio("Highest Earning - iOS", ["Bar Chart", "Pie Chart", "Histogram", "Box and Whisker Plot", 
                                                                 "Area Chart", "Scatter Plot", "Heat Map", "Pictogram Chart"], index=0)
highest_earning_google_play = st.sidebar.radio("Highest Earning - Google Play", ["Bar Chart", "Pie Chart", "Histogram", "Box and Whisker Plot", 
                                                                                 "Area Chart", "Scatter Plot", "Heat Map",  "Pictogram Chart"], index=0)
highest_earning_combined = st.sidebar.radio("Highest Earning - Combined", ["Bar Chart", "Pie Chart", "Histogram", "Box and Whisker Plot", 
                                                                           "Area Chart", "Scatter Plot", "Heat Map", "Pictogram Chart"], index=0)

# Function to create charts with smaller size
def create_chart(df, x_col, y_col, title, chart_type):
    fig_size = (8, 5)  # Adjust figure size here (width, height)
    if chart_type == "Bar Chart":
        fig, ax = plt.subplots(figsize=fig_size)
        df.plot(kind='bar', x=x_col, y=y_col, ax=ax, legend=False)
        ax.set_title(title)
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        st.pyplot(fig)
    elif chart_type == "Pie Chart":
        fig, ax = plt.subplots(figsize=fig_size)
        df.set_index(x_col).plot(kind='pie', y=y_col, ax=ax, legend=False, autopct='%1.1f%%')
        ax.set_ylabel('')
        ax.set_title(title)
        st.pyplot(fig)
    elif chart_type == "Histogram":
        fig, ax = plt.subplots(figsize=fig_size)
        df[y_col].plot(kind='hist', ax=ax, legend=False)
        ax.set_title(title)
        ax.set_xlabel(y_col)
        st.pyplot(fig)
    elif chart_type == "Box and Whisker Plot":
        fig, ax = plt.subplots(figsize=fig_size)
        sns.boxplot(data=df, x=x_col, y=y_col, ax=ax)
        ax.set_title(title)
        st.pyplot(fig)
    elif chart_type == "Area Chart":
        fig, ax = plt.subplots(figsize=fig_size)
        df.plot(kind='area', x=x_col, y=y_col, ax=ax, legend=False)
        ax.set_title(title)
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        st.pyplot(fig)
    elif chart_type == "Scatter Plot":
        fig, ax = plt.subplots(figsize=fig_size)
        df.plot(kind='scatter', x=x_col, y=y_col, ax=ax, legend=False)
        ax.set_title(title)
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        st.pyplot(fig)
    elif chart_type == "Heat Map":
        fig, ax = plt.subplots(figsize=fig_size)
        sns.heatmap(df[[x_col, y_col]].pivot_table(index=x_col, values=y_col, aggfunc='sum'), ax=ax, annot=True, fmt="d")
        ax.set_title(title)
        st.pyplot(fig)

    elif chart_type == "Pictogram Chart":
        fig = px.pie(df, values=y_col, names=x_col, title=title, height=300)  # Adjust height for plotly chart
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig)


# Display selected charts
if show_most_downloaded_ios:
    df = most_downloaded_df[most_downloaded_df["Platform"] == "iOS App Store"]
    create_chart(df, "Game", "Downloads (M)", "Most Downloaded Games - iOS App Store", most_downloaded_ios)

if show_most_downloaded_google_play:
    df = most_downloaded_df[most_downloaded_df["Platform"] == "Google Play"]
    create_chart(df, "Game", "Downloads (M)", "Most Downloaded Games - Google Play", most_downloaded_google_play)

if show_most_downloaded_combined:
    df = most_downloaded_df[most_downloaded_df["Platform"] == "Combined Total"]
    create_chart(df, "Game", "Downloads (M)", "Most Downloaded Games - Combined Total", most_downloaded_combined)

if show_highest_earning_ios:
    df = highest_earning_df[highest_earning_df["Platform"] == "iOS App Store"]
    create_chart(df, "Game", "Revenue ($M)", "Highest Earning Games - iOS App Store", highest_earning_ios)

if show_highest_earning_google_play:
    df = highest_earning_df[highest_earning_df["Platform"] == "Google Play"]
    create_chart(df, "Game", "Revenue ($M)", "Highest Earning Games - Google Play", highest_earning_google_play)

if show_highest_earning_combined:
    df = highest_earning_df[highest_earning_df["Platform"] == "Combined Total"]
    create_chart(df, "Game", "Revenue ($M)", "Highest Earning Games - Combined Total", highest_earning_combined)

# Sidebar statistics
st.sidebar.markdown("## Statistics")
if st.sidebar.checkbox("Show Statistics"):
    if st.sidebar.checkbox("Show Most Downloaded Data"):
        st.sidebar.markdown("### Most Downloaded Games")
        st.sidebar.dataframe(most_downloaded_df)

    if st.sidebar.checkbox("Show Highest Earning Data"):
        st.sidebar.markdown("### Highest Earning Games")
        st.sidebar.dataframe(highest_earning_df)