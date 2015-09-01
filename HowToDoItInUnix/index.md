How to make your life easier with unix!!

## Run a command in nohup mode
- If you run a command in nohup mode and program was running in backend mode, it doesn't gets interrupted if server gets disconnected
```
nohup bash test.sh &
```
## Logging your programm
- only stdout to logfile, stderr gets printed on terminal
```
nohup python test.py > test.log & 
```
- stdout and stderr both to the same log file
```
nohup python test.py > test.log 2>&1 & 
```
