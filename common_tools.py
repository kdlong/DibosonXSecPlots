import math
import copy
import matplotlib.pyplot as plt

def getVal(value):
    if isinstance(value, float):
        return value
    val = 1 
    if "*" in value:
        for i in value.split("*"):
            val *= float(i)
        return val
    else:
        return float(value)

def plotDataFromFile(file_name):
    xvals = []
    central = []
    errorup = []
    errordown = []
    error2up = []
    error2down = []
    with open(file_name) as input_file:
        for line in input_file:
            if line[0] == "#":
                continue
            values = line.split()
            if len(values) < 2:
                raise ValueError("Invalid input file %s. Line content was: \n    %s" % (file_name, line))
            xvals.append(getVal(values[0]))
            central.append(getVal(values[1]))
            if len(values) < 3:
                print("No error values found in input file %s" % file_name)
                continue
            if "%" in values[2]:
                values[2] = float(values[1])*float(values[2].strip("%"))/100
            if "%" in values[3]:
                values[3] = float(values[1])*float(values[3].strip("%"))/100
            errorup.append(getVal(values[2]))
            errordown.append(getVal(values[3]))
            if len(values) == 6:
                error2up.append(math.sqrt(getVal(values[2])**2 + getVal(values[4])**2))
                error2down.append(math.sqrt(getVal(values[3])**2 + getVal(values[5])**2))
    return xvals, central, errorup, errordown, error2up, error2down

def plotData(x, y, statup, statdown, totup, totdown, label):
    data_noerr_args = {
    'markersize' : 8, 
    }
    
    if "ATLAS" in label:
        data_noerr_args["markerfacecolor"] = 'w'
        
    data_args = copy.deepcopy(data_noerr_args)
    data_args['capsize'] = 4
    data_args['fmt'] = 'ok'
    if r"\nu" in label:
        data_args["fmt"] = 'sk'

    plt.errorbar(x,y,yerr=[totup,totdown], **data_args)
    plt.errorbar(x,y,yerr=[statup, statdown], **data_args)
    return plt.plot(x,y, data_args['fmt'], label=label, **data_noerr_args)

    
