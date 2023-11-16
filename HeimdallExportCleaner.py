# %% [markdown]
# # Imports

# %%
import pandas as pd
import json

# %% [markdown]
# # Config

# %%
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

heimdall_export_name = config['heimdall_export_name']
no_tag = config['no_tag']
tags = config['tags']
case_insensitive_sort = config['case_insensitive_sort']
clean_colour = config['clean_colour']
clean_description = config['clean_description']
clean_appid = config['clean_appid']
clean_appdescription = config['clean_appdescription']
separators_for_tag_name = config['separators_for_tag_name']

# %% [markdown]
# # Clean

# %%
df_raw = pd.read_json(heimdall_export_name + '.json')

if case_insensitive_sort:
    df_raw = df_raw.sort_values(by=['title'], key=lambda x: x.str.lower())
else:
    df_raw = df_raw.sort_values(by=['title'])

df_raw = df_raw.reset_index().drop(columns=['index'])

if clean_colour:
    df_raw['colour'] = "#161b1f"

if clean_description:
    df_raw['description'] = None

if clean_appid:
    df_raw['appid'] = "null"

if clean_appdescription:
    df_raw['appdescription'] = None

df_raw.head()

# %% [markdown]
# # Filter and export to `json` file(s)

# %%
def export_df_to_json(df_filtered, tag=None):
    if tag:
        filename = heimdall_export_name + '_' + tag
    else:
        filename = heimdall_export_name
    with open(filename + '.json', 'w') as json_file:
        json.dump(json.loads(df_filtered.to_json(orient='records')), json_file, indent=4)
        print('\"' + filename + '.json' + '\"' + ' created or customized!')

export_df_to_json(df_raw)

if tags is not None:
    for tag in tags:
        if df_raw['title'].str.contains(tag, case=False).any():
            df_filtered = df_raw[df_raw['title'].str.contains(tag, case=False)].copy().reset_index(drop=True)
            if separators_for_tag_name is not None:
                export_df_to_json(df_filtered, tag.replace(separators_for_tag_name[0], '').replace(separators_for_tag_name[1], ''))
            else:
                export_df_to_json(df_filtered, tag)

if no_tag is not None and tags is not None:
    conditions = ~df_raw['title'].str.contains('|'.join(tag for tag in tags), case=False)
    df_filtered = df_raw[conditions].copy().reset_index(drop=True)
    export_df_to_json(df_filtered, no_tag)

print('Done!')


