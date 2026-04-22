#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: check_disk
short_description: Verifie l'espace disque disponible sur une partition
version_added: "1.0.0"
description:
  - Ce module verifie l'espace disque disponible sur une partition donnee.
  - Il retourne un avertissement si le pourcentage d'utilisation depasse le seuil defini.
options:
  path:
    description:
      - Le chemin de la partition a verifier.
    required: true
    type: str
  threshold:
    description:
      - Le seuil d'utilisation en pourcentage au-dela duquel un avertissement est emis.
    required: false
    type: int
    default: 80
author:
  - Equipe DevOps InfraCloud
'''

EXAMPLES = r'''
- name: Verifier l'espace disque sur /
  infracloud.utils.check_disk:
    path: "/"
    threshold: 80

- name: Verifier /var avec seuil a 90%
  infracloud.utils.check_disk:
    path: "/var"
    threshold: 90
'''

RETURN = r'''
path:
  description: La partition verifiee
  type: str
  returned: always
total_gb:
  description: Espace total en Go
  type: float
  returned: always
used_gb:
  description: Espace utilise en Go
  type: float
  returned: always
free_gb:
  description: Espace libre en Go
  type: float
  returned: always
usage_percent:
  description: Pourcentage d'utilisation
  type: float
  returned: always
threshold:
  description: Seuil configure
  type: int
  returned: always
status:
  description: Statut OK ou WARNING
  type: str
  returned: always
message:
  description: Message descriptif
  type: str
  returned: always
'''

import os
from ansible.module_utils.basic import AnsibleModule


def get_disk_usage(path):
    """Recupere les statistiques d'utilisation disque."""
    statvfs = os.statvfs(path)
    total = statvfs.f_frsize * statvfs.f_blocks
    free = statvfs.f_frsize * statvfs.f_bavail
    used = total - (statvfs.f_frsize * statvfs.f_bfree)

    if total > 0:
        usage_percent = round((used / total) * 100, 1)
    else:
        usage_percent = 0.0

    return {
        'total_gb': round(total / (1024 ** 3), 2),
        'used_gb': round(used / (1024 ** 3), 2),
        'free_gb': round(free / (1024 ** 3), 2),
        'usage_percent': usage_percent
    }


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        threshold=dict(type='int', required=False, default=80),
    )

    result = dict(changed=False)

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    path = module.params['path']
    threshold = module.params['threshold']

    if not os.path.exists(path):
        module.fail_json(msg="Le chemin '{}' n'existe pas.".format(path), **result)

    try:
        disk_info = get_disk_usage(path)
    except OSError as e:
        module.fail_json(msg="Erreur lecture disque pour '{}': {}".format(path, str(e)), **result)

    if disk_info['usage_percent'] >= threshold:
        status = "WARNING"
    else:
        status = "OK"

    message = "Partition {} - Utilisation {}% (seuil: {}%) - Statut: {}".format(
        path, disk_info['usage_percent'], threshold, status
    )

    result['path'] = path
    result['total_gb'] = disk_info['total_gb']
    result['used_gb'] = disk_info['used_gb']
    result['free_gb'] = disk_info['free_gb']
    result['usage_percent'] = disk_info['usage_percent']
    result['threshold'] = threshold
    result['status'] = status
    result['message'] = message

    if status == "WARNING":
        module.warn(message)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
