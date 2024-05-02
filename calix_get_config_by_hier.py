#!/usr/bin/env python3
"""
============================
__title__  = "E9-2 AXOS COLLECT BY HEIR."
__author__ = "Charles F. Port"
__copyright__ = "Copyright 10MAR23"
__credits__ = ["Charles F. Port"]
__license__ = "GPL"
__version__ = "0.0.0"
__modified__ = 07FEB24
__maintainer__ = "TBD"
__email__ = "cport@rawbw.com"
__status__ = "Test"

TERMS AND CONDITIONS FOR USE
============================
1. This software is provided by the author "as is" and any express or implied
warranties, including, but not limited to, the implied warranties of
marketability and fitness for a particular purpose are disclaimed. In no
event shall the author be liable for any direct, indirect, incidental,
special, exemplary, or consequential damages (including, but not limited to,
procurement of substitute goods or services; loss of use, data, or profits; or
business interruption) however caused and on any theory of liability, whether
in contract, strict liability, or tort (including negligence or otherwise)
arising in any way out of the use of this software, even if advised of the
possibility of such damage.

2. No Support. Neither Author (nor Calix, Inc.) will provide support.

3. USE AT YOUR OWN RISK
===========================
END OF TERMS AND CONDITIONS

Changes:
========

10MAR23:
--------
0. Conception

07FEB24:
--------
1. [Function 3] cmd_n0 = ('terminal screen-length 250') || Changed from 150 to 250 

"""


# --------------------------------------------------
# PYTHON3 IMPORT LIBS
# --------------------------------------------------
import csv
import logging
import os
import re
from getpass import getpass
import time
from io import StringIO
from logging.config import dictConfig
from paramiko import SSHClient, AutoAddPolicy, SSHException
from paramiko_expect import SSHClientInteraction
# --------------------------------------------------
# DISABLE PARAMIKO LOGGER
# --------------------------------------------------
paramiko_logger = logging.getLogger("paramiko.transport")
paramiko_logger.disabled = True

# --------------------------------------------------
# [FUNCTION 0] Function to setup && start logging
# --------------------------------------------------
def init_logger():
    """define logger functions"""
    logging_config = dict(
        version=1,
        formatters={
            'f': {
                'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
            }
        },
        handlers={
            'h': {
                'class': 'logging.StreamHandler',
                'formatter': 'f',
                'level': logging.INFO
            }
        },
        root={
            'handlers': ['h'],
            'level': logging.DEBUG,
        },
    )
    dictConfig(logging_config)
    logger = logging.getLogger()
    if logger:
        return True

# --------------------------------------------------
# [FUNCTION 1] Interrogate user via input() [variables]
# --------------------------------------------------
def get_info():
    """Get variables"""
    hostname = input("Enter E9-BNG hostname or E9-BNG address: ")
    username = input("Enter SSH Username: ")
    password = getpass(prompt='Enter SSH Password: ')
    port = input("Enter SSH Port (if not default 22): ") or 22
    return hostname, username, password, port


# --------------------------------------------------
# [FUNCTION 2]  Use Paramiko to send a command
# --------------------------------------------------
def ssh_cmd(host_name, user_name, pass_word, port, cmd):
    """Peruse remote E9"""
    try:
        ssh_c = SSHClient()
        ssh_c.set_missing_host_key_policy(AutoAddPolicy())
        ssh_c.connect( hostname = host_name, username = user_name,
                     password = pass_word, port = port, allow_agent=False)
        stdin, stdout, stderr = ssh_c.exec_command(cmd)
        result = stdout.read().decode().strip()
    except  SSHException as ssh_exception:
        print(f"Unable to establish SSH connection: {ssh_exception}")
    finally:
        ssh_c.close()
    return result


# --------------------------------------------------
# [FUNCTION 3]  Use Paramiko Expect
# --------------------------------------------------
def ssh_interact(host_name, user_name, pass_word, port):
    """ SSH EXPECT """
    ##################################################
    # FUNCTION VARS
    ##################################################
    root_prompt = '.*# '
    ques_mark = '\x3F'
    cmd_n0 = ('terminal screen-length 250')
    cmd_n1 = (f'show running-config {ques_mark}')
    special_prompt = (f'{root_prompt}show running-config ')
    try:
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect( hostname = host_name, username = user_name,
                     password = pass_word, port = port, allow_agent=False)
        with SSHClientInteraction(ssh,timeout=10,display=False) as interact:
            interact.send('\n')
            interact.expect(root_prompt)
            ############################
            interact.send(cmd_n0)
            interact.expect(root_prompt)
            ############################
            interact.send(cmd_n1)
            interact.expect(special_prompt)
            ############################
            results = interact.current_output_clean
            ############################
        ssh.close()
    except SSHException as err:
        print(str(err).encode())
    return results


