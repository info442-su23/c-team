# Requirements.md

## Front-End (A)

### Base Page (AA)
1. Contains a scrollable navigation sidebar for the user-created courses.
2. Features a pop-up menu for each of the courses, allowing direct access to any lecture subdirectory or course material that was previously uploaded.
3. Offers a "Create New Course" button.
4. Includes a "Logout" button.
5. Provides a "Go Home" button.
6. Shows an "Account Settings" button.

### Home Page (AB)
1. When the user is logged in, the page displays highlights of the user's created courses.
2. Includes a search bar for finding user-created and public courses.
3. Shows a pop-up menu dividing the searched courses into the ones created by the user and public ones.
4. Recommends suggested public courses.

### Course Page (AC)
1. Contains two sections:
    - **Left Section:** (ACA)
        1. Opens a new page when the "Create New Course" button is clicked.
        2. Redirects to a blank course page where the user can input/edit the course name, description, and icon.
    - **Right Section:** (ACB)
        1. Contains a "Create New Lecture" button.
        2. Features a scrollable sidebar for previously created lectures.

### Lecture Page (AD)
1. Opens when the "New Lecture" button is clicked, redirecting to an empty lecture page.
2. The page contains two sections:
    - **Left Section:** (ADA)
        1. Allows users to enter the lecture number, dates, and an optional name.
        2. Shows the lecture recording, a description of it, and a full transcript once the materials are uploaded.
        3. Redirects to the handout if it is uploaded.
    - **Right Section:** (ADB)
        1. Contains three redirection buttons (Lecture summary, Handout, Study card) that become available based on the uploaded materials.
        2. Features an "Upload File" button, which shows a pop-up menu for dragging and dropping a file or choosing a file to upload.
        3. Provides a list of accepted file types for lecture recordings (video and audio) and handouts.
        4. Shows an error message if an inappropriate file format is uploaded or if there is an error with the file upload.
        5. Displays a "loading" pop-up with an option to cancel the upload when a file is being uploaded.
        6. Refreshes the page and displays a success message when a file is successfully uploaded.

### Summary Page (AE)
1. The page is identical for lecture and handout summaries.
2. Contains two sections:
    - **Left Section:** A scrollable navigation sidebar with a list of hyperlinks.
    - **Right Section:** Scrollable and editable text blocks with new headers reflecting the current state of the headers.
3. By default, the page is filled with processed materials from the uploaded files.
4. Provides a "Return to Lecture" button.

### Study Card Pages (AF)
1. Three different views are available:
    - **Card View:** Displays an individual study card with an editable term and definition.
    - **List View:** Shows all study cards in a scrolling list, with editable terms and definitions.
    - **Study View:** Interacts with each study card one by one. The user answers the prompt or question and clicks the "See Result" button to get feedback. 

## Back-End (B)

### Data Processing Backend (BA)
1. The submissions API should accept multiple file types: 
    - Videos: ".mp4", ".mkv", ".avi", ".flv", ".mov", ".wmv".
    - Audios: ".mp3", ".mp4a", ".m4p", ".raw", ".wav".
    - Docs: ".pdf", ".docx", ".rtf", ".txt".
2. If an unsupported filetype is submitted, the API should reject the request with a 415 status code and a message about supported file types.
3. If there's an issue reading any of the submitted files, the API should reject the request with a 400 status code and a message about the files being unreadable.
4. The file conversions API should extract audio from submitted video files and convert it to ".mp3".
5. The transcription API should extract text from audio files and save it as a ".txt" file, utilizing a locally-hosted Whisper model.
6. The backend should be capable of initializing a Chroma Vector database and a PostgreSQL user database, and storing and retrieving data from them.
7. It should store the submitted video, audio, and text files in the PostgreSQL user database.

### LLM API (BB)
1. It should format inputs for LLM agents tiktoken and OpenAI documentation and format outputs from the vector database for display on the front-end.
2. Upon accepting outputs from LLM agents, it should embed them using the embedder agent and store the embeddings in the Chroma vector database.
3. It should retrieve data from the Chroma vector database, convert it into text via the LLM embedder agent, and format it for display on the frontend.
4. It should submit requested text, audio, and video data to the frontend upon request.

### LLM Agents (BC)
1. The LLM labeling agent should map provided texts by tagging text chunks.
2. The LLM table of contents agent should form a table of contents for provided texts using tag maps and text chunks.
3. The LLM summarizing agent should summarize provided text chunks using a provided table of contents for context.
4. The LLM key term agent should extract key terms from provided text chunks, using summaries for context.
5. The LLM study card agent should compile term-definition pairs using provided key terms and summaries for context.
6. The embedder LLM agent should vectorize provided text tokens into a vector database-compatible format.
7. LLM agents should accept their according inputs from the data processing backend and submit their according outputs to the data processing backend.

### Chroma Vector Database (BD)
1. It should be able to create, edit, and delete tables with provided dimensions and meta-tags.
2. It should store and retrieve embeddings using semantic search and meta-tag search.

### User Data Database (BE)
1. It should be able to create, edit, and delete tables with provided fields.
2. It should store raw video, audio, text documents, and other non-vectorized data along with meta-tags from the vector database.
3. It should retrieve the stored files via queries using meta-tags.