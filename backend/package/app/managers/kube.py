import os
from kubernetes import client, config


class KubernetesManager:
    COMMONLY_IGNORED_CONFIGMAPS = ["kube-root-ca.crt"]
    DEFAULT_NAMESPACE = os.getenv("DEFAULT_NAMESPACE", "default")
    IN_CLUSTER = os.getenv("IN_CLUSTER", False)

    def __init__(self):
        if self.IN_CLUSTER:
            config.load_incluster_config()
        else:
            config.load_kube_config()
        aApiClient = client.ApiClient()
        self.api = client.CoreV1Api(aApiClient)

    def get_configmaps(self):
        formatted_configmaps = []
        configmaps = self.api.list_namespaced_config_map(
            self.DEFAULT_NAMESPACE, pretty=True, watch=False
        )
        for item in configmaps.items:
            if item.metadata.name not in self.COMMONLY_IGNORED_CONFIGMAPS:
                formatted_configmaps.append(
                    {"name": item.metadata.name, "data": item.data}
                )
        return formatted_configmaps

    def get_configmap(self, configmap_name):
        configmap = self.api.read_namespaced_config_map(
            configmap_name, self.DEFAULT_NAMESPACE
        )
        return {"name": configmap.metadata.name, "data": configmap.data}
