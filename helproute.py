@app.route('/help', methods=['GET'])
def help() -> str:
    '''
    Information on how to interact with the application
    Returns: A string describing what paths to use for each function.
    '''
    return '''\nFIRST LOAD DATA USING THE FOLLOWING PATH: /data -X POST\n
    IF THERE ARE ERROR LOAD THE DATA ONCE MORE\n\n
    Navigation:\n
    Use the following routes to access the data:
      1.  /feature/<feat_string>
          #posts data for a specific column in the csv
      2.  /earthquake/<id_num>
          #posts data from all columns for one earthquake
      3.  /magnitude/<mag>
          #all the earthquakes for a given magnitude
      4.  /delete/<id_num>
          #deletes an entry on the list based on id
      5.  /update/<id_num>/<feature_string>/<new_value>
          #changes the value of a feature for an earthquake
      6.  /jobs
          #uses a JSON to create a job
      7.  /jobs/delete/<job_uuid>
          #deletes one of the jobs that has been created
      8.  /jobs/<job_uuid>
          #API route for checking on the status of a submitted job
      9.  /download/<jobuuid>
          #plots map of earthquake magnitudes and downloads as png\n\n'''
