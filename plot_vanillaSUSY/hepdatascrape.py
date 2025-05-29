from hepdata_cli.api import Client
import os

client = Client(verbose=True)

reactionsList = [
    "(\"P P --> GLU GLU\" OR \"P P --> GLU GLU X\" OR \"PP --> GLUINO GLUINO\" OR \"PP --> GLUINO GLUINO X\" OR \"P P --> GLUINO GLUINO\" OR \"P P --> GLUINO GLUINO X\")",
    "(\"PP --> SQUARK SQUARK\" OR \"PP --> SQUARK SQUARK X\" OR \"P P --> SQUARK SQUARK\" OR \"P P --> SQUARK SQUARK X\")",
    "(\"PP --> STOP STOP\" OR \"PP --> STOP STOP X\" OR \"P P --> STOP STOP\" OR \"P P --> STOP STOP X\")",
]

outputList = []

def save_tuples_to_markdown(tuples_list, headers=None, filename="output.md"):
    """
    Saves a list of tuples to a Markdown file in table format.

    :param tuples_list: List of tuples, where each tuple represents a row.
    :param headers: Optional list of headers (column names).
    :param filename: Name of the markdown file to create.
    """
    # Sort by the second element in each tuple
    sorted_list = sorted(tuples_list, key=lambda x: x[0])
    
    # Prepare all rows as strings
    if headers:
        rows = [list(map(str, headers))] + [list(map(str, row)) for row in sorted_list]
    else:
        rows = [list(map(str, row)) for row in sorted_list]

    # Calculate max width for each column
    col_widths = [max(len(row[i]) for row in rows) for i in range(len(rows[0]))]

    with open(filename, "w") as f:
        if headers:
            # Write header row with padding
            header_line = "| " + " | ".join(headers[i].ljust(col_widths[i]) for i in range(len(headers))) + " |"
            f.write(header_line + "\n")
            # Write separator row with dashes matching the column width
            separator_line = "| " + " | ".join('-' * col_widths[i] for i in range(len(headers))) + " |"
            f.write(separator_line + "\n")

        # Write data rows with padding
        for row in sorted_list:
            line = "| " + " | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))) + " |"
            f.write(line + "\n")

    print(f"Markdown table saved to {filename}")

for reaction in reactionsList:
    queryString = ""
    queryString += f' reactions:{reaction} '
    queryString += f' AND year:[2018 TO 2026] '
    queryString += f' AND collaborations:(CMS OR ATLAS) '
    myresults = client.find(queryString)
    print(len(myresults))


    label = reaction.split("-->")[-1]
    label = ''.join(c for c in label if c.isalnum())

    for result in myresults:
        # print(result.keys())
        # dict_keys(['abstract', 'access_urls', 'analyses', 'arxiv_id', 'authors', 'collaborations', 'control_number', 'creation_date', 'data', 'data_abstract', 'data_keywords', 'date', 'doc_type', 'doi', 'first_author', 'hepdata_doi', 'id', 'inspire_id', 'journal_info', 'keywords', 'last_updated', 'parent_child_join', 'publication_date', 'recid', 'resources', 'subject_area', 'summary_authors', 'title', 'total_tables', 'type', 'uuid', 'version', 'year'])

        tmpURL = result["access_urls"]["links"]["csv"].replace("download","record").replace("submission/","")
        tmpURL = "/".join(tmpURL.split("/")[:-2])
        outputList.append(
            (
                result["arxiv_id"],
                result["year"],
                result["collaborations"][0],
                tmpURL,
                )

        )      
        os.makedirs(f"data/{label}/{result['arxiv_id'].replace(':','_')}", exist_ok=True)

    print(outputList)  

    filename = label+".md"
    save_tuples_to_markdown(outputList, filename=filename)

