# -*- coding: utf-8 -*-



import configparser


def read_ini(filename, section, key):
    cf = configparser.ConfigParser()
    cf.read(filename)
    value = cf.get(section, key)
    return value

def write_ini(filename, section, key, value):
    cf = configparser.ConfigParser()
    cf.read(filename)
    cf.set(section, key, value)
    # write to file
    cf.write(open(filename, "w"))


write_ini('C:\\Project\\TestSeq-Amazon\\Config\\Calibration.ini', 'Probe', 'probex', str(1.0))