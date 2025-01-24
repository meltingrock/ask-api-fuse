<img width="1041" alt="fuse" src="https://github.com/user-attachments/assets/b6ee6a78-5d37-496d-ae10-ce18eee7a1d6">
<h3 align="center">
  Containerized, Retrieval-Augmented Generation (RAG) with a RESTful API.
</h3>

<div align="center">
   <div>
      <h3>
         <a href="https://app.sciphi.ai">
            <strong>Sign up</strong>
         </a> ·
         <a href="https://fuse-docs.sciphi.ai/self-hosting/installation/overview">
            <strong>Self Host</strong>
      </h3>
   </div>
   <div>
      <a href="https://fuse-docs.sciphi.ai/"><strong>Docs</strong></a> ·
      <a href="https://github.com/SciPhi-AI/FUSE/issues/new?assignees=&labels=&projects=&template=bug_report.md&title="><strong>Report Bug</strong></a> ·
      <a href="https://github.com/SciPhi-AI/FUSE/issues/new?assignees=&labels=&projects=&template=feature_request.md&title="><strong>Feature Request</strong></a> ·
      <a href="https://discord.gg/p6KqD2kjtB"><strong>Discord</strong></a>
   </div>
   <br />
   <p align="center">
    <a href="https://fuse-docs.sciphi.ai"><img src="https://img.shields.io/badge/docs.sciphi.ai-3F16E4" alt="Docs"></a>
    <a href="https://discord.gg/p6KqD2kjtB"><img src="https://img.shields.io/discord/1120774652915105934?style=social&logo=discord" alt="Discord"></a>
    <a href="https://github.com/SciPhi-AI"><img src="https://img.shields.io/github/stars/SciPhi-AI/FUSE" alt="Github Stars"></a>
    <a href="https://github.com/SciPhi-AI/FUSE/pulse"><img src="https://img.shields.io/github/commit-activity/w/SciPhi-AI/FUSE" alt="Commits-per-week"></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-purple.svg" alt="License: MIT"></a>
    <a href="https://gurubase.io/g/fuse"><img src="https://img.shields.io/badge/Gurubase-Ask%20FUSE%20Guru-006BFF" alt="Gurubase: FUSE Guru"></a>
  </p>
</div>

# About
FUSE (RAG to Riches) is the most advanced AI retrieval system, supporting Retrieval-Augmented Generation (RAG) with production-ready features. Built around a containerized RESTful API, FUSE offers multimodal content ingestion, hybrid search functionality, knowledge graphs, and comprehensive user and document management.

For a more complete view of FUSE, check out the [full documentation](https://fuse-docs.sciphi.ai/).


## Key Features
- [**📁 Multimodal Ingestion**](https://fuse-docs.sciphi.ai/documentation/documents): Support for over 26 files types, including `.txt`, `.pdf`, `.json`, `.png`, `.mp3`, and more.
- [**🔍 Hybrid Search**](https://fuse-docs.sciphi.ai/documentation/hybrid-search): Combine semantic and keyword search with reciprocal rank fusion for enhanced relevancy.
- [**🔗 Knowledge Graphs**](https://fuse-docs.sciphi.ai/cookbooks/graphs): Automatically extract entities and relationships, build knowledge graphs, and run GraphRAG.
- [**🗂️ User Management**](https://fuse-docs.sciphi.ai/self-hosting/user-auth): Efficiently manage documents and user roles within FUSE.
- [**🔭 Observability**](https://fuse-docs.sciphi.ai/self-hosting/observability): Observe and analyze your RAG engine performance.
- [**🧩 Configuration**](https://fuse-docs.sciphi.ai/self-hosting/configuration/overview): Setup your application using intuitive configuration files.
- [**🖥️ Dashboard**](https://github.com/SciPhi-AI/FUSE-Application): An open-source React+Next.js admin dashboard to interact with FUSE via GUI.


## Getting Started

### [SciPhi Cloud](https://app.sciphi.ai)

Access FUSE through a deployment managed by the SciPhi team, which includes a generous free-tier. No credit card required.

## Self Hosting

Install FUSE:

```bash
# Install the FUSE package
pip install fuse

# Set necessary environment variables
export OPENAI_API_KEY=sk-...

# Run the server and database
fuse serve --docker --full
```

The command above will install the `full` installation which includes Hatchet for orchestration and Unstructured.io for parsing.


## Resources and Cookbooks

- [Quickstart](https://fuse-docs.sciphi.ai/documentation/quickstart): A quick introduction to FUSE's core features
- [Self Hosting Installation](https://fuse-docs.sciphi.ai/self-hosting/installation/overview): Self hosted installation of FUSE
- [API & SDKs](https://fuse-docs.sciphi.ai/api-and-sdks/introduction): API reference and Python/JS SDKs for interacting with FUSE

- Advanced Retrieval
  - [RAG Agent](https://fuse-docs.sciphi.ai/documentation/agent): FUSE's powerful RAG agent
  - [Hybrid Search](https://fuse-docs.sciphi.ai/documentation/hybrid-search): Introduction to hybrid search
  - [Advanced RAG](https://fuse-docs.sciphi.ai/documentation/advanced-rag): Advanced RAG features

### Cookbooks

- [Ingestion](https://fuse-docs.sciphi.ai/cookbooks/ingestion): Learn how to ingest, update, and delete documents with FUSE
- [Knowledge Graphs](https://fuse-docs.sciphi.ai/cookbooks/graphs): Building and managing graphs through collections
- [Orchestration](https://fuse-docs.sciphi.ai/cookbooks/orchestration): Learn how orchestration is handled inside FUSE
- [Maintenance & Scaling](https://fuse-docs.sciphi.ai/cookbooks/maintenance): Learn how to maintain and scale your FUSE system
- [Web Development](https://fuse-docs.sciphi.ai/cookbooks/web-dev): Learn how to build webapps powered by RAG using FUSE


## Community

[Join our Discord](https://discord.gg/p6KqD2kjtB) to get support and connect with both the FUSE team and other developers in the community. Whether you're encountering issues, looking for advice on best practices, or just want to share your experiences, we're here to help.

## Contributing

We welcome contributions of all sizes! Here's how you can help:

- Open a PR for new features, improvements, or better documentation.
- Submit a [feature request](https://github.com/SciPhi-AI/FUSE/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=) or [bug report](https://github.com/SciPhi-AI/FUSE/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=)

### Our Contributors
<a href="https://github.com/SciPhi-AI/FUSE/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=SciPhi-AI/FUSE" />
</a>
