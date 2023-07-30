import os
import json
from kubernetes import client, config


class KubernetesManager:
    COMMONLY_IGNORED_CONFIGMAPS = ["kube-root-ca.crt"]
    DEFAULT_NAMESPACE = os.getenv("DEFAULT_NAMESPACE", "default")
    IN_CLUSTER = bool("true" == str(os.getenv("IN_CLUSTER", "false")).lower())

    def __init__(self):
        if self.IN_CLUSTER:
            config.load_incluster_config()
        else:
            config.load_kube_config()
        aApiClient = client.ApiClient()
        self.api = client.CoreV1Api(aApiClient)

    def format_kubernetes_api_exception(self, exception: client.ApiException):
        error = json.loads(exception.body)
        formatted_error = {"message": error["reason"], "errors": {}}
        error_details = error["details"]
        if "causes" in error_details:
            for item in error["details"]["causes"]:
                formatted_error["errors"][item["field"]] = item["message"]
        else:
            formatted_error["errors"]["__all__"] = error["message"]
        return formatted_error

    def get_configmaps(self):
        formatted_configmaps = []
        configmaps = self.api.list_namespaced_config_map(
            self.DEFAULT_NAMESPACE, pretty=True, watch=False
        )
        for item in configmaps.items:
            if item.metadata.name not in self.COMMONLY_IGNORED_CONFIGMAPS:
                formatted_configmaps.append({"name": item.metadata.name})
        return formatted_configmaps

    def get_configmap(
        self, configmap_name: str, should_format=False
    ) -> client.V1ConfigMap | dict:
        configmap = self.api.read_namespaced_config_map(
            configmap_name, self.DEFAULT_NAMESPACE
        )
        if should_format:
            return {"name": configmap.metadata.name, "data": configmap.data}
        return configmap

    def create_configmap(self, configmap_dict: dict):
        configmap = client.V1ConfigMap(
            api_version="v1",
            kind="ConfigMap",
            metadata=client.V1ObjectMeta(
                name=configmap_dict.name, namespace=self.DEFAULT_NAMESPACE
            ),
            data=configmap_dict.data,
        )
        return self.api.create_namespaced_config_map(self.DEFAULT_NAMESPACE, configmap)

    def update_configmap(self, configmap_name: str, configmap_dict: dict):
        configmap = self.get_configmap(configmap_name)
        configmap.data = configmap_dict.data
        return self.api.replace_namespaced_config_map(
            configmap_name, self.DEFAULT_NAMESPACE, configmap
        )
