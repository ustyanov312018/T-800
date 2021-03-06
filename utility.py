from datetime import date, datetime, time, timedelta
import time as wait
import requests
import re
import sys
import argparse
import platform

SUCCESS         =  0
COOKIE_ERROR    = -1
RESPONSE_ERROR  = -2
BAD_USAGE       = -3

NUM_OF_TRIES    = 10

TARGET_URL      = 'https://lk.sut.ru/cabinet/'
SCHEDULE_URL    = 'https://lk.sut.ru/cabinet//project/cabinet/forms/raspisanie_bak.php'
AUTH_URL        = 'https://lk.sut.ru/cabinet/lib/autentificationok.php'
BUTTON_ID_STR   = '<span id=\"knop(\d*?)\">'


def file_log_info(message: str):
    with open("botlog.log", "a") as fp:
        fp.write("[INFO] " + message + "\n")

def file_log_error(message: str):
    with open("botlog.log", "a") as fp:
        fp.write("[ERROR] " + message + "\n")

def con_log_error(message: str):
        print("[ERROR] " + message)

def con_log_info(message: str):
        print("[INFO] " + message)

def con_log_warn(message: str):
        print("[WARN] " + message)

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("login", help="email used for logging in to lk.sut")
    parser.add_argument("password", help="password used for logging in to lk.sut")
    parser.add_argument("-d", help="Start bot as a daemon", action="store_true")
    args = parser.parse_args()
    return args