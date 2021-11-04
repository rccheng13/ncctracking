cd c:\python39\user\censusreader
copy /y census_log.csv census_log.bak
"c:\python39\python.exe" censuscounter2.py

copy /y census_log.csv "C:\Users\rc1084\OneDrive - Rutgers University\Documents\NeuroCensus.csv"
rem copy /y census_log_dw.csv "C:\Users\rc1084\OneDrive - Rutgers University\Documents\NeuroCensus_dw.csv"

"c:\python39\python.exe" last_days.py
rem "c:\python39\python.exe" upload_gdrive.py

copy /y census_log_dw.csv ncctracking\census_log_dw.csv
move /y tendays_dw.csv ncctracking\tendays_dw.csv

rem sync to github for graphing
cd ncctracking
"C:\Program Files\Git\cmd\git.exe" add --all
"C:\Program Files\Git\cmd\git.exe" commit -m "scheduled push"
"C:\Program Files\Git\cmd\git.exe" push origin main
