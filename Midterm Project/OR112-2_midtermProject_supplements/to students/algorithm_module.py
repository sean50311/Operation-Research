from MTP_lib import *

def heuristic_algorithm(file_path):
    '''
    1. Write your heuristic algorithm here.
    2. We would call this function in grading_program.py to evaluate your algorithm.
    3. Please do not change the function name and the file name.
    4. Do not import any extra library. We will import libraries from MTP_lib.py.
    5. The parameter is the file path of a data file, whose format is specified in the document.
    6. You need to return your schedule in two lists "machine" and "completion_time".
        (a) machine[j][0] is the machine ID (an integer) of the machine to process the first stage of job j + 1, and
            machine[j][1] is the machine ID (an integer) of the machine to process the second stage of job j + 1.
            Note. If job j + 1 has only one stage, you may store any integer in machine[j][1].
        (b) completion_time[j][0] is the completion time (an integer or a floating-point number) of the first stage of job j + 1, and
            completion_time[j][1] is the completion time (an integer or a floating-point number) of the second stage of job j + 1.
            Note. If job j + 1 has only one stage, you may store any integer or floating-point number in completion_time[j][1].
        Note 1. If you have n jobs, both the two lists are n by 2 (n rows, 2 columns).
        Note 2. In the list "machine", you should record the IDs of machines
                (i.e., to let machine 1 process the first stage of job 1,
                you should have machine[0][0] == 1 rather than machine[0][0] == 0).
    7. The only PY file that you need and are allowed to submit is this algorithm_module.py.
    '''

    # read data and store the information into your self-defined variables
    fp = open(file_path, 'r')
    # for a_row in fp:
    #    print(a_row) # a_row is a list
    # ...

    # start your algorithm here
    machine = []
    completion_time = []
    # ...

    return machine, completion_time
