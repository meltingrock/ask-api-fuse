# FUSE JavaScript SDK Documentation

For the complete look at the FUSE JavaScript SDK, [visit our documentation.](https://fuse-docs.sciphi.ai/api-and-sdks/introduction)

## Installation

Before starting, make sure you have completed the [FUSE installation](https://fuse-docs.sciphi.ai/documentation/installation/overview).

Install the FUSE JavaScript SDK:

```bash
npm install fuse-js
```

## Getting Started

1. Import the FUSE client:

```javascript
const { fuseClient } = require('fuse-js');
```

2. Initialize the client:

```javascript
const client = new fuseClient('http://localhost:7272');
```

3. Check if FUSE is running correctly:

```javascript
const healthResponse = await client.health();
// {"status":"ok"}
```

4. Login (Optional):
```javascript
// client.register("me@email.com", "my_password"),
// client.verify_email("me@email.com", "my_verification_code")
client.login("me@email.com", "my_password")
```
When using authentication the commands below automatically restrict the scope to a user's available documents.
