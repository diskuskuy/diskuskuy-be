from typing import List, Optional
from injector import inject
from datetime import datetime, timedelta
from django.utils import timezone
import pytz

from .models import Thread, Week
from .specs import ThreadDomain, CreateThreadSpec
from .utils import ObjectMapperUtil

class ThreadService:
    @staticmethod
    def get_thread(self, thread_id: int):
        # payment = self.payment_accessor.get(payment_id)
        thread = Thread.objects.get(pk=thread_id)
        # except Thread.DoesNotExist:
        #     return None

        thread_domain = self._convert_to_domain(thread)

        if not thread_domain:
            return None

        return thread_domain

    @staticmethod
    def create_thread(self, spec: CreateThreadSpec):
        week = Week.objects.get(pk=spec.week_id)

        if not week:
            raise Exception(f"Bill object with id: {spec.week_id} not found")

        # payment = self.payment_accessor.create(
        #     PaymentDomain(
        #         bill_id=spec.bill_id,
        #         **ObjectMapperUtil.default_domain_creation_params(),
        #     )
        # )
        thread_domainn = ThreadDomain(
                week_id=spec.week_id,
                title=spec.title,
            )
        thread = self._convert_to_model(obj=thread_domainn, is_create=True)
        thread.save()
        thread_domain = self._convert_to_domain(thread)

        return thread_domain

    @staticmethod
    def _convert_to_domain(obj: Thread) -> ThreadDomain:
        return ObjectMapperUtil.map(obj, ThreadDomain)

    @staticmethod
    def _convert_to_model(obj: ThreadDomain, is_create: bool) -> Thread:
        return Thread(
            id=None if is_create else obj.id,
            title=obj.title,
            week_id=obj.week_id,
        )

   