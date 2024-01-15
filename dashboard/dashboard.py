# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(style='dark')

# get data
main_df = pd.read_csv('dashboard/hour_modified.csv')

# main title
st.title("Bike Sharing Dataset Analysis")


# first plot about distribution of bike sharing based on season
st.header("Distribution of bike sharing based on day")
fig, ax = plt.subplots(figsize=(15, 6))
hue_order = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

sns.lineplot(x='hour', y='total_users', hue='weekday', palette='bright', hue_order=hue_order, data=main_df)
ax.set_title('Distribution of users per hour based on day', fontsize=15)
ax.set_xlabel('Hour', fontsize=15)
ax.set_xticks(range(0, 24))
ax.set_ylabel('Total users', fontsize=15)
ax.legend(loc='upper right', fontsize=15, title='Day', title_fontsize=15)
st.pyplot(fig)


# second plot about distribution of bike sharing based on weather
st.header("Distribution of users based on workdays")
fig, ax1 = plt.subplots(figsize=(15, 6))
hue_order = [1, 0]

sns.lineplot(x='hour', y='casual_users', hue='is_working_day', hue_order=hue_order,
             palette='bright', data=main_df, ax=ax1)
ax1.set_title('Distribution of casual users per hour based on workday', fontsize=15)
ax1.set_xlabel('Hour', fontsize=15)
ax1.set_xticks(range(0, 24))
ax1.set_ylabel('Casual users', fontsize=15)
ax1.legend(loc='upper right', fontsize=15, title='Workday', title_fontsize=15, labels=['Yes', 'No'], handles=ax1.lines[::len(hue_order)+1])
st.pyplot(fig)


# third plot about distribution of bike sharing based on weather
fig, ax2 = plt.subplots(figsize=(15, 6))
hue_order = [1, 0]

sns.lineplot(x='hour', y='registered_users', hue='is_working_day', hue_order=hue_order,
             palette='bright', data=main_df, ax=ax2)
ax2.set_title('Distribution of registered users per hour based on workday', fontsize=15)
ax2.set_xlabel('Hour', fontsize=15)
ax2.set_xticks(range(0, 24))
ax2.set_ylabel('Registered users', fontsize=15)
ax2.legend(loc='upper right', fontsize=15, title='Workday', title_fontsize=15, labels=['Yes', 'No'], handles=ax2.lines[::len(hue_order)+1])
st.pyplot(fig)


# fourth plot about distribution of bike sharing based on weather
st.header("Correlation between temperature and bike sharing")
fig, ax = plt.subplots(figsize=(15, 6))

sns.regplot(x='temperature', y='total_users', line_kws=dict(color="b"), data=main_df)
ax.set_title('Distribution of users by temperature', fontsize=15)
ax.set_xlabel('Temperature', fontsize=15)
ax.set_ylabel('Total Users', fontsize=15)
st.pyplot(fig)