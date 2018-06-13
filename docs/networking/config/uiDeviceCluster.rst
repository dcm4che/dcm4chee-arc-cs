UI Cluster Configuration
========================
Configuration of Device URL to use beside the main UI URL

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UI Cluster Configuration Attributes (LDAP Object: dcmUiDeviceCluster)
    :header: Name (LDAP Attribute), Type, Description
    :widths: 23, 7, 70

    "
    .. _dcmuiDeviceClusterName:

    :ref:`Name (dcmuiDeviceClusterName) <dcmuiDeviceClusterName>`",string,"Cluster Name"
    "
    .. _dcmuiDeviceClusterDescription:

    :ref:`Description (dcmuiDeviceClusterDescription) <dcmuiDeviceClusterDescription>`",string,"Cluster Description"
    "
    .. _dcmuiDeviceClusterLoadBalancer:

    :ref:`Load Balancer (dcmuiDeviceClusterLoadBalancer) <dcmuiDeviceClusterLoadBalancer>`",string,"Select the Load Balancer"
    "
    .. _dcmuiDeviceClusterKeycloakServer:

    :ref:`Keycloak Server (dcmuiDeviceClusterKeycloakServer) <dcmuiDeviceClusterKeycloakServer>`",string,"If this cluster doesn't use the same Keycloak select the configured Keycloak"
    "
    .. _dcmuiDeviceClusterDevices:

    :ref:`Device(s) (dcmuiDeviceClusterDevices) <dcmuiDeviceClusterDevices>`",string,"Add the name of the configured devices"
    "
    .. _dcmuiDeviceClusterInstalled:

    :ref:`Installed (dcmuiDeviceClusterInstalled) <dcmuiDeviceClusterInstalled>`",boolean,"Use this URL in the UI"
