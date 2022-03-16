# Shaun Bowman
# Dec 22 2021
from ina260.controller import Controller
import logging as log
import argparse
import sys
import getopt

# Setup the ina260 I2C interfaces for monitoring power / voltage / current
pSenseIna0x40 = Controller(address=0x40)
pSenseIna0x41 = Controller(address=0x41)
pSenseIna0x44 = Controller(address=0x44)

# Setup the relay board. This is one that i bought
# cheap off of amazon, it uses MCP23017 I2C 16 
# channel iosplitter chip.
relayBrd0x22 = Controller(address=0x22)
relayBrd0x22.relaySingleSet(bank='a',relay=2,state=0)
relayBrd0x22.relayBankSet(bank='a',state=0)
relayBrd0x22.relaySingleFlip(bank='a',relay=2)

# Setup logging. Provide "verbose" mode invoked w python thisFile.py -v
p = argparse.ArgumentParser()
p.add_argument('--verbose', '-v', action='count', default=0)
args = p.parse_args()
if args.verbose:
    log.basicConfig(format="%(asctime)s %(levelname)s: %(message)s",
                    level=log.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')
    log.info("Verbose output.")
else:
    log.basicConfig(format="%(levelname)s: %(message)s")
# log.info("This should be verbose.")
# log.warning("This is a warning!")
# log.error("This is an error.")

