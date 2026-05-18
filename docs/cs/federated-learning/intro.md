---
title: Federated Learning
sidebar_position: 0
---

# Federated Learning

![A federated learning system diagram shows a central server coordinating model updates with multiple clients holding local data.](https://commons.wikimedia.org/wiki/Special:FilePath/Federated_learning_process_central_case.png)

*Figure: The centralized federated learning loop — server broadcasts model, clients train locally, server aggregates updates without seeing raw data. Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Federated_learning_process_central_case.png), Jeromemetronome, CC BY-SA 4.0.*

Federated learning trains models across decentralized data without first copying that data into one central warehouse. A coordinating service sends a model to clients, clients improve it using local examples, and the service aggregates the updates into a new model. The appeal is not that model updates are magically private. The appeal is that raw records can stay under the control of phones, hospitals, banks, vehicles, labs, or regulated business units while still contributing to a shared learning objective.

The setting sits between machine learning, distributed systems, optimization, privacy engineering, and security. It is motivated by privacy regulation such as GDPR and HIPAA, contractual data-sovereignty constraints, high uplink cost, edge compute, and the reality that some data is valuable precisely because it is generated in local context. The canonical split is **cross-device** federated learning, with many unreliable clients such as phones or IoT devices, and **cross-silo** federated learning, with fewer more reliable institutions such as hospitals or banks. Both use the same basic server-client loop, but they differ sharply in availability, trust, auditing, communication budgets, and tolerance for manual governance.

This chapter sequence is a graduate-level survey. It begins with the FedAvg baseline, then studies what breaks under non-IID data and system heterogeneity. The middle chapters cover personalization, privacy, secure aggregation, communication reduction, Byzantine robustness, and backdoors. The final chapter connects the older mobile-keyboard motivation to modern systems for healthcare, finance, recommendation, and foundation-model fine-tuning.

1. [Foundations and FedAvg](/cs/federated-learning/foundations-and-fedavg)
2. [Heterogeneity and Federated Optimization](/cs/federated-learning/heterogeneity-and-optimization)
3. [Personalization in Federated Learning](/cs/federated-learning/personalization-in-federated-learning)
4. [Privacy: Differential Privacy and Secure Aggregation](/cs/federated-learning/privacy-differential-and-secure-aggregation)
5. [Communication Efficiency and Robustness](/cs/federated-learning/communication-efficiency-and-robustness)
6. [Applications and Systems](/cs/federated-learning/applications-and-systems)
