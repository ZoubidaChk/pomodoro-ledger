#!/usr/bin/env python3
"""Record and total Pomodoro focus sessions in a JSON file."""
import argparse, json
from dataclasses import dataclass, asdict
from datetime import datetime
@dataclass
class Session: task:str; minutes:int; timestamp:str
def add(path,task,minutes):
    try:
        with open(path,encoding="utf-8") as f: data=json.load(f)
    except (FileNotFoundError,json.JSONDecodeError): data=[]
    data.append(asdict(Session(task,int(minutes),datetime.now().isoformat(timespec="seconds"))))
    with open(path,"w",encoding="utf-8") as f: json.dump(data,f,indent=2)
    return data
def totals(data): return {"sessions":len(data),"minutes":sum(int(x.get("minutes",0)) for x in data)}
def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("file"); p.add_argument("--task"); p.add_argument("--minutes",type=int,default=25); a=p.parse_args()
    if a.task: add(a.file,a.task,a.minutes)
    else:
        try:
            with open(a.file,encoding="utf-8") as f: data=json.load(f)
        except (FileNotFoundError,json.JSONDecodeError): data=[]
        print(json.dumps(totals(data),indent=2))
if __name__=="__main__": raise SystemExit(main())
