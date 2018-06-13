UI Cluster Configuration
========================
Configuration of Device URL to use beside the main UI URL

.. tabularcolumns:: |p{4cm}|l|p{8cm}|
.. csv-table:: UI Cluster Configuration Attributes (LDAP Object: dcmUiDeviceCluster)
    :header: Name, Type, Description (LDAP Attribute)
    :widths: 23, 7, 70

    "
    .. _dcmuiDeviceClusterName:

    :ref:`Name <dcmuiDeviceClusterName>`",string,"Cluster Name

    (dcmuiDeviceClusterName)"
    "
    .. _dcmuiDeviceClusterDescription:

    :ref:`Description <dcmuiDeviceClusterDescription>`",string,"Cluster Description

    (dcmuiDeviceClusterDescription)"
    "
    .. _dcmuiDeviceClusterLoadBalancer:

    :ref:`Load Balancer <dcmuiDeviceClusterLoadBalancer>`",string,"Select the Load Balancer

    (dcmuiDeviceClusterLoadBalancer)"
    "
    .. _dcmuiDeviceClusterKeycloakServer:

    :ref:`Keycloak Server <dcmuiDeviceClusterKeycloakServer>`",string,"If this cluster doesn't use the same Keycloak select the configured Keycloak

    (dcmuiDeviceClusterKeycloakServer)"
    "
    .. _dcmuiDeviceClusterDevices:

    :ref:`Device(s) <dcmuiDeviceClusterDevices>`",string,"Add the name of the configured devices

    (dcmuiDeviceClusterDevices)"
    "
    .. _dcmuiDeviceClusterInstalled:

    :ref:`Installed <dcmuiDeviceClusterInstalled>`",boolean,"Use this URL in the UI

    (dcmuiDeviceClusterInstalled)"
