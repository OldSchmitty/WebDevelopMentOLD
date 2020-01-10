import csv


def superSplit(s):
    if "Threshold" in s:
        return s.split("Achievement Threshold")
    elif "Benchmark" in s:
        return s.split("Benchmark")
    else:
        return s.split("Dimension Score")

def main():
    output ="""<table>\n\t<tr><th colspan=\"3\">Safety Scores</th></tr>\n\t<tr>\n\t<th>Name</th>\n\t<th>Achievement Threshold</th>\n\t<th>Benchmark</th>\n\t<th>Measure Score</th>\n\t</tr>
    """
    with open("Safety.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        start = True;
        columns = []
        headers = []
        for row in csv_reader:
            if start:
                start = False
                headers = row
                i = 0
                for name in row:
                    if ("Measure" in name or "Benchmark" in name or "Threshold" in name) and "Combined" not in name:
                        #print name
                        columns.append(i)
                    i+=1
            if row[0] == "670055":
                name = ""
                newstring = "<tr>\n"
                for column in columns:
                    if name != headers[column].split(" ")[0] or name == "":
                        if name != "":
                            name = headers[column].split(" ")[0]
                            newstring += "</tr>\n<tr>\n\t<td>\n\t\t" + name + "\n\t</td>\n"
                        else:
                            name = headers[column].split(" ")[0]
                            newstring+="\t<td>\n\t\t"+name+"\n\t</td>\n"
                    newstring+="\t<td>\n"+"\t\t"+row[column]+"\n\t</td>\n"
                newstring += "</tr>"

    output+=newstring
    output += "\n</table>"
    print output

    output = """<table>\n\t<tr><th colspan=\"3\">Clinical Care Scores</th></tr>\n\t<tr>\n\t<th>Name</th>\n\t<th>Achievement Threshold</th>\n\t<th>Benchmark</th>\n\t<th>Measure Score</th>\n\t</tr>
        """
    with open("ClinicalCare.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        start = True;
        columns = []
        headers = []
        for row in csv_reader:
            if start:
                start = False
                headers = row
                i = 0
                for name in row:
                    if ("Measure" in name or "Benchmark" in name or "Threshold" in name) and "Combined" not in name:
                        # print name
                        columns.append(i)
                    i += 1
            if row[0] == "670055":
                name = ""
                newstring = "<tr>\n"
                for column in columns:
                    if name != headers[column].split(" ")[0] or name == "":
                        if name != "":
                            name = headers[column].split(" ")[0]
                            newstring += "</tr>\n<tr>\n\t<td>\n\t\t" + name + "\n\t</td>\n"
                        else:
                            name = headers[column].split(" ")[0]
                            newstring += "\t<td>\n\t\t" + name + "\n\t</td>\n"
                    newstring += "\t<td>\n" + "\t\t" + row[column] + "\n\t</td>\n"
                newstring += "</tr>"

    output += newstring
    output += "\n</table>"
    print output

    output = """<table>\n\t<tr><th colspan=\"3\">Efficency Domain Scores</th></tr>\n\t<tr>\n\t<th>Name</th>\n\t<th>Achievement Threshold</th>\n\t<th>Benchmark</th>\n\t<th>Measure Score</th>\n\t</tr>
        """
    with open("EfficencyDomain.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        start = True;
        columns = []
        headers = []
        for row in csv_reader:
            if start:
                start = False
                headers = row
                i = 0
                for name in row:
                    if ("Measure" in name or "Benchmark" in name or "Threshold" in name) and "Combined" not in name:
                        # print name
                        columns.append(i)
                    i += 1
            if row[0] == "670055":
                name = ""
                newstring = "<tr>\n"
                for column in columns:
                    if name != headers[column].split(" ")[0] or name == "":
                        if name != "":
                            name = headers[column].split(" ")[0]
                            newstring += "</tr>\n<tr>\n\t<td>\n\t\t" + name + "\n\t</td>\n"
                        else:
                            name = headers[column].split(" ")[0]
                            newstring += "\t<td>\n\t\t" + name + "\n\t</td>\n"
                    newstring += "\t<td>\n" + "\t\t" + row[column] + "\n\t</td>\n"
                newstring += "</tr>"

    output += newstring
    output += "\n</table>"
    print output

    output = """<table>\n\t<tr><th colspan=\"3\">Experience Domain Scores</th></tr>\n\t<tr>\n\t<th>Name</th>\n\t<th>Achievement Threshold</th>\n\t<th>Benchmark</th>\n\t<th>Dimension Score</th>\n\t</tr>
            """
    with open("ExperienceDomain.csv") as f:
        csv_reader = csv.reader(f, delimiter=',')
        start = True;
        columns = []
        headers = []
        for row in csv_reader:
            if start:
                start = False
                headers = row
                i = 0
                for name in row:
                    if ("Dimension" in name or "Benchmark" in name or "Threshold" in name) and "Combined" not in name:
                        # print name
                        columns.append(i)
                    i += 1
            if row[0] == "670055":
                name = ""
                newstring = "<tr>\n"
                for column in columns:
                    if name != superSplit(headers[column])[0] or name == "":
                        if name != "":
                            name = superSplit(headers[column])[0]
                            newstring += "</tr>\n<tr>\n\t<td>\n\t\t" + name + "\n\t</td>\n"
                        else:
                            name = superSplit(headers[column])[0]
                            newstring += "\t<td>\n\t\t" + name + "\n\t</td>\n"
                    newstring += "\t<td>\n" + "\t\t" + row[column] + "\n\t</td>\n"
                newstring += "</tr>"

    output += newstring
    output += "\n</table>"
    print output


if __name__ == "__main__":
    main()