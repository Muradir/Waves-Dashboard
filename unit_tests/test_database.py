#import external modules
import unittest
import sys, os

testdir = os.path.dirname(__file__)
srcdir = '../data_stores'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

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

