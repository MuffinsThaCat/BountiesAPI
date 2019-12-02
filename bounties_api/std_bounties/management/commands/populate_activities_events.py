import requests
from math import pow
from decimal import Decimal
from django.core.management.base import BaseCommand
from std_bounties.models import Activity, Community, Bounty, Event, Comment, FulfillerApplication
import logging
import sys

logger = logging.getLogger('django')


class Command(BaseCommand):
    help = 'Populate the activities table with events'

    def handle(self, *args, **options):
        try:
            all_events = Event.objects.all()
            for event in all_events:
                user = User.objects.get(public_address = event.transaction_from.lower())
                bounty = Bounty.objects.get(id = event.bounty_id)
                activity = Activity.objects.create(
                    event_type = event.event,
                    bounty_id = event.bounty_id,
                    fulfillment_id = event.fulfillment_id,
                    date = event.event_date,
                    transaction_hash = event.transaction_hash,
                    user_id = user.id,
                    community_id = bounty.community_id)

        except Exception as e:
            # goes to rollbar
            logger.exception(e)
            sys.exit(1)
