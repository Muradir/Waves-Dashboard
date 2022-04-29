#import external modules
import unittest
import sys, os

pathToDataStoresDir = os.path.join(os.path.dirname(__file__), '../../backend_app/data_stores')
sys.path.append(pathToDataStoresDir)
print(sys.path)

#import internal classes
from database import Database
from test_data import TestData

#testing the functionality of the database
class TestDatabase(unittest.TestCase):

    def test_insertDataIntoDatabase(self):
        self.assertEquals(Database().insertDataIntoDatabase(entity=TestData(), recordsToInsert=[(1, 'test')]), 'Data of entity test_table was inserted successfully into Database!')

    def test_executeSelectQuery(self):
        self.assertEqual(Database().executeSelectQuery(tableName='test_table'), [(1, 'test')])


if __name__ == '__main__':
    unittest.main()

