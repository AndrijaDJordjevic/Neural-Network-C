#!/usr/bin/env python3
import argparse
import sys
import Macro
import Neural

def get_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=Macro.MYTORCH_DESCRIPTION, epilog=Macro.EPILOG)
    new_load_flag = parser.add_mutually_exclusive_group(required=True)
    train_predict_flag = parser.add_mutually_exclusive_group(required=True)

    new_load_flag.add_argument(
        "--new", nargs="+", metavar="LAYERS", help=Macro.NEW_DESCRIPTION
    )
    new_load_flag.add_argument(
        "--load", metavar="LOADFILE", nargs=1, help=Macro.LOAD_DESCRIPTION
    )
    train_predict_flag.add_argument(
        "--train", action="store_true", help=Macro.TRAIN_DESCRIPTION
    )
    train_predict_flag.add_argument(
        "--predict", action="store_true", help=Macro.PREDICT_DESCRIPTION
    )

    parser.add_argument("--save", metavar="SAVEFILE", nargs=1, help=Macro.SAVE_DESCRIPTION)
    parser.add_argument("FILE", nargs=1, help=Macro.FILE)
    return parser
    
def main():
    parser = get_args()
    
    if (len(sys.argv) == 2):
        if (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
            parser.print_help()
    else:
        arg = parser.parse_args()
        Neural.StartNeural(arg)

if __name__ == "__main__":
    main()
