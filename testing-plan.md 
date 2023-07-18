User Acceptance Testing Script:  

Test Case 1: Page Navigation
   ## Context: User is on the home page.
   - Action: Verify the presence and functionality of the navigation sidebar.
   - Expected Outcome: The sidebar displays the user's created courses, and clicking on a course opens the respective course page.


Test Case 2: File upload/processing
   ## Context: User is attempting to upload one lecture
Action: 
Expected Outcome:.

Test Case 3: Create New Course
   ## Context: User is on the base page and navigates to the sidebar.
Action: Click on the "Create New Course" button.
 Expected Outcome: User is redirected to a blank course page where they can input/edit course details.

 Test Case 4: Create New Lecture 
 ## Context:
Action:
Expected Outcome:


Test Case 5: Study Card List View (Study card interaction/editing)
   ## Context: User is on the Study Card List View page.
   - Action: Verify the display and functionality of the list of study cards.
   - Expected Outcome: The list shows all study cards, and users can navigate, edit, and review cards easily.

Test Case 6: Summary card interaction 
## Context:
Action:
Expected outcome:

Backend unit tests:

## Module 1: File Upload/Processing

### Test Case 1.1: Uploading Files
**Purpose:**  
Tests the file uploading endpoints. Tests requirements BA1-BA3

**Procedure:**  
Load dummy video, audio, text files in the supported formats
Load dummy video, audio, text files in at least one unsupported format
Post the dummy files to the API
Receive sanity check API response

**Expected Result:**  
Success if supported formats successfully load, unsupported issue a 415 status code error; otherwise - failure

### Test Case 1.2: Video to audio conversion
**Purpose:**  
Tests the file converter functionality. Test requirement BA4

**Procedure:**  
Load dummy video file
Pass the dummy file to the file converter function
Receive the dummy audio file
**Expected Result:**  
Success if a valid dummy audio .mp3 file is produced; fail otherwise 


### Test Case 1.3: Audio transcription
**Purpose:**  
Tests the audio transcription functionality. Test requirement BA5

**Procedure:**  
Load dummy audio file
Pass the dummy file to the Whisper API
Receive the dummy transcript file
**Expected Result:**  
Success if a valid dummy transcript .txt file is produced; fail otherwise 

## Module 2: Text embeddings

### Test Case 2.1: Embedding text
**Purpose:**  
Tests the embedding LLM agent. Tests the BB2, BC6 requirements

**Procedure:**  
Load the dummy text 
Pass the dummy text to encoding embedding function 
Receive embedding of the dummy text

**Expected Result:**  
Success if the embedding is in valid vector format; fail otherwise

### Test Case 2.2: Reading a textual embedding
**Purpose:**  
Tests the embedding LLM agent. Tests the BB3 requirement

**Procedure:**  
Load the dummy text 
Pass the dummy text to encoding embedding function 
Receive embedding of the dummy text 
Pass dummy embedding to decoding embedding function 
Compare decoded embedding to original dummy text
**Expected Result:**  
Success if identical; failure otherwise

## Module 3: Large Language Model Agents

### Test Case 3.1: Labeling agent
**Purpose:**  
Tests the labeling agent. Tests BC1 requirement

**Procedure:**  
Load the dummy text 
Pass the dummy text to a labeling function 
Receive output label

**Expected Result:**  
Success if the output label is valid (no more than 50 tokens in length); fail otherwise

### Test Case 3.2: Table of contents agent
**Purpose:**  
Tests the table of contents agent. Tests the BC2 requirement

**Procedure:**  
Load the dummy text 
Pass the dummy text to a table of contents function
Receive output table of contents

**Expected Result:**  
Success if table of contents is in valid .json format; fail otherwise 

### Test Case 3.3: Summarizing agent
**Purpose:**  
Tests the summarizing agent. Tests the BC3 requirement

**Procedure:**  
Load the dummy text 
Pass the dummy text to a summarizing function
Receive output summary

**Expected Result:**  
Success if summary is in valid .json format; fail otherwise 

### Test Case 3.4: Key term agent
**Purpose:**  
Tests the key term agent. Tests the BC4 requirement

**Procedure:**  
Load the dummy text
Pass the dummy text to a key term function
Receive output key terms dictionary
**Expected Result:**  
Success if key terms is in valid dictionary format; fail otherwise

### Test Case 3.5: Study card agent
**Purpose:**  
Tests the study card agent. Tests the BC5 requirement

**Procedure:**  
Load dummy key terms dictionary 
Load the dummy text 
Pass dummy text, dummy key terms dictionary to a study card function
Receive study cards .json
**Expected Result:**  
Success if study card are in valid .json format; fail otherwise 

## Module 4: Databases

### Test Case 4.1: SQL Database Post
**Purpose:**  
Tests the User data SQL database. Partially tests the BE1-BE2 requirements 

**Procedure:**  
Load a dummy table from a dummy schema 
Post a dummy entry
Receive database response
**Expected Result:**  
Success if response is 200; fail otherwise

### Test Case 4.2: SQL Database Get
**Purpose:**  
Tests the User data SQL database. Tests the BE3 requirements

**Procedure:**  
Load a dummy table from a dummy schema 
Post a dummy entry
Get the dummy entry 
Receive database response
**Expected Result:**  
Success if response is 200, and received entry equals posted entry; fail otherwise

### Test Case 4.3: Vector Database Post
**Purpose:**  
Tests the Vector database. Tests the BD1-BD2 requirements

**Procedure:**  
Load a dummy table from a dummy vector + dummy tags
Post a dummy vector
Receive database response
**Expected Result:**  
Success if response is 200; fail otherwise

### Test Case 4.4: Vector Database Get
**Purpose:**  
Tests the Vector database. Tests the BD1-BD2 requirements

**Procedure:**  
Load a dummy table from a dummy vector + dummy tags
Post a dummy vector
Get the dummy vector using dummy tags
Receive the database response
**Expected Result:**  
Success if response is 200, and received dummy vector equals posted dummy vector; fail otherwise