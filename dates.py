from datetime import date, timedelta, datetime
import time
import json
from multiprocessing.pool import ThreadPool as Pool


def worker(jsonString, loginName, apiSecret):
    try:
        triggerOmnitureDownload(jsonString, loginName, apiSecret)
    except Exception, e:
        print(str(e))

def getDateArray(startDate, endDate, offset):
    off = timedelta(hours=offset)

    end = endDate - off

    day = startDate

    result = []
    result.append(day)

    while(day <= end):
        day = day + timedelta(days=1)
        result.append(day)

    return result


def getRequestData(jsonTemplateString, dateReplace):
    """
        Take the template string
        Replace the [[date]]-token with the actual date in the correct format.
    """

    jsonResult = str(jsonTemplateString).replace("[[date]]", str(dateReplace))

    return jsonResult



def triggerOmnitureDownload(jsonString, loginName, apiSecret):

    print "finished %s" % time.ctime(time.time())

def saveJsons(jsonsArray):
    count = 0
    for jsonString in jsonsArray:
        jsonString = jsonString.replace("u'", "'")
        with open("./json_output/bupa"+ str(count) +".json", 'w+') as outfile:
            json.dump(jsonString, outfile)
        outfile.close()
        count = count + 1

def __main__():
    dates = getDateArray(datetime(2013,1,1), datetime(2013,1,31), 36)
    requestStrings = []
    template = json.load(open("./json_template/template.json", 'r'))
    for day in dates:
        requestStrings.append(getRequestData(template, day))
    saveJsons(requestStrings)
    pool_size = 5
    pool = Pool(pool_size)
    for request in requestStrings:
        pool.apply_async(worker, (request, "login", "pass",))


__main__()