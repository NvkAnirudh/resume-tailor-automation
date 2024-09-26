---
title: Resume Tailor
emoji: 👁
colorFrom: yellow
colorTo: purple
sdk: streamlit
sdk_version: 1.38.0
app_file: app/streamlit_app.py
pinned: false
license: mit
---

<a id="readme-top"></a>

![GitHub License](https://custom-icon-badges.demolab.com/github/license/NvkAnirudh/resume-tailor-automation?logo=law)
![Last Commit](https://custom-icon-badges.demolab.com/github/last-commit/NvkAnirudh/resume-tailor-automation?logo=history&logoColor=white)
![](https://custom-icon-badges.demolab.com/github/languages/code-size/NvkAnirudh/resume-tailor-automation?logo=file-code&logoColor=white)
![](https://custom-icon-badges.demolab.com/github/stars/NvkAnirudh/resume-tailor-automation?logo=star&style=social&logoColor=black)
![](https://custom-icon-badges.demolab.com/github/forks/NvkAnirudh/resume-tailor-automation?logo=fork&style=social&logoColor=black)
![](https://custom-icon-badges.demolab.com/github/watchers/NvkAnirudh/resume-tailor-automation?logo=eye&style=social&logoColor=black)

<!-- PROJECT LOGO -->
<br />
<div align="center">
<!--   <a href="https://github.com/sandesh-bharadwaj/VidTune"> -->
  <img src="https://github.com/user-attachments/assets/8ba70d9d-e2c6-4225-b29c-95e3d5080dd2" alt="Logo" width="80" height="80">
<!--   </a> -->

  <h3 align="center">Resume Optimizer</h3>

  <p align="center">
    Automation of Resume Tailoring
    <br />
    <br />
  </p>
</div>

If you find this project helpful, I'd appreciate it if you could give this repo a star ⭐ Cheers!

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#problem-statement">Problem Statement</a></li>
    <li><a href="#project-overview">Project Overview</a></li>
    <li><a href="#source-code">Source Code</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#deployment">Deployment</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#pricing">Pricing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contributions">Contributions</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## Introduction
This project automates the tailoring of resumes to a given job description using the Claude 3.5 sonnet model from Anthropic. The goal is to save time and increase efficiency in the job application process.

### Built With
![](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)
![](https://img.shields.io/badge/Anthropic%20Claude%20-8A2BE2.svg?logo=anthropic)
![](https://img.shields.io/badge/Hugging%20Face-FFD21E?logo=huggingface&logoColor=000)
![](https://img.shields.io/badge/Google%20Docs%20-FFFFFF.svg?logo=googledocs)
![](https://img.shields.io/badge/Streamlit%20-FF4B4B.svg?logo=streamlit&logoColor=white)

<p align="right">(<a href="#readme-top">top</a>)</p>

## Problem Statement
Tailoring a resume to a job description can be a tedious and time-consuming process. This project aims to consolidate everything in one place, allowing users to simply copy-paste the job description and update their resume accordingly.

<p align="right">(<a href="#readme-top">top</a>)</p>

## Project Overview
The project consists of the following components:
- A Streamlit application for user input and output
- A Python script for Google Docs API authentication and text styling
- A source code directory containing the following files:
  - api_client.py: initializes the Claude 3.5 sonnet model
  - config.py: initializes the required Anthropic API key
  - pdf_handler.py: reads and returns the attached PDF content
  - resume_analyzer.py: initializes the prompt and passes it to the Claude 3.5 API
  - text_processing.py: processes the response from Claude to output a structured analysis and updated resume
 
<p align="right">(<a href="#readme-top">top</a>)</p>

## Source Code
The source code is organized into the following directories and files:
  - ```app```: contains the Streamlit application code
  - ```src```: contains the source code files listed above
  - ```credentials_creation.py```: generates the credentials.py file for Google Docs API authentication

<p align="right">(<a href="#readme-top">top</a>)</p>

## Getting Started
To get started in the **local environment**, follow these steps:
1. Clone the repository using git clone https://github.com/your-username/resume-tailor-automation.git
2. Install the required packages using pip install -r requirements.txt
3. Set up your Anthropic API key as an environment variable
4. Enable the ```Google Docs API``` on GCP console by going to APIs & Services -> Enabled APIs & Services -> 'Search for Google Docs API'
5. Download the ```credentials.json``` file from GCP console after creating a OAuth2.0 Client ID by going to Credentials -> OAuth 2.0 Client IDs (you may want to fill out the OAuth Consent Screen first)
6. Once you have all the required keys, you can run ```app/streamlit_app.py```

<p align="right">(<a href="#readme-top">top</a>)</p>

## Deployment
The application was deployed on Hugging Face Spaces using GitHub Actions.

To get started in **Hugging Face Spaces**, follow these steps:
1. Create your own GitHub repo
2. Create a **GitHub Secret**  with your ```HF_Token``` (access token from Hugging Face)
3. Go to ```Actions``` in your GitHub repo, click **Set up a workflow yourself** and add the yml file from [Hugging Face Spaces documentation](https://huggingface.co/docs/hub/spaces-github-actions)
4. Since you won't have your ```credentials.json``` (because you put this file in .gitignore so that it doesn't get committed), add ```Google Client ID``` and ```Google Client Secret``` to Spaces environment variables. This is when you need ```credentials_creation.py``` to create a credentials.json file.
5. Once the above steps are executed properly, your app should be up and running.

<p align="right">(<a href="#readme-top">top</a>)</p>

## Usage
To use the application, follow these steps:
1. Copy-paste the job description into the input field
2. Upload your resume as a PDF file
3. Click the "Optimize Resume" button to generate an updated resume

<p align="right">(<a href="#readme-top">top</a>)</p>

## Pricing
The pricing for using the Claude 3.5 sonnet model can be found [here](https://docs.anthropic.com/en/docs/about-claude/models#model-comparison-table)

<p align="right">(<a href="#readme-top">top</a>)</p>

## License
This project is licensed under [MIT](https://github.com/NvkAnirudh/resume-tailor-automation/blob/main/LICENSE).

<p align="right">(<a href="#readme-top">top</a>)</p>

## Contributions
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

<p align="right">(<a href="#readme-top">top</a>)</p>

## Contact
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nvkanirudh/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:nuti.krish4@gmail.com)

<p align="right">(<a href="#readme-top">top</a>)</p>

## Acknowledgements
- Anthropic
- Google



