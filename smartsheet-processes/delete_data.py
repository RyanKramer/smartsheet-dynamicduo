# Import the dependencies needed for the process
import yaml
import smartsheet

# Read the values from the configuration file
with open("config.yml", "r") as yml_file:
    cfg = yaml.load(yml_file, Loader=yaml.FullLoader)

# Pretty print the configuration details to terminal
for section in cfg:
    print(section)
    for key, value in cfg[section].items():
        print("    " + key, value)

# Initialize client
smartsheet_client = smartsheet.Smartsheet(cfg["smartsheet"]['api_token'])

# Make sure we don't miss any errors
smartsheet_client.errors_as_exceptions(True)

# Enable the ability to provide one or more sheet IDs split by ,'s
try:
    sheet_list = cfg["smartsheet"]['sheet_id'].split(",")
except Exception:
    sheet_list = cfg["smartsheet"]['sheet_id']


# Define the function that we will call for each sheet
def remove_date_from_sheet(sheet_id):
    # Get sheet details
    active_sheet = smartsheet_client.Sheets.get_sheet(sheet_id)
    # Get rows from sheets
    raw_street_rows = active_sheet.rows._TypedList__store
    row_ids = []
    # Iterate through each sheet in the configuration file
    for row in raw_street_rows:
        row_ids.append(row._id_)

    # Extra space for pretty printing in terminal
    print("")
    # Will execute if there are any records in the sheet to remove
    if len(row_ids) > 0:
        print("Removing " + str(len(row_ids)) + " row from grid")
        smartsheet_client.Sheets.delete_rows(
            cfg["smartsheet"]['sheet_id'],
            row_ids)
    # Will execute if there are no records in the sheet to remove
    else:
        print("No rows to remove")

# If a single sheet to be removed will be of type int
if type(sheet_list) == int:
    remove_date_from_sheet(sheet_list)
# Will handle the list of sheets in the configuration file
else:
    for sheet in sheet_list:
        remove_date_from_sheet(sheet)
