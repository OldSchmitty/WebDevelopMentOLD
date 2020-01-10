#provider number = 670055
#year = 2016
#hospital's expected Medicare reimbursement for that fiscal year = (total discharges * average medicare payments) + results for each  DRG
#calculated VBP bonus/penalty to the hospital for the given fiscal year =
#
# ExperienceDomain.hcahps_consistency_score
#adjusted expected Medicare reimbursement for the hospital, accounting for the VBP bonus/penalty
#score each measures for VBP program =
#threshold for each measure =
#benchmark for the measure =

import csv
#8,10


TPS = 40.630952380952
AVERAGE_MEDICARE_PAYMENTS = 10
TOTAL_DISCHARGES = 8
HOSPITAL_PROVIDER_NUMBER = "670055"

def main():
    with open("MedicareProviderCharge.csv") as f:
        total = 0.0
        headers = []
        csv_reader = csv.reader(f, delimiter=',')
        start = True;
        for row in csv_reader:
            if start:
                start = False
                for name in row:
                    name = name.replace(" ", "_")
                    name = name.replace("-", "")
                    headers.append(name)
            else:
                if row[1] == HOSPITAL_PROVIDER_NUMBER:
                    row[AVERAGE_MEDICARE_PAYMENTS] = row[AVERAGE_MEDICARE_PAYMENTS].replace("$","")
                    row[AVERAGE_MEDICARE_PAYMENTS] = row[AVERAGE_MEDICARE_PAYMENTS].replace(",", "")
                    row[TOTAL_DISCHARGES] = row[TOTAL_DISCHARGES].replace("$", "")
                    row[TOTAL_DISCHARGES] = row[TOTAL_DISCHARGES].replace(",", "")
                    currentNum = float(row[AVERAGE_MEDICARE_PAYMENTS])*float(row[TOTAL_DISCHARGES])
                    total += currentNum
    adjustedTotal = total*.02
    adjustedTotal = adjustedTotal*(TPS/100)
    print adjustedTotal
    adjustedTotal = total + adjustedTotal
    print total
    print adjustedTotal



if __name__ == "__main__":
    main()