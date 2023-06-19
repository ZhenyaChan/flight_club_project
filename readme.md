# Flight Club Project

## Description
- Implementation of the Flight Deals App using latest technologies of <strong>Twilio Library, OOP concepts, Python, Sheety API, Tequila API, Google Sheets, smtplib, and requests modules</strong>.
- The app retrieves data about users and destination airports stored in Google Sheets using Sheety API and requests module.
- The Flight Club retrieves IATA code for the airports using Tequila API if IATA data is absent in Google Sheets.
- This program checks the flights to each destination airport from Google Sheets that are available in next 6 months using <strong>Tequila API</strong>.
- If the available flights are cheaper than the "lowest price" column from Google Sheets, then it will email the details about the flight using <strong>smtplib</strong> (can be changed to sms if <strong>send_sms()</strong> method is used in `main.py`)

## How to Setup the Project
1. Create an empty folder
2. Add the folder to workplace area in your VS Code and open terminal OR navigate to the created folder using terminal
3. Download the project .zip file OR Enter to the terminal:
   `git clone https://github.com/ZhenyaChan/flight_club_project.git`
4. Change the environment variables in the beginning of each file
5. Run the code by entering in the terminal `python3 ./main.py`
