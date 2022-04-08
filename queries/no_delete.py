import sys
sys.path.append(".")
from connections.connection import *

delete_testable = """
DROP TABLE TESTABLE
"""

execute_query(delete_testable)