# --------------------------------------------------
# [FUNCTION 4] CREATE A CONFIG HIERARCHY
# --------------------------------------------------
def create_hierarchy(raw_results):
    """ CREATE A CONFIG HIERARCHY"""
    new_data = list(csv.DictReader(StringIO(raw_results), delimiter='\t'))
    new_list = [d['show running-config ?'] for d in new_data if 'show running-config ?' in d]
    heir_0 = (re.findall(r"\'\s\s(\w+)\s+", str(new_list)))
    heir_1 = (re.findall(r"\'\s\s(\w+[\-]\w+)\s+", str(new_list)))
    heir_2 = (re.findall(r"\'\s\s(\w+[\-]\w+[\-]\w+)\s+", str(new_list)))
    heir_3 = (re.findall(r"\'\s\s(\w+[\-]\w+[\-]\w+[\-]\w+)\s+", str(new_list)))
    heir_4 = (re.findall(r"\'\s\s(\w+[\-]\w+[\-]\w+[\-]\w+[\-]\w+)\s+", str(new_list)))
    heir_new = []
    for line_0 in heir_0:
        heir_new.append(line_0)
    for line_1 in heir_1:
        heir_new.append(line_1)
    for line_2 in heir_2:
        heir_new.append(line_2)
    for line_3 in heir_3:
        heir_new.append(line_3)
    for line_4 in heir_4:
        heir_new.append(line_4)
    heir_axos = sorted(heir_new)
    return heir_axos


# --------------------------------------------------
# [FUNCTION 5] MAKE DIRECTORY TREE
# --------------------------------------------------
def make_directory(top_dir,cfg_list):
    """MKDIR"""
    main_dir = []
    main_dir.append(top_dir)
    sub_dir = []
    for item_1 in cfg_list:
        sub_dir.append(item_1)
    print(main_dir)
    print(sub_dir)
    for dir1 in main_dir:
        for dir2 in sub_dir:
            try:
                os.makedirs(os.path.join(dir1,dir2))
            except OSError:
                pass
    return True


# --------------------------------------------------
# MAIN FUNCTION  Execute FUNCTION sequence
# --------------------------------------------------
def main():
    """
    #####################################
    # MAIN: ORCHESTRATE ALL FUNCTIONS
    #####################################
    """
    #####################################
    # START LOGGER
    #####################################
    start_logging = init_logger()
    if start_logging:
        logging.info('Script is starting')
    #####################################
    # COLLECT INPUT VARIABLES
    #####################################
    logging.info('Get target input variables')
    hostname, username, password, port = get_info()
    #####################################
    # GET HIERARCHY
    #####################################
    logging.info('Use login info to ssh and determine AXOS hierarchy')
    heir_info = ssh_interact(hostname, username, password, port)
    #####################################
    # PARSE HIERARCHY
    #####################################
    logging.info('Generate release specific AXOS hierarchy')
    heir_stanzas = create_hierarchy(heir_info)
    #####################################
    # BUILD DIRECTORY STRUCTURE
    #####################################
    logging.info("Building Configuration Directory structure")
    mk_new = make_directory(hostname, heir_stanzas)
    if mk_new:
        logging.info("Directory tree created")
    #####################################
    # GET CONFIG BY HIERARCHY AND STORE
    #####################################
    index = 0
    dir_path_root = (f"./{hostname}/")
    while index < len(heir_stanzas):
        element = heir_stanzas[index]
        run_cmd = f"show running-config {element} | nomore"
        heir_cfg = ssh_cmd(hostname, username, password, port, run_cmd)
        file_name = f"{element}_cfg.txt"
        sub_path = f"{element}/"
        rel_path = os.path.join(dir_path_root,sub_path)
        abs_path = os.path.join(rel_path,file_name)
        if os.path.exists (rel_path):
            with open(abs_path, "w", encoding='utf-8') as fl_x:
                fl_x.write(heir_cfg)
                logging.info(f"File %s_cfg.txt was created in file %s", element, abs_path)
        time.sleep(5)
        index += 1

if __name__ == "__main__":
    main()
