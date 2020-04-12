import yaml
import smartsheet

with open("config.yml", "r") as yml_file:
    cfg = yaml.load(yml_file, Loader=yaml.FullLoader)

for section in cfg:
    print(section)
    for key, value in cfg[section].items():
        print("    " + key, value)

# Initialize client
smartsheet_client = smartsheet.Smartsheet(cfg["smartsheet"]['api_token'])

# Make sure we don't miss any errors
smartsheet_client.errors_as_exceptions(True)

try:
    sheet_list = cfg["smartsheet"]['sheet_id'].split(",")
except Exception:
    sheet_list = cfg["smartsheet"]['sheet_id']


def remove_date_from_sheet(sheet_id):
    # Get sheet details
    active_sheet = smartsheet_client.Sheets.get_sheet(sheet_id)
    # Get rows from sheets
    raw_street_rows = active_sheet.rows._TypedList__store
    row_ids = []
    for row in raw_street_rows:
        row_ids.append(row._id_)

    print("")
    if len(row_ids) > 0:
        print("Removing " + str(len(row_ids)) + " row from grid")
        smartsheet_client.Sheets.delete_rows(
            cfg["smartsheet"]['sheet_id'],
            row_ids)
    else:
        print("No rows to remove")


if type(sheet_list) == int:
    remove_date_from_sheet(sheet_list)
else:
    for sheet in sheet_list:
        remove_date_from_sheet(sheet)
