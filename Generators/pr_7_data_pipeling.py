"""
Let’s think of a strategy:

Read every line of the file.
Split each line into a list of values.
Extract the column names.
Use the column names and lists to create a dictionary.
Filter out the rounds you aren’t interested in.
Calculate the total and average values for the rounds you are interested in.

permalink,company,numEmps,category,city,state,fundedDate,raisedAmt,raisedCurrency,round
digg,Digg,60,web,San Francisco,CA,1-Dec-06,8500000,USD,b
digg,Digg,60,web,San Francisco,CA,1-Oct-05,2800000,USD,a
facebook,Facebook,450,web,Palo Alto,CA,1-Sep-04,500000,USD,angel
facebook,Facebook,450,web,Palo Alto,CA,1-May-05,12700000,USD,a
photobucket,Photobucket,60,web,Palo Alto,CA,1-Mar-05,3000000,USD,a

"""

file_name = "techcrunch.csv"

lines = (line for line in open(file_name, "r"))
list_lines = (s.strip().split(",") for s in lines)
cols = next(list_lines)
company_dicts = (dict(zip(cols, data)) for data in list_lines)

funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)

total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")
