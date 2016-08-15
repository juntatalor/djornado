"""
Generic handlers for Protobuf REST service
"""
from peewee import IntegrityError
from tornado import web

from project.application import models_pb2


class BaseHandler(web.RequestHandler):
    def get_current_user(self):
        # Получение текущего пользователя
        return self.get_secure_cookie('user')


class PBContentMixin(web.RequestHandler):
    """
    Class to set Protobuf content-type for response
    """

    def initialize(self):
        self.set_header('Content-Type', 'application/x-protobuf')


class PBApiHandlerMixin(object):
    @staticmethod
    def orm_to_message(message, item):
        """
        Peewee ORM model -> Protobuf message
        """
        for field in message.DESCRIPTOR.fields:
            setattr(message, field.name, getattr(item, field.name))

    @staticmethod
    def message_to_orm(message, item, not_empty=False):
        """
        Protobuf message -> Peewee ORM model
        """
        for field in message.DESCRIPTOR.fields:
            if not_empty and not message.HasField(field.name):
                # Skip empty fields when not_empty flag is set
                continue
            setattr(item, field.name, getattr(message, field.name))

    @staticmethod
    def message_to_dict(message):
        """
        Protobuf message -> dict
        """
        save_dict = {}
        for field in message.DESCRIPTOR.fields:
            save_dict[field.name] = getattr(message, field.name)
        return save_dict


class PBApiListHandlerMixin(PBApiHandlerMixin, PBContentMixin):
    """
    Implementation of Protobuf REST interface
    """
    # Peewee model
    model = None
    # Google Protobuf item message
    pb_item_cls = None
    # Google Protobuf list message
    pb_list_cls = None
    # Google protobuf list message field name to store items
    list_field = 'items'
    # Allowed fields to filter
    allowed_filter = []

    def validate(self):
        """
        Override this method for non-Protobuf validation
        """
        try:
            return self.pb_item_cls.FromString(self.request.body)
        except models_pb2._message.DecodeError:
            raise web.HTTPError(400)

    async def create(self, save_dict):
        """
        Override this method for non-create save
        """
        try:
            return await self.application.objects.create(self.model, **save_dict)
        except IntegrityError:
            # Not null, unique constraints etc
            raise web.HTTPError(400)

    @classmethod
    def get_response(cls, items):
        """
        Get byte-encoded response with given collection
        Protobuf implementation
        """
        pb_message = cls.pb_list_cls()
        pb_list = getattr(pb_message, cls.list_field)

        for item in items:
            cls.orm_to_message(pb_list.add(), item)

        return pb_message.SerializeToString()


class ApiListHandler(BaseHandler, PBApiListHandlerMixin):

    @web.authenticated
    async def get(self):
        # Apply filters
        qs = self.model.select()
        filter_qs = {k: v[0] for k, v in self.request.query_arguments.items() if k in self.allowed_filter}
        if filter_qs:
            qs = qs.filter(**filter_qs)
        # Receive items from database
        items = await self.application.objects.execute(qs)

        self.write(self.get_response(items))

    @web.authenticated
    async def post(self):
        # Get protobuf message
        pb_item = self.validate()
        # Save to database
        await self.create(self.message_to_dict(pb_item))

        self.set_status(201)


class ApiItemHandler(BaseHandler, PBApiHandlerMixin):
    # Peewee model
    model = None
    # Model primary key
    model_pk = 'id'
    # Google Protobuf item message
    pb_item_cls = None

    async def get_item(self, item_id):
        # Async get item from database by primary key
        try:
            filter_dict = {
                self.model_pk: item_id
            }
            return await self.application.objects.get(self.model, **filter_dict)
        except self.model.DoesNotExist:
            raise web.HTTPError(404)

    async def save(self, item):
        # Async save to db
        try:
            return await self.application.objects.save(item)
        except IntegrityError:
            raise web.HTTPError(400)

    @web.authenticated
    async def get(self, item_id):
        item = await self.get_item(item_id)

        pb_item = self.pb_item_cls()
        self.orm_to_message(pb_item, item)

        self.write(pb_item)

    @web.authenticated
    async def delete(self, item_id):
        item = await self.get_item(item_id)
        await self.application.objects.delete(item)

        self.set_status(204)

    @web.authenticated
    async def post(self, item_id):
        item = await self.get_item(item_id)

        pb_item = self.pb_item_cls.FromString(self.request.body)
        self.message_to_orm(pb_item, item)

        await self.application.objects.save(item)
        self.set_status(204)

    @web.authenticated
    async def put(self, item_id):
        item = await self.get_item(item_id)

        pb_item = self.pb_item_cls.FromString(self.request.body)
        self.message_to_orm(pb_item, item, not_empty=True)

        await self.application.objects.save(item)
        self.set_status(204)
