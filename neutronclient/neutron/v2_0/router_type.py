import logging

from neutronclient.neutron import v2_0 as neutronV20
from neutronclient.openstack.common.gettextutils import _


class ListRouterType(neutronV20.ListCommand):
    """List router types"""
    resource = 'router_type'
    log = logging.getLogger(__name__ + '.ListRouterType')


class ShowRouterType(neutronV20.ShowCommand):
    """Show information of a given router type."""

resource = 'router_type'
log = logging.getLogger(__name__ + '.ShowRouterType')


class CreateRouterType(neutronV20.CreateCommand):
    """Create a router type."""

    resource = 'router_type'
    log = logging.getLogger(__name__ + '.CreateRouter')

    def add_known_arguments(self, parser):
        parser.add_argument(
            'name', metavar='NAME',
            help=_('Name of router type'))
        parser.add_argument(
            '--description',
            help=_('Description of router type'))
        parser.add_argument(
            '--template_id',
            help=_('Id of the template used by this router-type'))
        parser.add_argument(
            '--slot_need', metavar='SLOT NEED',
            help=_('Number of slots needed by this router type'))
        parser.add_argument(
            '--scheduler', metavar='SCHEDULER',
            help=_('Scheduler for this router type'))
        parser.add_argument(
            '--cfg_agent_driver', metavar='DRIVER',
            help=_('Driver to be used by the config agent'))

    def args2body(self, parsed_args):
        body = {'router_type': {
            'name': parsed_args.name}}
        if parsed_args.description:
            body['router_type'].update(
                {'description': parsed_args.description})
        if parsed_args.template_id:
            body['router_type'].update(
                {'template_id': parsed_args.template_id})
        if parsed_args.slot_need:
            body['router_type'].update(
                {'slot_need': parsed_args.slot_need})
        if parsed_args.scheduler:
            body['router_type'].update(
                {'scheduler': parsed_args.scheduler})
        if parsed_args.cfg_agent_driver:
            body['router_type'].update(
                {'cfg_agent_driver': parsed_args.cfg_agent_driver})
        return body


class DeleteRouterType(neutronV20.DeleteCommand):
    """Delete a given router type."""

    log = logging.getLogger(__name__ + '.DeleteRouterType')
    resource = 'router_type'


class UpdateRouterType(neutronV20.UpdateCommand):
    """Update router type's information."""

    log = logging.getLogger(__name__ + '.UpdateRouterType')
    resource = 'router_type'


class ShowRouterType(neutronV20.ShowCommand):
    """Show information of a given router type."""

    resource = 'router_type'
    log = logging.getLogger(__name__ + '.ShowRouterType')


class ListRouterType(neutronV20.ListCommand):
    """List router types."""

    resource = 'router_type'
    log = logging.getLogger(__name__ + '.ListRouterType')
    # list_columns = ['id', 'name', 'firewall_policy_id']
    _formatters = {}
    pagination_support = True
    sorting_support = True
