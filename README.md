# INFO 5940 
Welcome to the INFO 5940 repository. You will complete your work using [**GitHub Codespaces**](#about-github-codespaces) and save your progress in your own GitHub repository. This guide will walk you through setting up the development environment and running the test notebook.  

## Getting Started 

### Step 1: Fork this repository 
1. Click the **Fork** button (top right of this page).
2. This will create a copy of the repo under **your own GitHub account**.

Forking creates a personal copy of the repo under **your** GitHub account.  
- You can commit, push, and experiment freely.  
- Your work stays separate from the official class materials.

### Step 2: Open your forked repo Codespace
1. Go to **your forked repo**.
2. Click the green **Code** button and switch to the **Codespaces** tab.  
3. Select **Create Codespace**.
4. Wait a few minutes for the environment to finish setting up.

### Step 3: Verify your environment 
Once the Codespace is ready: 
1. If you are in `<your-file-name>.ipynb` in your codespace.
2. Install the Python 3.11.13 Kernel.  In the top-right corner, click **Select Kernel**.
    1. If **Install/Enable suggested extensions Python + Jupyter** appears, select it, and wait for the install to finish before moving on to the next step.
    2. Select **Python Environments** choose **Python 3.11.13 (first option)**.
3. Run the code block to check your setup. 

## About GitHub Codespaces

[Codespaces](https://docs.github.com/en/codespaces) is a complete software development and execution environment, running in the cloud, with its primary interface being a VSCode instance running in your browser.

Codespaces is not free, but their per-month [free quota](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces#free-quota) is generous.  Codespaces is free under the [GitHub Student Developer Pack](https://education.github.com/pack#github-codespaces).

### Codespaces Tips

* Codespaces keep running even when you close your browser (but will time out and stop after a while)
* Unless you're on a free plan, or within your free quota, costs acrue while the codespace is running, whether or not you have it open in your browser or are working on it
* You can control when it's running, and the space it takes up.  Check out [GitHub's codespaces lifecycle documentation](https://docs.github.com/en/codespaces/about-codespaces/understanding-the-codespace-lifecycle)

## Sync Updates 
To make sure your personal forked repository stays up to date with the original class repository, please follow these steps:
1. Open your forked repo.
2. At the top of the page, you should see a banner or menu option that shows whether your fork is behind the original repo.
3. Click the **Sync fork** button.
4. In the dropdown, choose **Update branch** to pull the latest changes from the original repo into your fork.

Optionally, you can also follow these steps to create a new branch on your fork:
1. Open your **forked repository** on GitHub.  
2. At the top of the page, next to the branch dropdown, click the **Branches** button.  
3. In the **Branches** view, click the green **New Branch** button.  
4. In the popup window, enter a branch name.  
   - You can use any name you like, but it’s recommended to match the branch name used in class for better organization.  
5. Under **Branch source**, select:  
   - **Repository:** `AyhamB/INFO-5940-Codespace`  
   - **Branch:** choose the branch you want to sync from (e.g., `streamlit`).  
6. Click the green **Create New Branch** button.  
7. Verify that you’re now back in **your fork**, on the new branch you just created.  
8. Click the **Code** button and create a new Codespace (if you don’t already have one).  
   - Make sure the Codespace is created from the **current branch**.
  
## Running a Streamlit App on Codespaces  
Follow these steps to launch and view your Streamlit app in GitHub Codespaces:
1. **Open the terminal** inside your Codespace.
2. Run the command:  
   ```bash
   streamlit run your-file-name.py
   ```  
   **(Replace `your-file-name.py` with the actual name of your Streamlit app file, e.g., `hello_app.py`.)**
3. After pressing **Enter**, a popup should appear in the bottom-right corner of Codespace editor.  
   - Click **“Open in Browser”** to view your app.  

   ⚠️ *If you miss the popup:*  
   - Press **Ctrl + C** in the terminal to stop the app.  
   - Rerun the command from step 2 — the popup should appear again.
4. A new browser tab will open, showing the interface of your Streamlit app.
5. **Make changes to your code** in the Codespace editor.  
   - Refresh the browser tab to see the updated version of your app.  

## Setting Your API Key in GH Codespaces
You will receive an individual API Key for class assignments. To prevent accidental exposure online, please follow the steps below to securely insert your key in the terminal.
1. **Open the terminal** inside your Codespace.
2. Run the command to temporarily set your API Key for this session:  
   ```bash
   export API_KEY="your_actual_API_KEY"
   ```
3. If you want to run the Streamlit app and set up the key at the same time, run both commands together:
   ```bash
   API_KEY="your_actual_API_KEY" streamlit run your-file-name.py
   ```

## Troubleshooting
- The Jupyter extension should install automatically. If you still cannot select a Python kernel on Jupyter Notebook: Go to the left sidebar >> **Extensions** >> search for **Jupyter** >> reload window (or reinstall it).

## RAG Application

### Overview
This application allows users to upload `.txt` and `.pdf` documents and have a conversation with their content. It uses **LangChain** for the Retrieval-Augmented Generation (RAG) pipeline and **Streamlit** to create a chat-style web interface. It stores your document data in **ChromaDB** for fast and accurate retrieval.

### Features
- Upload `.txt` and `.pdf` files.
- Support for multiple document uploads.
- Document chunking for efficient processing of large files.
- Conversational interface for querying document content.

### Setup Instructions

1. **Install Dependencies**:
   Make sure you are in the provided Codespace environment. Run the following command to install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   Start the Streamlit application by running:
   ```bash
   streamlit run chat_with_pdf.py
   ```

3. **Upload Documents**:
   - Use the file uploader to upload `.txt` or `.pdf` files.
   - Ask questions about the uploaded documents with the chat interface.

### Notes
- Before running the app, make sure your OpenAI API key is saved as the environment variable `API_KEY`.
- The app uses ChromaDB as its vector database to store, search, and retrieve document information efficiently.

### Changes to Provided Setup
- Added `chromadb` to `requirements.txt` to enable vector database functionality.
- Updated chat_with_pdf.py to support both .txt and .pdf uploads, document chunking, and full RAG pipeline integration.
