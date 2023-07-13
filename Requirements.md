# Requirements.md

## Front-End

### Base Page
1. Contains a scrollable navigation sidebar for the user-created courses.
2. Features a pop-up menu for each of the courses, allowing direct access to any lecture subdirectory or course material that was previously uploaded.
3. Offers a "Create New Course" button.
4. Includes a "Logout" button.
5. Provides a "Go Home" button.
6. Shows an "Account Settings" button.

### Home Page
1. When the user is logged in, the page displays highlights of the user's created courses.
2. Includes a search bar for finding user-created and public courses.
3. Shows a pop-up menu dividing the searched courses into the ones created by the user and public ones.
4. Recommends suggested public courses.

### Account Settings Page
1. Allows the user to change the password, name, or the email associated with the account.

### Course Page
1. Contains two sections:
    - **Left Section:**
        1. Opens a new page when the "Create New Course" button is clicked.
        2. Redirects to a blank course page where the user can input/edit the course name, description, and icon.
    - **Right Section:**
        1. Contains a "Create New Lecture" button.
        2. Features a scrollable sidebar for previously created lectures.

### Lecture Page
1. Opens when the "New Lecture" button is clicked, redirecting to an empty lecture page.
2. The page contains two sections:
    - **Left Section:**
        1. Allows users to enter the lecture number, dates, and an optional name.
        2. Shows the lecture recording, a description of it, and a full transcript once the materials are uploaded.
        3. Redirects to the handout if it is uploaded.
    - **Right Section:**
        1. Contains three redirection buttons (Lecture summary, Handout, Study card) that become available based on the uploaded materials.
        2. Features an "Upload File" button, which shows a pop-up menu for dragging and dropping a file or choosing a file to upload.
        3. Provides a list of accepted file types for lecture recordings (video and audio) and handouts.
        4. Shows an error message if an inappropriate file format is uploaded or if there is an error with the file upload.
        5. Displays a "loading" pop-up with an option to cancel the upload when a file is being uploaded.
        6. Refreshes the page and displays a success message when a file is successfully uploaded.

### Summary Page
1. The page is identical for lecture and handout summaries.
2. Contains two sections:
    - **Left Section:** A scrollable navigation sidebar with a list of hyperlinks.
    - **Right Section:** Scrollable and editable text blocks with new headers reflecting the current state of the headers.
3. By default, the page is filled with processed materials from the uploaded files.
4. Provides a "Return to Lecture" button.

### Study Card Pages
1. Three different views are available:
    - **Card View:** Displays an individual study card with an editable term and definition.
    - **List View:** Shows all study cards in a scrolling list, with editable terms and definitions.
    - **Study View:** Interacts with each study card one by one. The user answers the prompt or question and clicks the "See Result" button to get feedback. 

## Back-End
