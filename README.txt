
# Overview

Add markers to a JSON file and show the markers on a map.

Markers are added using markers-editor.html which runs on the local machine.  
Edited marker file is temporarily saved to the Downloads folder and must be copied back to the project folder.
Use Visual Studio to push the updated project to github.

Markers are shown on index.html at https://ladyerin42-boat.github.io/trip2025/index.html?nocache=1




# Adding markers to a map

## Run the editor page locally

In terminal, run the server.py script in the project folder to create a localhost

cd /path/to/project (cd C:\xfp\projects\triplog)
python server.py

OR ALSO

python -m http.server 8000

Page is visible at http://localhost:8000/marker-editor.html

## Edit the current trip file

The page loads a default file eg south_2025.json. Edit the 'defaultFile' const to work on a new trip. 

Add entries by clicking on map. Click the location. Lat / Long are populated. Add the location name and the URL (Facebook post).
Facebook links only work if they are public.

Save the markers by Clicking the “Download markers.json” button.
The “Download markers.json” button in marker-editor.html takes the 
in-memory array of markers and uses JavaScript’s Blob + URL.createObjectURL 
trick to trigger a download in the browser.

✅ It creates a brand-new file (called [defaultFile].json.

✅ The browser saves it into the downloads folder.

❌ It does not overwrite the original json sitting in your project folder (or on GitHub).

After downloading, you still need to:

✅ Manually copy the new json file into your project folder (replacing the old one).

✅ Commit and push it to GitHub so Pages can serve the updated markers.
To Add a Marker:



After updating the markers file, the changed file is synced to the github repo.


# How to sync files to github

In Visual Studio:

- View, Git changes
- Any changed files appear
- Add a comment
- Commit and Push

If everything works correctly, the changed files are synced to the github project.



# Viewing entries

The updated markers.json file is used by github pages to serve the page. 
After uploading to github, the new index.html page should be visible in a few seconds or minutes, 

Page is served from 
https://ladyerin42-boat.github.io/trip2025/

Try CTRL-SHIFT-R to force the browser to request a new version of the page (not use cache)

OR try

https://ladyerin42-boat.github.io/trip2025/index.html?nocache=1


# Changes

Working on a version of index.html that allows the user to select a marker.json file (representing separate trips)