spreadsheet = {
        'properties': {
            'title': check
            }
        }

spreadsheet = service.spreadsheets().create(
        body=spreadsheet,
        fields='spreadsheetId').execute()

print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))


