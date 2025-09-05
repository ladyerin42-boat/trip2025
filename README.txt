
# Adding markers to a map

In terminal, run the server.py script in the project folder to create a localhost

cd /path/to/project (cd C:\xfp\projects\triplog)
python server.py

OR ALSO

python -m http.server 8000

Page is visible at http://localhost:8000/marker-editor.html


In the browser, visit http://localhost:8000/marker-editor.html

Workflow:

- markers-editor loads the project's markers.json file.

- Add entries. Click the location. Lat / Long are populated. Add the location name and the URL (Facebook post).
Facebook links only work if they are public.

- Save by Clicking the “Download markers.json” button.
The “Download markers.json” button in marker-editor.html just takes the 
in-memory array of markers and uses JavaScript’s Blob + URL.createObjectURL 
trick to trigger a download in the browser.

✅ It creates a brand-new file called markers.json.

✅ The browser saves it into your downloads folder (or wherever your browser normally saves files).

❌ It does not overwrite the original markers.json sitting in your project folder (or on GitHub).

After downloading, you still need to:

✅ Manually copy the new markers.json into your project folder (replacing the old one).

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