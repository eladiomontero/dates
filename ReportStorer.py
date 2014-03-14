__author__ = 'Eladio'
from couchdb import Server
import json


class ReportStorer():
    def __init__(self):
        self.urlServer = "http://fuse-dev-sql1.pc.aspectgroup.co.uk"
        self.port = '5984'
        self.username = 'eladio'
        self.password = 'oidale'

        self.couch = Server(self.urlServer + ":" + self.port)
        self.couch.resource.credentials = (self.username,self.password)
        self.db = self.couch['rezidor_dev_org']

    def storeReport(self, report):

        if type(report) is dict:
            try:
                print "The report with the ID: ", self.db.save(report), " has been inserted."
                print "Done uploading the reports"
            except Exception, e:
                print "There was an error", e

    def findExists(self, report):
        print 0
r = ReportStorer()

r.storeReport({"foo": "bar"})




