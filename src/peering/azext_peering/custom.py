# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=unused-argument

import json


def create_peering_asn(cmd, client,
                       name,
                       peer_asn=None,
                       emails=None,
                       phone=None,
                       peer_name=None,
                       validation_state=None):
    body = {}
    body['peer_asn'] = peer_asn  # number
    body.setdefault('peer_contact_info', {})['emails'] = json.loads(emails) if isinstance(emails, str) else emails
    body.setdefault('peer_contact_info', {})['phone'] = json.loads(phone) if isinstance(phone, str) else phone
    body['peer_name'] = peer_name  # str
    body['validation_state'] = validation_state  # str
    return client.create_or_update(peer_asn_name=name, peer_asn=body)


def update_peering_asn(cmd, client, body,
                       name,
                       peer_asn=None,
                       emails=None,
                       phone=None,
                       peer_name=None,
                       validation_state=None):
    body = client.get(peer_asn_name=name).as_dict()
    body.peer_asn = peer_asn  # number
    body.peer_contact_info.emails = json.loads(emails) if isinstance(emails, str) else emails
    body.peer_contact_info.phone = json.loads(phone) if isinstance(phone, str) else phone
    body.peer_name = peer_name  # str
    body.validation_state = validation_state  # str
    return client.create_or_update(peer_asn_name=name, peer_asn=body)


def list_peering_asn(cmd, client):
    return client.list_by_subscription()


def create_peering(cmd, client,
                   resource_group,
                   name,
                   kind,
                   location,
                   sku_name=None,
                   sku_tier=None,
                   sku_family=None,
                   sku_size=None,
                   direct_connections=None,
                   direct_peer_asn=None,
                   direct_direct_peering_type=None,
                   exchange_connections=None,
                   exchange_peer_asn=None,
                   peering_location=None,
                   tags=None):
    body = {}
    body.setdefault('sku', {})['name'] = sku_name  # str
    body.setdefault('sku', {})['tier'] = sku_tier  # str
    body.setdefault('sku', {})['family'] = sku_family  # str
    body.setdefault('sku', {})['size'] = sku_size  # str
    body['kind'] = kind  # str
    body.setdefault('direct', {})['connections'] = json.loads(direct_connections) if isinstance(direct_connections, str) else direct_connections
    body.setdefault('direct', {}).setdefault('peer_asn', {})['id'] = direct_peer_asn
    body.setdefault('direct', {})['direct_peering_type'] = direct_direct_peering_type  # str
    #body.setdefault('exchange', {})['connections'] = json.loads(exchange_connections) if isinstance(exchange_connections, str) else exchange_connections
    #body.setdefault('exchange', {}).setdefault('peer_asn', {})['id'] = exchange_peer_asn
    body['peering_location'] = peering_location  # str
    body['location'] = location  # str
    body['tags'] = tags  # dictionary
    return client.create_or_update(resource_group_name=resource_group, peering_name=name, peering=body)


def update_peering(cmd, client, body,
                   resource_group,
                   name,
                   kind,
                   location,
                   sku_name=None,
                   sku_tier=None,
                   sku_family=None,
                   sku_size=None,
                   direct_connections=None,
                   direct_peer_asn=None,
                   direct_direct_peering_type=None,
                   exchange_connections=None,
                   exchange_peer_asn=None,
                   peering_location=None,
                   tags=None):
    body = client.get(resource_group_name=resource_group, peering_name=name).as_dict()
    body.sku.name = sku_name  # str
    body.sku.tier = sku_tier  # str
    body.sku.family = sku_family  # str
    body.sku.size = sku_size  # str
    body.kind = kind  # str
    body.direct.connections = json.loads(direct_connections) if isinstance(direct_connections, str) else direct_connections
    body.direct.peer_asn = direct_peer_asn
    body.direct.direct_peering_type = direct_direct_peering_type  # str
    body.exchange.connections = json.loads(exchange_connections) if isinstance(exchange_connections, str) else exchange_connections
    body.exchange.peer_asn = exchange_peer_asn
    body.peering_location = peering_location  # str
    body.location = location  # str
    body.tags = tags  # dictionary
    return client.create_or_update(resource_group_name=resource_group, peering_name=name, peering=body)


def list_peering(cmd, client,
                 resource_group):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list_by_subscription()


def create_peering_service_prefix(cmd, client,
                                  resource_group,
                                  peering_service_name,
                                  name,
                                  prefix=None):
    body = {}
    body['prefix'] = prefix  # str
    return client.create_or_update(resource_group_name=resource_group, peering_service_name=peering_service_name, prefix_name=name, peering_service_prefix=body)


def update_peering_service_prefix(cmd, client, body,
                                  resource_group,
                                  peering_service_name,
                                  name,
                                  prefix=None):
    body = client.get(resource_group_name=resource_group, peering_service_name=peering_service_name, prefix_name=name).as_dict()
    body.prefix = prefix  # str
    return client.create_or_update(resource_group_name=resource_group, peering_service_name=peering_service_name, prefix_name=name, peering_service_prefix=body)


def list_peering_service_prefix(cmd, client,
                                resource_group,
                                peering_service_name):
    return client.list_by_peering_service(resource_group_name=resource_group, peering_service_name=peering_service_name)


def create_peering_service(cmd, client,
                           resource_group,
                           name,
                           location,
                           peering_service_location=None,
                           peering_service_provider=None,
                           tags=None):
    body = {}
    body['peering_service_location'] = peering_service_location  # str
    body['peering_service_provider'] = peering_service_provider  # str
    body['location'] = location  # str
    body['tags'] = tags  # dictionary
    return client.create_or_update(resource_group_name=resource_group, peering_service_name=name, peering_service=body)


def update_peering_service(cmd, client, body,
                           resource_group,
                           name,
                           location,
                           peering_service_location=None,
                           peering_service_provider=None,
                           tags=None):
    body = client.get(resource_group_name=resource_group, peering_service_name=name).as_dict()
    body.peering_service_location = peering_service_location  # str
    body.peering_service_provider = peering_service_provider  # str
    body.location = location  # str
    body.tags = tags  # dictionary
    return client.create_or_update(resource_group_name=resource_group, peering_service_name=name, peering_service=body)


def list_peering_service(cmd, client,
                         resource_group):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list_by_subscription()