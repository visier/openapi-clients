## Overview
Visier, Inc. publishes the [OpenAPI v3](https://spec.openapis.org/oas/latest.html) definitions of a growing list of its public APIs to ease the development of client applications against the Visier platform. OpenAPI v3 is a language-agnostic definition, enabling (among other things) the programmatic generation of client-level interface wrappers that substantially reduce the amount of code that has to otherwise be written manually in libraries or directly in applications.

Visier's Public APIs are classified according to:
* **Administration** - APIs to perform administrative tasks such as managing permissions.
* **Authentication** - Get secure access to the Visier platform.
* **Data-In** - APIs for loading data and monitoring jobs.
* **Data-Out** - Query and data extraction APIs.
* **Modeling** - Query the Visier catalog for object metadata.

## Usage
Visier usese these definitions to generate end-user content like reference documentation as well as SDKs (currently Python is available).

Developers using other languages are encouraged to generate the API wrappers using a tool of their choice and then write their application to make Visier public API calls using these wrappers.

OpenAPI v3 client-wrappers can be generated using freely available tools as well as using commercially supported options.

## License
The Visier OpenAPI v3 definitions are published under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
