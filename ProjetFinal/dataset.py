import pandas as pd

def generateDataset(rawDatasetPath):
    '''
    definition: This function will convert the raw dataset stored in vegetables.data 
                to a usable and fonctionnal pandas table.
    input: The relative path of the raw dataset
    output: Pandas Table
    '''

    # Create the variables which will help to build the table
    attributes = ["name","green","root","flower","fruit",
                  "leaf","seed","aromatic","tuber",
                  "bulb","stems","white","orange","season"]
    parsedInstancesName = []
    parsedValues = []
    
    # Open the .data file
    rawData = open(rawDatasetPath, "r")
    lines = rawData.readlines()

    # Get the instances in each line
    for line in lines:
        # Parse the instance's attribute values in a list
        values = line.split(',')

        # Add the data in the variables
        data = {}
        for i in range(len(attributes)):
            label = attributes[i]
            if label == "name":
                parsedInstancesName.append(values[i])
            else :
                data[label] = int(values[i])
        parsedValues.append(data)

    # Create and return the dataset
    dataset = pd.DataFrame(parsedValues, index=parsedInstancesName)
    return dataset