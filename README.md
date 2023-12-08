# HeimdallExport-Cleaner

If you want to install Heimdall: https://github.com/linuxserver/Heimdall/

---

Nice and pastel-colored Heimdall theme with dark and light mode: [Heimdall-Catppuccin-Theme](https://github.com/fuchs-fabian/Heimdall-Catppuccin-Theme)

---

> This Python script was created in a [Jupyter Notebook](https://jupyter.org/) (`.ipynb`)

## Description

When doing a Heimdall export, the json file is not very well suited for uploading to [GitHub](https://github.com/), for example, to get a decent versioning.

- This script ensures that the export (`HeimdallExport.json`) is sorted alphabetically so that changes are easier to recognize.

- This script can also split the Heimdall export into further exports, so that if you want to set up Heimdall again, you can import them more easily and possibly not have to import certain bookmarks ("with a tag" -> What I call a tag, see below), so you don't have to manually delete them from Heimdall.
  For example:

  - `HeimdallExport_MAIN.json`
  - `HeimdallExport_HOMELAB.json`
  - `HeimdallExport_IPv4.json`

- This script can also override the `colour` so that they all have the same one. Also, it is possible to remove the `description`, `appid` and `appdescription` when exporting so that they are all "the same" when re-importing.

## Run

> This Python script must be executed in the same folder in which the Heimdall export is located!

In order for the Python script to run correctly under **Linux**, the [Pandas library must be installed](https://pandas.pydata.org/docs/getting_started/install.html#installing-from-pypi) beforehand:

```Shell
pip install pandas
```

> Additional packages may need to be installed. Confirm this with `y`. The `json` library may also need to be installed.

You can then execute the Python script as follows:

```Shell
python3 HeimdallExportCleaner.py
```

## Use of the `config.json`

Example:

```json
{
  "heimdall_export_name": "HeimdallExport",
  "case_insensitive_sort": true,
  "tags": ["HOMELAB", "IPv4"],
  "no_tag": "MAIN",
  "separators_for_tag_name": ["[", "]"],
  "clean_colour": false,
  "clean_description": false,
  "clean_appid": false,
  "clean_appdescription": false
}
```

Example of the appearance of a title in Heimdall: "`[HOMELAB] bookmark_name`"

Tag: `[HOMELAB]`

### `heimdall_export_name`

By default, the file that is created during Heimdall export is named: `HeimdallExport.json`

However, if you have renamed it, please enter the file name without the file extension here.

### `no_tag`

If you want an export to be carried out without the tags being included in this Heimdall export, enter a name here, e.g. `MAIN`.

### `separators_for_tag_name`

If you use special separators for the tags, please enter them here so that they do not appear in the name of the new json files created.
