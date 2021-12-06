# Book`s rating predictor

## Description
The project based on machine learning algorythm and attached web service.
The main goal is creating model that makes the most accurate rating prediction based on few input features.

## Relevance
There are not any similar solution. Most of presented services are paid or their prediction are less accurate.
Our product is simple to use, also we can accept API requests. Our solution helps people to make a decision what book they should order.

## Functionality
At the web service user can fill input parameters (upload book cover, choose genres, type in authors, select number of pages
and number of book reviews). After that empty fields are filling with zeros. Finally, user gets prediction and warnings on missed fields.
User can fill missed features and get more accurate prediction.

## Technology stack

**Python**

`Python` is one of the most popular programming language. The key features:
* Simple and easy syntax.
* Developing speed. Python allows you to develop MVP in few month, then you can test your business solution and be the first at world market. 
* Community. There are a lot of enthusiasts who are working on additional features and developing new functionality.
* Accessibility & Versatility. You can use `Python` to solve different tasks from web developing to ML solutions. 

To develop ML solution, you have to use `Python`, because it has libraries that make your development easier and faster, such as `NummPy`, 
`Scikit-learn`, `Pandas` and others.

**Streamlit**

`Streamlit` is an open-source Python library (available from `Python` 3.6) that makes it easy to create and share beautiful, custom web apps for machine learning and data science.
`Streamlit` makes it easy for you to visualize, mutate, and share data. The API reference is organized by activity type, like displaying data or optimizing performance.
We used this library, because it is simple in deploy and it also has lots of pre-defined methods to visualize data and interactive widgets.

**FastAPI**

`FastAPI` is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. 
The key features are:
* Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic)
* Fast to code: Increase the speed to develop features by about 200% to 300%.
* Fewer bugs: Reduce about 40% of human (developer) induced errors.
* Intuitive: Great editor support. Completion everywhere. Less time debugging.
* Easy: Designed to be easy to use and learn. Less time reading docs.
* Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* Robust: Get production-ready code. With automatic interactive documentation.

Comparing to `Flask`, we pay attention at `FastAPI` working speed. It was one of the biggest effort, because we have machine learning algorythm working
at the backend and we can not waste time on requests.

## Schema

![diagram](https://github.com/shooterdimon/int20h/blob/master/diagrams/ux.png)
## Timeline

![timeline](https://github.com/shooterdimon/int20h/blob/master/diagrams/timeline.png)

