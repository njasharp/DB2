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

st.markdown("<style>body {background-color: #212121;}</style>", unsafe_allow_html=True)
# Custom CSS to hide the Streamlit menu and footer
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)



# Streamlit app
st.sidebar.title("Data Analysis - Mobile Games May2024")
st.info("built by dw - v1")
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
                                                                                 "Area Chart", "Scatter Plot", "Heat Map", "Pictogram Chart"], index=1)
most_downloaded_combined = st.sidebar.radio("Most Downloaded - Combined", ["Bar Chart", "Pie Chart", "Histogram", "Box and Whisker Plot", 
                                                                           "Area Chart", "Scatter Plot", "Heat Map", "Pictogram Chart"], index=2)
highest_earning_ios = st.sidebar.radio("Highest Earning - iOS", ["Bar Chart", "Pie Chart", "Histogram", "Box and Whisker Plot", 
                                                                 "Area Chart", "Scatter Plot", "Heat Map", "Pictogram Chart"], index=1)
highest_earning_google_play = st.sidebar.radio("Highest Earning - Google Play", ["Bar Chart", "Pie Chart", "Histogram", "Box and Whisker Plot", 
                                                                                 "Area Chart", "Scatter Plot", "Heat Map",  "Pictogram Chart"], index=2)
highest_earning_combined = st.sidebar.radio("Highest Earning - Combined", ["Bar Chart", "Pie Chart", "Histogram", "Box and Whisker Plot", 
                                                                           "Area Chart", "Scatter Plot", "Heat Map", "Pictogram Chart"], index=5)

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
if st.sidebar.checkbox("Show Statistics", value=True):
    if st.sidebar.checkbox("Show Most Downloaded Data", value=True):
        st.markdown("### Most Downloaded Games")
        st.dataframe(most_downloaded_df)

    if st.sidebar.checkbox("Show Highest Earning Data", value=True):
        st.markdown("### Highest Earning Games")
        st.dataframe(highest_earning_df)

st.markdown("""

In May 2024, the gaming market saw significant activity with notable trends in both downloads and revenue generation across the iOS App Store and Google Play. On the iOS App Store, "Brawl Stars" and "Block Blast!" each led the downloads with 4 million installs, followed closely by "Roblox," "Subway Surfers," and "Happy Fishing," each with 3 million installs. The Google Play store showed an even higher volume of downloads, with "Pizza Ready!" and "Subway Surfers" each reaching 19 million installs, and "Ludo King™" achieving 15 million installs.

When considering combined totals across both platforms, "Subway Surfers" and "Pizza Ready!" topped the charts with 22 million downloads each, followed by "Ludo King™" with 16 million and "Roblox" with 15 million installs. Other notable mentions include "Wood Nuts & Bolts" with 15 million and "Block Blast!" with 14 million downloads.

In terms of revenue, "King of Glory" dominated the iOS App Store, generating 131 million, while "MONOPOLY GO!" and "Peace Elite" followed with 96 million and 90 million, respectively. On Google Play, "Royal Match" led the earnings with 28 million, with "Coin Master" and "Candy Crush Saga" each earning 27 million.

Combining revenue from both platforms, "King of Glory" maintained its top position with 131 million in earnings. "MONOPOLY GO!" and "Royal Match" also performed strongly with 116 million and 96 million, respectively. "Peace Elite" earned 90 million, and "Candy Crush Saga" rounded out the top five with 70 million in revenue.

These findings highlight the significant engagement and spending within the mobile gaming market, with certain games consistently performing well across both downloads and revenue metrics.

In May 2024, the mobile gaming landscape was dominated by a mix of action, puzzle, and simulation games. Here's a breakdown of the leading genres and why they performed so well:

### Action Games
**Top Games: Brawl Stars, Free Fire, Free Fire MAX**
- **Brawl Stars:** This game led the downloads on the iOS App Store with 4 million installs. Its success can be attributed to its fast-paced, multiplayer gameplay which keeps players engaged and coming back for more. The game's regular updates, events, and a strong community also contribute to its popularity.
- **Free Fire and Free Fire MAX:** These battle royale games continue to attract a large player base due to their accessible gameplay, short match times, and extensive customization options. Their strong presence on Google Play with millions of downloads highlights their appeal in diverse markets.

### Puzzle Games
**Top Games: Block Blast!, Candy Crush Saga, Wood Nuts & Bolts**
- **Block Blast!:** Ranking high in downloads on both iOS and Google Play, this puzzle game combines simple mechanics with challenging levels, making it highly addictive. Puzzle games like Block Blast! are known for their broad appeal, attracting both casual and hardcore gamers.
- **Candy Crush Saga:** Despite being a veteran in the mobile gaming space, Candy Crush Saga continues to generate substantial revenue. Its enduring popularity is driven by its easy-to-learn but hard-to-master gameplay, frequent updates, and social features that encourage competition among friends.

### Simulation Games
**Top Games: Pizza Ready!, Township, MONOPOLY GO!**
- **Pizza Ready!:** This simulation game saw remarkable success, especially on Google Play, with 19 million downloads. Its engaging gameplay, which involves managing a virtual pizza restaurant, appeals to players who enjoy strategy and time management elements.
- **Township:** Another simulation game that performed well on iOS, Township combines city-building with farming, offering a varied and immersive experience. Its blend of different gameplay elements keeps players engaged over the long term.
- **MONOPOLY GO!:** Generating significant revenue on both platforms, this game leverages the familiar Monopoly brand, adding new features and mechanics to attract both old fans and new players.

### Social and Multiplayer Games
**Top Games: Roblox, Ludo King™**
- **Roblox:** This platform continues to dominate with high download numbers and revenue. Roblox's success lies in its user-generated content model, allowing players to create and share their own games. This leads to a vast and ever-evolving library of content, ensuring there is always something new for players to explore.
- **Ludo King™:** This classic board game adaptation has found a large audience on mobile, particularly in regions where traditional board games are popular. Its simple rules, multiplayer options, and social features make it a favorite for casual gaming sessions with friends and family.

### Endless Runner Games
**Top Game: Subway Surfers**
- **Subway Surfers:** As one of the most downloaded games, Subway Surfers remains popular due to its easy-to-understand mechanics, vibrant graphics, and regular updates that introduce new challenges and themes. Its endless runner format appeals to players looking for quick, fun sessions.

These genres and their top-performing games highlight the diverse interests of mobile gamers. The success of these games can be attributed to their engaging gameplay, frequent updates, social features, and the ability to appeal to a wide audience. Whether it's the adrenaline rush of action games, the mental stimulation of puzzles, the strategic depth of simulations, or the social interaction in multiplayer games, there's something for everyone in the mobile gaming world.
""")
