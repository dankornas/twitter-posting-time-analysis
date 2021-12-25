# %%
import pandas as pd
from twitterscraper import scrapeProfile

# %% [markdown]
# ## Scrape your profile into a csv
# Set twitterUser to your Twitter handle.

# %%
twitterUser = 'yourTwitterHandleHere'

scrapeProfile(twitterUser, twitterUser+'.csv')

# %% [markdown]
# ## Open the created CSV in pandas and clean up data

# %%
# function for converting like counts such as 3.3k into numbers 3300
def convert_to_string(row):
    try:
        if type(row) == type(str()):
            if row.find('K') != -1:
                row = row.replace('.', '')
                row = row.replace('K', '')
                row = row + '00'
                return(int(row))
            else:
                return(int(row))
        else:
            return(row)
    except:
        print(row)

# %%
df = pd.read_csv('dankornas.csv')
df = df.drop(['User','Handle'], axis=1)
df = df.fillna(0)

df['LikeCount'] = df['LikeCount'].apply(convert_to_string)
df[['ReplyCount', 'RetweetCount', 'LikeCount']] = df[['ReplyCount', 'RetweetCount', 'LikeCount']].astype(int)

df.PostDate = pd.to_datetime(df.PostDate)

# %%
df

# %% [markdown]
# ## Create new features from dates

# %%
# extract month feature
months = df.PostDate.dt.month
months = pd.DataFrame(months)
months.columns = ['months']

# extract day of month feature
day_of_months = df.PostDate.dt.day
day_of_months = pd.DataFrame(day_of_months)
day_of_months.columns = ['day_of_months']

# extract hour feature
hours = df.PostDate.dt.hour
hours = pd.DataFrame(hours)
hours.columns = ['hours']

# extract the day name literal
days = df.PostDate.dt.day_name()
days = pd.DataFrame(days)
days.columns = ['days']

# is_weekend flag 
day_names = df.PostDate.dt.day_name()
is_weekend = day_names.apply(lambda x : 1 if x in ['Saturday','Sunday'] else 0)

is_weekend = pd.DataFrame(is_weekend)
is_weekend.columns = ['is_weekend']

# %%
features = pd.concat([hours, days, day_of_months, months, is_weekend], axis=1)
df_new = pd.concat([df, features], axis=1)
df_new

# %% [markdown]
# ## Look at your stats

# %%
df_new.groupby(['hours'])['LikeCount'].mean().plot.bar(title='Avg Number of Likes based on hour posted (INCLUDING Viral Tweets)', xlabel='Hour', ylabel='Avg Number of Likes', figsize=(16,8))

# %%
df_new[df['LikeCount']<1000].groupby(['hours'])['LikeCount'].mean().plot.bar(title='Avg Number of Likes based on hour posted (not including Viral Tweets)', xlabel='Hour', ylabel='Avg Number of Likes', figsize=(16,8))

# %%
df_new.groupby(['hours'])['LikeCount'].count().plot.bar(title='Total number of tweets posted each hour', xlabel='Hour', ylabel='Number of Tweets', figsize=(16,8))

# %%
df_new[df['LikeCount']<1000].groupby(['days'])['LikeCount'].mean().plot.bar(title='Avg number of likes for each day of the week (without Viral Tweets)', xlabel='Day of the Week', ylabel='Number of Likes', figsize=(16,8))

# %%
df_new.groupby(['days'])['LikeCount'].mean().plot.bar(title='Avg number of likes for each day of the week (with Viral Tweets)', xlabel='Day of the Week', ylabel='Number of Likes', figsize=(16,8))

# %%
df_new[df['LikeCount']<1000].groupby(['days'])['LikeCount'].sum().plot.bar(title='Total number of likes per day (without Viral Tweets)', xlabel='Day of the Week', ylabel='Number of Likes', figsize=(16,8))

# %%
df_new.groupby(['days'])['LikeCount'].sum().plot.bar(title='Total number of likes per day (without Viral Tweets)', xlabel='Day of the Week', ylabel='Number of Likes', figsize=(16,8))


