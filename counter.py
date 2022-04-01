def countEmail():
    emailCount = dict()
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    for line in handle:
        if line.startswith('From '):
            emailinfo = line.split()
            actualEmail = emailinfo[1]
            emailCount[actualEmail] = emailCount.get(actualEmail, 0) +1
        else:
            continue

    bigWord = 0
    bigCount = 0 
    for keys,values in emailCount.items():
        if values > bigCount:
            bigWord = keys
            bigCount = values
        else:
            continue

    
    print(bigWord, bigCount)

## if you want to test locally before you try to sync
## uncomment countEmail() and run > python counter.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#countEmail()
