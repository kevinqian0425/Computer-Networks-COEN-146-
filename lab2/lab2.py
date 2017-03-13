import subprocess

NUM_TRIALS = 10
INTERMEDIARY_FILE = 'data.log'

def transfer(user, min_mb=0, max_mb=500):
    """
    Create an ssh connection over which we transfer file over network link.

    Positional Arguments:
            user: username to log into. If no ssh key is present it'll be a pain to run (string)

    Keyword Arguments:
            min_mb: minimum number of megabytes to transfer (int, 0)
                    max_mb: maximum number of megabytes to transfer (int, 1000)

    Return:
            None

     Side Effect:
             Generates a file called lab2.dat
    """

    with open(INTERMEDIARY_FILE, 'w') as outfile:
        for file_size in range(min_mb, max_mb, int(max_mb/NUM_TRIALS)):
            print("Transfer time for file size: " + str(file_size) + "MB")
            subprocess.call('>&2 echo {}'.format(file_size), stderr=outfile, shell=True)
            for run_no in range(10):
                subprocess.call('time dd if=/dev/zero bs=1048576 count=1024|ssh -q kqian@linux.scudc.scu.edu "dd of=/dev/null 2>/dev/null"'.format(file_size* (10**6)), stderr=outfile, shell=True)
                # subprocess.call('>&2 echo {}'.format(run_no), stderr=outfile, shell=True)

def parse_data(file_path=INTERMEDIARY_FILE):
    """
    Parses the given file and averages the time spent for each run
    
    Returns:
            averages (list) - averages in order based on the step size
    
    """

    sizes = []
    averages = []
    with open (file_path, 'r') as outfile:
        for line in outfile:
            try:
                sizes.append(int(line))
                averages.append(0)
            except:
                if 'user' in line or 'sys' in line:
                    averages[-1] += float(line.split('m')[1].strip()[:-1])

    return ([averages/NUM_TRIALS for average in averages], sizes)

if __name__ == '__main__': 
    transfer('kqian')
    print(parse_data(INTERMEDIARY_FILE))















