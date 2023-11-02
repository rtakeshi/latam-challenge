import pytest
import sys
import os

#adding src directory to sys path
current_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.join(current_directory, '..', 'src')
sys.path.append(src_directory)



from q2_memory import q2_memory
from q2_time import q2_time

TEST_DATA_DIR = "home/jovyan/work/data/test_data.csv"


#testing function for q2_memory
def test_q2_memory():
    result = q2_memory(TEST_DATA_DIR)

    expected_result =[
    ("😍", 15),
    ("🌍", 14),
    ("🐱", 13),
    ("🌞", 13),
    ("❤️", 12),
    ("🎈", 12),
    ("🚀", 11),
    ("🌸", 10),
    ("🌟", 9),
    ("🌼", 6)
]

    assert result == expected_result



def test_q2_time():
    result = q2_time(TEST_DATA_DIR)
 
    expected_result =[
    ("😍", 15),
    ("🌍", 14),
    ("🐱", 13),
    ("🌞", 13),
    ("❤️", 12),
    ("🎈", 12),
    ("🚀", 11),
    ("🌸", 10),
    ("🌟", 9),
    ("🌼", 6)
]


    assert result == expected_result