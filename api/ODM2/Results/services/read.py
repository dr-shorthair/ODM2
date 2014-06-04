import sys
import os

this_file = os.path.realpath(__file__)
directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(this_file))))
sys.path.insert(0, directory)

from ODM2 import service_base
import ODM2.Results.model as m

__author__ = 'Jacob'

class read(service_base):
    """queries to tables contained in Results schema"""

    def __init__(self):
        pass

    """
    TimeSeriesResults
    """
    def getAllTimeSeriesResults(self):
        """Select all on TimeSeriesResults

        :return TimeSeriesResults Objects:
            :type list:
        """

    def getTimeSeriesResultsById(self, timeSeriesId):
        """
        """
        pass

    def getTimeSeriesResultsbyCode(self, timeSeriesCode):
        """
        """
        pass


    """
    TimeSeriesResultValues
    """
    def getAllTimeSeriesValues(self):
        """Select all on TimeSeriesResults

        :return TimeSeriesResultsValue Objects:
            :type list:
        """
        return self._session.query(m.Timeseriesresultvalue).all()

    def getTimeSeriesValuesById(self, timeSeriesId):
        """Select by timeSeriesId

        :param timeSeriesId:
            :type Integer:
        :return return matching Timeseriesresultvalue Object filtered by timeSeriesId:
            :type Timeseriesresultvalue:
        """
        try:
            return self._session.query(m.Timeseriesresultvalue).filter_by()

    def getTimeSeriesValuesByCode(self, timeSeriesCode):
        """

        :param timeSeriesCode:
        :return:
        """
        pass
