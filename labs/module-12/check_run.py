"""Consistency checks of a retained local-generation record, not execution attestation."""
import argparse,json
from pathlib import Path
from run_local_model import check_record
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('record',type=Path);args=parser.parse_args()
    check_record(json.loads(args.record.read_text()))
    print('PASS: retained Module 12 synthetic generation record consistency; not execution attestation')
