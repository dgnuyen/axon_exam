# axon_exam

1. Microservice to consume JSON file:

    -   The script named "redact_ppls_name.py" for processing JSON url.
    -   Therecord folder using Django framework to setup a microservice. 

2. Packaging the service and deploy to local k8s:

    -   The Dockerfile inside folder "therecord" can be run to package the service into container.
    -   YAML files "therecord-deployment.yaml" & "therecord-svc.yaml" can be run to deploy the microserivce in to local k8s by creating deployment resource and service resource then expose the service via NodePort mode.

3. CI process will be described in "CI_document.docx"
