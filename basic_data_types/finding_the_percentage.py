# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = 3
    inputs = [['Krishna',67,68,69],['Arjun',70,98,63],['Malika',52,56,60]]
    query_name = 'Malika'


    for i in range(n):
        if (inputs[i][0] == query_name):
            del inputs[i][0]
            result = '%0.2f' % float(sum(inputs[i]) / 3)

    print(result)