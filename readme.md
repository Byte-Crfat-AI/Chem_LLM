
# 🧠 Simple RAG Pipeline using Gemini API

This is a simple template of RAG pipeline to add context in Gemini prompts using a Chroma database and Gemini Embeddings. 🌟




## 🚀 Setup
**Clone the Repository**

```bash
  git clone https://github.com/Rohitmantha/RAG-Pipeline-using-Gemini-API.git
```

**Go to the project directory**

```bash
  cd RAG-Pipeline-using-Gemini-API
```

**Install dependencies**

Make sure you have a virtual environment set up. Install the required packages using pip:
```bash
  pip install -r requirements.txt
```

**Configure Environment Variables**

Create a `.env` file in the root directory of the project and add your Google API key

```bash
  GOOGLE_API_KEY=your_google_api_key_here
```


## 📄 Populate the Database

**To populate the Chroma database with your documents:**
  1) Place your PDF documents in the ./resources/ directory.
  2) Run the populate_db.py script:

```bash
  python populate_db.py
```
This script will load PDF documents, split them into manageable chunks, and save them to the Chroma vector database. 📚

## 🔍 Query the Database
To query the database and generate answers based on the context:
Use the gen_context.py script. Pass your query as an argument:
```bash
python gen_context.py "Your query here"
```

**This script will:**
Retrieve relevant chunks from the Chroma database.
Generate a prompt based on the retrieved context and passes that to a LLM. 🤖

## 📝 How It Works

***populate_db.py*** reads and processes PDF documents, splits them into chunks, and saves them in the Chroma database.

You can tweak the parameters as you wish and get an optimal chunk size,chunk overlap and also to read from some other file type change the *.pdf in the load_documenst() function in populate_db to any other format intended.

***gen_context.py*** retrieves relevant chunks for a given query and generates a detailed answer using the Google Generative AI model

## 🎉 Contributions
Feel free to contribute to this project! Whether you have suggestions, improvements, or fixes, your input is welcome. Just fork the repo and create a pull request. 🚀
#### Contributors

- [@Rohitmantha](https://github.com/Rohitmantha)
- [@uday-sv](https://github.com/uday-sv)

