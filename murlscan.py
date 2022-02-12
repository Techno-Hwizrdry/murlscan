# Copyright: 2022, Alexan Mardigian
__version__ = "1.0.0"

import sys
from argparse     import ArgumentParser
from configparser import ConfigParser
from csv import DictWriter
from os.path import exists
from malurl  import MalURL

CONFIG_FILE = 'murlscan.conf'

def get_args():
    parser = ArgumentParser()
    parser.add_argument('-c', dest='conf_filepath',   help='File path to MurlScan configuration file.',
                                                      default=CONFIG_FILE)
    parser.add_argument('-u', dest='url',             help='URL of suspicious link.',
                                                      required=False)
    parser.add_argument('-i', dest='input_filepath',  help='File path to a file listing URLs.',
                                                      required=False)
    parser.add_argument('-o', dest='output_filepath', help='File path for the output.',
                                                      default='')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()

def print_and_exit(msg):
    print(msg)
    sys.exit(0)

def read_config_file(filename):
    config = ConfigParser()
    config.read(filename)
    return config

def read_urls(filename):
    if not exists(filename): return []

    with open(filename, 'r') as infile:
        return [line.strip() for line in infile.readlines()]

def get_data(config):
    cfg = config['murlscan']
    apikey = cfg['apikey']
    strictness = cfg['strictness']
    return MalURL(apikey, strictness)

def print_results(murl, urls):
    for url in urls:
        murl.fetch(url)
        murl.print()
        print('\n')

def write_csv(murl, urls, filename):
    with open(filename, 'w') as csvfile:
        count = 0
        for url in urls:
            count += 1
            murl.fetch(url)
            field_names = murl.results.keys()
            writer = DictWriter(csvfile, fieldnames=field_names)
            if count == 1: writer.writeheader()
            writer.writerow(murl.results)

def main():
    opts = get_args()
    infile = opts.input_filepath
    
    if not infile and not opts.url:
        msg = f"Error: No URL or list of URLs provided.\nFor help, run:  'python3 {sys.argv[0]} --help'"
        print_and_exit(msg)

    config_file = opts.conf_filepath

    try:
        config = read_config_file(config_file)
        urls = [opts.url] if opts.url else read_urls(infile)

        if not urls:
            print_and_exit("Error: file {infile} not found.")

        murl = get_data(config)

        if not outfile:
            print_results(murl, urls)
        else:
            print(f'Writing to {opts.output_filepath} ...')
            write_csv(murl, urls, opts.output_filepath)
            print("Done!")
    except KeyError as e:
        print(f"Error: {e.args[0]} section missing from config file '{config_file}'.")
    except FileNotFoundError as e:
        print(e)

if __name__ == '__main__':
    main()