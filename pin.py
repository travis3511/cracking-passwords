import os
import argparse

def main(parser):
    parser.add_argument("--ip_address","-a",default="localhost")
    parser.add_argument("--username","-u",required=True)
    parser.add_argument("--passwordlist","-p")
    parser.add_argument("--length","-l")
    parser.add_argument("--start_index","-s",default=0)
    parser.add_argument("--end_index","-e",default=6)
    parser.add_argument("--input_file","-i")
    parser.add_argument("--output_file","-o")
    args = parser.parse_args()
    
    if args.passwordlist:
        attempts = args.passwordlist.split("\n")
    elif args.inputfile:
	inputfile = args.inputfile.split("\n")
	datalist = []
        parsed_data = {}
        for i in inputfile:
            datalist.append(i.split(","))
	for w in datalist:
	    for n in w:
		if datalist.index(w) == 0:
		    parsed_data[n] = ""
		else:
		    key_words = parsed_data.keywords()
		    for m in keywords:
			parsed_data[m] = w
    elif args.length:
	attempts = []
	for i in range(args.start_index,args.end_index,1):
	    attempts.append(i)
    os.system("net use \\localhost /user:"+args.username+" "+password)

if __name__ == "__main__":
    main(argparse.ArgumentParser())