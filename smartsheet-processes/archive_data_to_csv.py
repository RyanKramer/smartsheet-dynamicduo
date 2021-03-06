# Copyright 2020, DynamicDuo LLC, All rights reserved.

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
def remove_date_from_sheet_and_archive_records(sheet_id):
    # Get sheet details
    active_sheet = smartsheet_client.Sheets.get_sheet(sheet_id)

    # Get sheet name and append csv
    sheet_name = active_sheet.name + ".csv"
    file = open("archived_data/" + sheet_name, "w+")

    # Get rows from sheets
    raw_street_rows = active_sheet.rows._TypedList__store

    # Get sheet headers and parse them
    headers_raw = active_sheet._columns._TypedList__store
    headers_pre = []

    # Output the headers to your csv file
    for row in headers_raw:
        headers_pre.append(row.title)

    headers = ', '.join(headers_pre)

    # Write headers to csv
    file.write(headers)
    file.write("\n")

    # Write data to csv
    cells = []
    for row in raw_street_rows:
        for cell in row.cells._TypedList__store:
            if cell.value:
                cells.append(cell.value)
            else:
                cells.append("")
        file.write(", ".join(cells))
        file.write("\n")
        cells = []

        # Uncomment below lines if you would like to remove the data from the specified grids
        # print("Removing row with ID " + str(row._id_.value) + " from grid")
        # smartsheet_client.Sheets.delete_rows(
        #     active_sheet._id_.value,
        #     row._id_.value)

    # Close file
    file.close()

if type(sheet_list) == int:
    remove_date_from_sheet_and_archive_records(sheet_list)
else:
    for sheet in sheet_list:
        remove_date_from_sheet_and_archive_records(sheet)
