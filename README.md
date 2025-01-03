# Get Autodance from Just Dance for Wii U (tested for 2019)

## Use FTPiiU_Everywhere to access Wii U memory:
https://hb-app.store/wiiu/ftpiiu-cbhc (downloaded and run via homebrew)  
https://github.com/wiiu-env/ftpiiu_plugin (runs via plugins)  
https://www.youtube.com/watch?v=LTiN1aW-hqQ (how to use ftpiiu)  

## Where to find save files:
https://gbatemp.net/threads/extract-just-dance-autodance-video.493341 (if you can't open storage_usb, try storage_slc)  

## How to get the name of the folder with the desired save files:
https://wiiubrew.org/wiki/Title_database

## Extraction
(Start with the JDSave_1 save file, JDSave_0 save file used for something else)
1. Name the save file as 'input.bin' or change the input file name in run.py, on the line input_file = 'input.bin'
2. Put input.bin in the same folder as run.py
2. Run the run.py script
3. The result will be saved in the output.webm file in the same folder