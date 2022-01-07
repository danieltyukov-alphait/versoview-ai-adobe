# Requirements:

pip install pdfservices-sdk
python version: 3.6 =< ...

(I am using Python 3.10)

## Solution Tool

https://www.adobe.io/apis/documentcloud/dcsdk/pdf-extract.html

## Docs

https://www.adobe.io/apis/documentcloud/dcsdk/docs.html?view=extract

This tool is an SDK so we do not have to provide our own templatefor extraction is better as the Publisher may post documents that we may not have prepared for, plus ADOBE has an in-built AI tool which organizes and spots the data without the requirements of us writing that manually.

In the following sample I provided a simple example for Text Extraction, but it can spot, images, tables and structure them out differently.

It provides the data in JSON format, so we can after that work with the front-end team to convert it to Markdown for editing purposes if the writer will be willing to perform it.

## Credentials

I have created a personal Adobe Developer Console Account for the time being.

https://developer.adobe.com/console/home

login: Daniel.Tyukov@alphait.us

pass: !BCmS5u}YsD?#XK

project: alphait-versoviewai