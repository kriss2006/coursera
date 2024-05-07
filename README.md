# coursera

I had trouble fetching data from the mysql db in xampp I had set up, so I opted to use hardcoded dictionaries representing the data from the different tables. In the `generate_prompts()` function I begin writing into the csv/html (as chosen in the command line). The completion date in the junction tables is compared with the start and end dates of our filtering and if it is within the range, a variable for the credit in that time range gets incremented. If it is over the minimum, the details for the course are supposed to be written in the file(s), but I could not get it to write the output into the csv.

By using the `argparse` module I've done my best to keep the "reading from the command line" part easily adjustable, and instead of my temporary solution - to work with dictionaries acting as tables - the adequate approach is to use a module such as `mysql.connector` to preserve scalability.
