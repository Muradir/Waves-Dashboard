#import modules
import unittest
from datetime import datetime

#import classes
from database_depr import Database

class TestDatabase(unittest.TestCase):

    def test_executeTruncateStatement(self):
        Database().executeTruncateStatement(tableName='stage_test_table')
        self.assertEqual(Database().executeSelectQuery(tableName='stage_test_table'), [])

    def test_executeInsertStatement(self):
        Database().executeInsertStatement(tableName='stage_test_table', data=[{'test_column' : 'test'}], loadId=0, tableAttributes=['test_column', 'loadId'], dynamicValues='%s, %s')
        self.assertEquals(Database().executeSelectQuery(tableName='stage_test_table'), [('test', 0)])

    def test_executeSelectQuery(self): 
        self.assertEqual(Database().executeSelectQuery('stage_test_table'),  [('test', 0)])

    def test_callLoadIdProcedure(self):
        self.assertGreater(Database().callLoadIdProcedure(procedureParameters=['stage_test_table', datetime.today()]), 0)

    def test_callCoreProcessingProcedure(self):
        Database().executeTruncateStatement(tableName='core_test_table')
        Database().executeInsertStatement(tableName='stage_test_table', data=[{'test_column' : 'tests'}], loadId=0, tableAttributes=['test_column', 'loadId'], dynamicValues='%s, %s')
        Database().callCoreProcessingProcedure(tableName='core_test_table', procedureName='load_core_test_table')
        self.assertEquals(Database().executeSelectQuery('core_test_table'), [])













if __name__ == '__main__':
    unittest.main()

