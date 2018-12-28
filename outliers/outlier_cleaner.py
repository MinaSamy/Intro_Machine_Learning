#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    #compare the predictions with net_worths(training data)
    
    cleaned_data = []
    
    ### your code goes here
    for i in range(len(ages)):
        prediction=predictions[i]
        actual=net_worths[i]
        error=abs(prediction-actual)
        data=(ages[i],actual,error)
        cleaned_data.append(data)

    #sort ascendingly according to error
    
    cleaned_data.sort(key=lambda tup:tup[2])
    cleaned_data=cleaned_data[0:81]
    #print len(cleaned_data)
    
    return cleaned_data

