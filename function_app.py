import azure.functions as func
import logging
from urllib.parse import parse_qs

# Load the azure class
app = func.FunctionApp()

# Call the app anything you want
@app.function_name(name="Upload")

# Be carefull, this makes the app anonymously accessable
@app.route(route="upload", auth_level=func.AuthLevel.ANONYMOUS)
# Without anonymous access: 
# @app.route(route="upload")

# function to send the upload to
def upload(req: func.HttpRequest) -> func.HttpResponse:

    # this is the file itself, probably smart to do some checking
    file = req.files.get('file')
    logging.info('File: %s' % file)

    # get the HTTP GET value from the page submit, call it anything you want
    camid = req.form.get('camid')
    logging.info('CamID: %s' % camid)

    # A way of processing multiple files, also smart to do some checking
    for input_file in req.files.values():
        filename = input_file.filename
        contents = input_file.stream.read()

        logging.info('Filename: %s' % filename)
        logging.info('Contents:')
        logging.info(contents)


    # Return for printing so you can view the results in CURL 
    return func.HttpResponse(f"camid: {camid} and filename: {filename}")
    # You can also return status codes: 
    # return func.HttpResponse("Something something...", status_code=200 )