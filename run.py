#!/usr/bin/env python3
import time
import subprocess
import datetime

SLEEP_TIME = 10
LOG_FILE = 'run.log'
MAX_DURATION = 10800
MIN_DURATION = 1800

def s_exec(command):
    print(command)
    command = str(command) + '\n'
    log(command)
    return subprocess.check_output(command, universal_newlines=True, shell=True)

def check_if_running():
    return len([i for i in s_exec("ps xww").splitlines() if "org.radargun.LaunchMaster" in i])

def get_configs():
    return ['torun/' + i for i in s_exec('ls torun').splitlines()]

def log_and_print(in_val):
    print(in_val)
    in_val = str(in_val) + '\n'
    log(in_val)

def init_log():
    log('*****************************************************************************')
    log('******************************  new experiment ******************************')
    log('*****************************************************************************')

def log_new_run():
    log('******************************  new run *************************************')

def log(in_val):
    with open(LOG_FILE,'a') as f:
        for line in in_val.splitlines():
            line = str(datetime.datetime.now()) + ' ' + line + '\n'
            f.write(line)

def set_up_config(config):
    log(s_exec("cp {config} radargun/conf/benchmark.xml".format(**locals())))

def main():
    init_log()
    for config in get_configs():
        log_new_run()
        log_and_print("going for "+config)
        set_up_config(config)
        log(s_exec("./clean.sh"))
        time.sleep(SLEEP_TIME)
        log(s_exec("./start.py"))
        time.sleep(SLEEP_TIME)
        for i in range(0,MIN_DURATION,SLEEP_TIME):
            time.sleep(SLEEP_TIME)
            if not check_if_running():
                log_and_print('ERROR: ended before time :( ')
                break;
        else:
            for i in range(0,MAX_DURATION-MIN_DURATION,SLEEP_TIME):
                time.sleep(SLEEP_TIME)
                if not check_if_running():
                    log_and_print('DONE: YAY,{config} done'.format(**locals()))
                    break;
            else:
                log_and_print('ERROR: ended much later :( ')
                pass
        log(s_exec("./collect.sh"))
        log(s_exec("./clean.sh"))


if __name__ == '__main__':
    main()
