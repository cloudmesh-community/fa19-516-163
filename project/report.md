# Project Proposal

## Students

Kenneth Jones (fa19-516-146)  
John Hoerr (fa19-516-163)

## Description

We are interested in comparing the cold- and warm-start performance of
serverless REST APIs across multiple clouds and a mix of interpreted and
compiled languages. We will use the Serverless Framework to provision and deploy
the functions to their respective clouds. Among the outputs of our project will
be an OpenAPI 3.0 spec and a performance matrix for each cloud and language. The
goal of this analysis is to better understand the state of serverless platform
performance and to provide guidance for developers wishing to find the highest
performing cloud for their chosen language/stack. This proposal can be extended
to include more clouds as time allows.

## Platforms

* Cloudmesh Commandline interface to derive from specifications deplyment and running functions
* Abstract REST Service interface in OPENAPI
- AWS Lambda
- Azure Functions
- GCP Functions

## Languages

Primary:
- Python 3.7 the APIs defined with puthon will be integrated into conexion with the help of Operantion Ids

Secondary, derived form OpenAPI 3 specification:
- Node.js 10
- C# 8 or F# 4.7 (.Net Core)
